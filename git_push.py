import os
import git

def push_changes_to_github(repo_path, commit_message):
    try:
        repo = git.Repo(repo_path)

        # Check if the repository is dirty (i.e., has modified files)
        if repo.is_dirty(untracked_files=True):
            # Stage all changes
            repo.git.add(A=True)

            # Commit the changes
            repo.index.commit(commit_message)

            # Push the changes to the remote repository
            origin = repo.remote(name='origin')
            origin.push()

            print("Changes have been pushed to GitHub.")
        else:
            print("No changes detected. Nothing to commit.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Path to the local repository
    repo_path = r"C:\Users\I751676\Desktop\Clone_Repo\Template_Repo"

    # Commit message
    commit_message = "Updated YAML files with environment variable values."

    # Push changes to GitHub
    push_changes_to_github(repo_path, commit_message)
