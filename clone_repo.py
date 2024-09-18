from git import Repo
import os

repo_url = 'https://github.com/venkatesh-reddy-prog/Template_Repo.git'
clone_dir = 'Template_Repo'

def clone_repo(repo_url, clone_dir):
    if not os.path.exists(clone_dir):
        Repo.clone_from(repo_url, clone_dir, depth=1)
    return True

if __name__ == "__main__":
    clone_repo(repo_url, clone_dir)
