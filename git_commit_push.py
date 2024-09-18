from git import Repo, GitCommandError

clone_dir = 'Template_Repo'
branch_name = 'main'

def commit_and_push_changes():
    repo = Repo(clone_dir)

    print("Adding changes to git...")
    repo.git.add('bic/applications/')

    if repo.is_dirty():
        try:
            print("Committing changes...")
            repo.git.commit(m="Update repoURL in YAML files")
            print("Committed changes.")
        except GitCommandError as e:
            print(f"Failed to commit changes: {e}")
            return

        try:
            print("Pushing changes to remote...")
            repo.git.push('origin', branch_name)
            print("Changes pushed to remote.")
        except GitCommandError as e:
            print(f"Failed to push changes: {e}")
    else:
        print("No changes to commit.")

if __name__ == "__main__":
    commit_and_push_changes()
