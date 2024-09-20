import os
import git

def push_changes_to_github(repo_path, commit_message):
    try:
        repo = git.Repo(repo_path)

        if repo.is_dirty(untracked_files=True):
            repo.git.add(A=True)

            repo.index.commit(commit_message)

            origin = repo.remote(name='origin')
            origin.push()

            print("Changes have been pushed to GitHub.")
        else:
            print("No changes to push. Repository is up to date.")
    except Exception as e:
        print(f"Error pushing changes to GitHub: {e}")

if __name__ == "__main__":
    repo_path = r"C:\Users\I751676\Desktop\Clone_Repo\Template_Repo"

    commit_message = "Updated YAML files with environment variable values."

    push_changes_to_github(repo_path, commit_message)
