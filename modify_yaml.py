import yaml
import os

clone_dir = 'Template_Repo'
files_to_modify = {
    'bic/applications/additional-secrets.yaml': 2,
    'bic/applications/btp-secrets.yaml': 1,
    'bic/applications/postgres-app.yaml': 1
}

new_repo_url = os.getenv('NEW_REPO_URL')

if not new_repo_url:
    raise ValueError("The environment variable 'NEW_REPO_URL' is not set.")

def update_yaml(file_path, occurrence):
    full_file_path = os.path.join(clone_dir, file_path)
    
    if not os.path.exists(full_file_path):
        return
    
    with open(full_file_path, 'r') as file:
        data = yaml.safe_load(file)

    def find_and_update(data, count=0):
        if isinstance(data, dict):
            for key, value in data.items():
                if key == 'repoURL':
                    count += 1
                    if count == occurrence:
                        data[key] = new_repo_url
                count = find_and_update(value, count)
        elif isinstance(data, list):
            for item in data:
                count = find_and_update(item, count)
        return count

    find_and_update(data)
    
    with open(full_file_path, 'w') as file:
        yaml.dump(data, file)

if __name__ == "__main__":
    for file_path, occurrence in files_to_modify.items():
        update_yaml(file_path, occurrence)
