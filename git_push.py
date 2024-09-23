import os
import git # type: ignore

def commit_and_push_changes(repo_dir):
    try:
        repo = git.Repo(repo_dir)
        
        repo.git.add(all=True)
        
        repo.git.commit('-m', 'Update YAML files')
        
        repo.git.push()
        
        print("Changes have been committed and pushed to the remote repository.")
    except Exception as e:
        print(f"An error occurred while pushing changes: {e}")

if __name__ == "__main__":
    dest_clone_dir = r"C:\Users\I751676\Desktop\Clone_Repo\Demo1-Folder"

    if os.path.exists(dest_clone_dir):
        commit_and_push_changes(dest_clone_dir)
    else:
        print("Destination repository does not exist. Please clone it first.")
