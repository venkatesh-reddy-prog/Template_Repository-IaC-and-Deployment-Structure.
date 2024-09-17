import os
import yaml
from git import Repo

# Configuration
repo_url = 'https://github.com/venkatesh-reddy-prog/Template_Repo.git'
clone_dir = 'Template_Repo'
yaml_file_path = 'bic/applications/additional-secrets.yaml'
branch_name = 'update-repo-url'

# Retrieve the new repo URL from environment variable
new_repo_url = os.getenv('NEW_REPO_URL')
if not new_repo_url:
    raise ValueError("Environment variable 'NEW_REPO_URL' not set")

# Clone the repository
if not os.path.exists(clone_dir):
    print(f"Cloning repository from {repo_url}...")
    Repo.clone_from(repo_url, clone_dir)
else:
    print(f"Repository already cloned. Updating local repository...")
    repo = Repo(clone_dir)
    repo.remotes.origin.pull()

# Open the repository
repo = Repo(clone_dir)

# Create and switch to a new branch
if branch_name in repo.branches:
    repo.git.checkout(branch_name)
else:
    repo.git.checkout('HEAD', b=branch_name)

# Path to the YAML file
full_yaml_path = os.path.join(clone_dir, yaml_file_path)

# Read the YAML file
with open(full_yaml_path, 'r') as file:
    data = yaml.safe_load(file)

# Update the repoURL in the YAML content
data['spec']['sources'][1]['repoURL'] = new_repo_url

# Write the updated YAML back to the file
with open(full_yaml_path, 'w') as file:
    yaml.dump(data, file)

# Stage, commit, and push the changes
repo.git.add(yaml_file_path)
repo.git.commit(m="Update repoURL in additional-secrets.yaml")
repo.git.push('origin', branch_name)

print(f"Updated repoURL to {new_repo_url} in {yaml_file_path} and pushed changes to {branch_name} branch")
