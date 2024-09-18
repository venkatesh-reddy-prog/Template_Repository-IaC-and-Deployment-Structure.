import os
import yaml
from git import Repo, GitCommandError

repo_url = 'https://github.com/venkatesh-reddy-prog/Template_Repo.git'
clone_dir = 'Template_Repo'
branch_name = 'main'
files_to_modify = {
    'bic/applications/additional-secrets.yaml': 2,
    'bic/applications/btp-secrets.yaml': 1,
    'bic/applications/postgres-app.yaml': 1
}

new_repo_url = os.getenv('NEW_REPO_URL')

if not new_repo_url:
    raise ValueError("The environment variable 'NEW_REPO_URL' is not set.")

def clone_repo(repo_url, clone_dir):
    if not os.path.exists(clone_dir):
        print(f"Cloning repository from {repo_url} into {clone_dir}...")
        Repo.clone_from(repo_url, clone_dir)
        print("Repository cloned successfully.")
    else:
        print(f"Repository already cloned in {clone_dir}.")

def update_yaml(file_path, occurrence):
    full_file_path = os.path.join(clone_dir, file_path)
    print(f"Processing file: {full_file_path}")

    try:
        with open(full_file_path, 'r') as file:
            data = yaml.safe_load(file)
            print(f"Loaded data from {full_file_path}")
    except (IOError, yaml.YAMLError) as e:
        print(f"Error reading {full_file_path}: {e}")
        return

    def find_and_update(data, count=0):
        if isinstance(data, dict):
            for key, value in data.items():
                if key == 'repoURL':
                    count += 1
                    if count == occurrence:
                        print(f"Updating {key} in {file_path} to {new_repo_url}")
                        data[key] = new_repo_url
                count = find_and_update(value, count)
        elif isinstance(data, list):
            for item in data:
                count = find_and_update(item, count)
        return count

    updated_count = find_and_update(data)

    if updated_count > 0:
        try:
            with open(full_file_path, 'w') as file:
                yaml.dump(data, file)
                print(f"Updated {full_file_path} with {updated_count} changes.")
        except IOError as e:
            print(f"Error writing {full_file_path}: {e}")
    else:
        print(f"No updates made to {full_file_path}.")

def main():
    print("Starting script...")
    clone_repo(repo_url, clone_dir)
    
    repo = Repo(clone_dir)

    try:
        print(f"Checking out branch: {branch_name}")
        repo.git.checkout(branch_name)
        repo.git.fetch('origin')
        remote_branches = [b.name for b in repo.remotes.origin.refs]

        if branch_name not in remote_branches:
            print(f"Branch {branch_name} does not exist on remote. Attempting to push...")
            try:
                repo.git.push('origin', branch_name)
                print(f"Branch {branch_name} pushed to remote.")
            except GitCommandError as e:
                print(f"Failed to push branch {branch_name}: {e}")

        print(f"Pulling latest changes from {branch_name}...")
        repo.git.pull('origin', branch_name)

        print("Modifying YAML files...")
        for file_path, occurrence in files_to_modify.items():
            update_yaml(file_path, occurrence)

        print("Adding changes to git...")
        repo.git.add('bic/applications/')

        if repo.is_dirty():
            try:
                print("Committing changes...")
                repo.git.commit(m="Update repoURL in YAML files")
                print("Committed changes.")
                
                print("Pushing changes to remote...")
                repo.git.push('origin', branch_name)
                print("Changes pushed to remote.")
            except GitCommandError as e:
                print(f"Failed to commit or push changes: {e}")
        else:
            print("No changes to commit.")

    except GitCommandError as e:
        print(f"Git command failed: {e}")

if __name__ == "__main__":
    main()
