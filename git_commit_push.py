from git import Repo

clone_dir = 'Template_Repo'
branch_name = 'main'

def commit_and_push_changes():
    repo = Repo(clone_dir)
    
    repo.git.add('bic/applications/')
    
    if repo.is_dirty():
        repo.git.commit(m="Update repoURL in YAML files")
        repo.git.pull('origin', branch_name)
        repo.git.push('origin', branch_name)

if __name__ == "__main__":
    commit_and_push_changes()
