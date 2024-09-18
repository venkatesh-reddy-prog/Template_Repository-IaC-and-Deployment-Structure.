from git import Repo, GitCommandError
import os

repo_url = 'https://github.com/venkatesh-reddy-prog/Template_Repo.git'
clone_dir = 'Template_Repo'

def clone_repo(repo_url, clone_dir):
    if not os.path.exists(clone_dir):
        print(f"Cloning repository from {repo_url} into {clone_dir}...")
        try:
            Repo.clone_from(repo_url, clone_dir, depth=1)  
            print("Repository cloned successfully.")
        except GitCommandError as e:
            print(f"Error cloning repository: {e}")
            return False
    else:
        print(f"Repository already cloned in {clone_dir}.")
    return True

if __name__ == "__main__":
    clone_repo(repo_url, clone_dir)
