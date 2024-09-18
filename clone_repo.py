# clone_repo.py
import os
import time
from git import Repo, exc

def clone_repo(repo_url, clone_dir):
    if not os.path.exists(clone_dir):
        print(f"Cloning repository from {repo_url} into {clone_dir}...")
        start_time = time.time()
        try:
            Repo.clone_from(repo_url, clone_dir)
            print(f"Repository cloned successfully in {time.time() - start_time} seconds.")
        except exc.GitCommandError as e:
            print(f"Error cloning repository: {e}")
            return False
    else:
        print(f"Repository already cloned in {clone_dir}.")
    return True

# Execute the function if this file is run directly
if __name__ == "__main__":
    repo_url = 'https://github.com/venkatesh-reddy-prog/Template_Repo.git'
    clone_dir = 'Template_Repo'
    clone_repo(repo_url, clone_dir)
