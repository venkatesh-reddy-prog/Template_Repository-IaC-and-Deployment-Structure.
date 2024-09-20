import os
import git

repo_url = "https://github.com/venkatesh-reddy-prog/Template_Repo.git"
clone_dir = r"C:\Users\I751676\Desktop\Clone_Repo\Template_Repo"

if os.path.exists(clone_dir):
    print("Skipping cloning.")
else:
    git.Repo.clone_from(repo_url, clone_dir)
    print(f"Repository cloned ")
