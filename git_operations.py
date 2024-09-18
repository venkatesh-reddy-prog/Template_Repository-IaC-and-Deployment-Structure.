# git_operations.py
from git import GitCommandError, Repo

def git_checkout_pull(repo, branch_name):
    try:
        print(f"Checking out branch: {branch_name}")
        repo.git.checkout(branch_name)
        repo.git.fetch('origin')
        repo.git.pull('origin', branch_name)
        print(f"Pulled latest changes from {branch_name}")
    except GitCommandError as e:
        print(f"Git command failed: {e}")

def git_commit_push(repo, branch_name, files_path):
    try:
        print("Adding changes to git...")
        repo.git.add(files_path)

        if repo.is_dirty():
            print("Committing changes...")
            repo.git.commit(m="Update repoURL in YAML files")
            print("Committed changes.")

            print("Pushing changes to remote...")
            repo.git.push('origin', branch_name)
            print("Changes pushed to remote.")
        else:
            print("No changes to commit.")
    except GitCommandError as e:
        print(f"Failed to commit or push changes: {e}")

# Example usage
if __name__ == "__main__":
    clone_dir = 'Template_Repo'
    branch_name = 'main'
    repo = Repo(clone_dir)

    git_checkout_pull(repo, branch_name)
    git_commit_push(repo, branch_name, 'bic/applications/')
