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
