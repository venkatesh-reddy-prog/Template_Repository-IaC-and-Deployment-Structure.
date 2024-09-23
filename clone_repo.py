import os
import git  # type: ignore

def clone_repositories(source_repo_url, dest_repo_url, source_clone_dir, dest_clone_dir):
    if not os.path.exists(source_clone_dir):
        git.Repo.clone_from(source_repo_url, source_clone_dir)
        print("Source repository cloned.")
    else:
        print("Source repository already exists. Skipping clone.")

    if not os.path.exists(dest_clone_dir):
        git.Repo.clone_from(dest_repo_url, dest_clone_dir)
        print("Destination repository cloned.")
    else:
        print("Destination repository already exists. Skipping clone.")

if __name__ == "__main__":
    source_repo_url = "https://github.com/venkatesh-reddy-prog/Template_Repo.git"
    source_clone_dir = r"C:\Users\I751676\Desktop\Clone_Repo\Template_Repo"
    dest_repo_url = "https://github.com/venkatesh-reddy-prog/Demo1-Folder.git"
    dest_clone_dir = r"C:\Users\I751676\Desktop\Clone_Repo\Demo1-Folder"

    clone_repositories(source_repo_url, dest_repo_url, source_clone_dir, dest_clone_dir)
