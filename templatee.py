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

def clone_repo(repo_url, clone_dir):
    if not os.path.exists(clone_dir):
        Repo.clone_from(repo_url, clone_dir)

def update_yaml(file_path, occurrence):
    full_file_path = os.path.join(clone_dir, file_path)
    with open(full_file_path, 'r') as file:
        data = yaml.safe_load(file)

    def find_and_update(data, count=0):
        if isinstance(data, dict):
            for key, value in data.items():
                if key == 'repoURL':
                    count += 1
                    if count == occurrence:
                        data[key] = new_repo_url
                count = find_and_update(value, count)
        elif isinstance(data, list):
            for item in data:
                count = find_and_update(item, count)
        return count

    find_and_update(data)

    with open(full_file_path, 'w') as file:
        yaml.dump(data, file)
    print(f"Updated {file_path}")

def main():
    clone_repo(repo_url, clone_dir)
    
    repo = Repo(clone_dir)

    try:
        branch_exists = branch_name in [b.name for b in repo.branches]
        if not branch_exists:
            print(f"Branch '{branch_name}' does not exist locally. Creating it.")
            repo.git.checkout('HEAD', b=branch_name)
        else:
            repo.git.checkout(branch_name)

        repo.git.fetch('origin')
        remote_branches = [b.name for b in repo.remotes.origin.refs]

        if branch_name not in remote_branches:
            print(f"Branch '{branch_name}' does not exist on the remote. Pushing it.")
            repo.git.push('origin', branch_name)

        try:
            repo.git.pull('origin', branch_name)
        except GitCommandError as e:
            print(f"Error pulling from remote: {e}")

        for file_path, occurrence in files_to_modify.items():
            update_yaml(file_path, occurrence)

        repo.git.add('bic/applications/')
        
        if repo.is_dirty():
            repo.git.commit(m="Update repoURL in YAML files")
            push_result = repo.git.push('origin', branch_name)
            print(f"Pushed changes to {repo_url}")
        else:
            print("No changes to commit.")

    except GitCommandError as e:
        print(f"Git error: {e}")

if __name__ == "__main__":
    main()
