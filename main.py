# main.py
import os
from git import Repo
from clone_repo import clone_repo
from update_yaml import update_yaml
from git_operations import git_checkout_pull, git_commit_push

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

def main():
    print("Starting script...")

    # Clone the repository
    if not clone_repo(repo_url, clone_dir):
        print("Cloning failed, exiting script.")
        return
    
    repo = Repo(clone_dir)

    git_checkout_pull(repo, branch_name)

    print("Modifying YAML files...")
    for file_path, occurrence in files_to_modify.items():
        update_yaml(file_path, occurrence, clone_dir, new_repo_url)

    git_commit_push(repo, branch_name, 'bic/applications/')

if __name__ == "__main__":
    main()
