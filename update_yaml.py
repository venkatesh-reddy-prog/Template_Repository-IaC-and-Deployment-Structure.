# update_yaml.py
import os
import yaml

# Get NEW_REPO_URL from environment variables
new_repo_url = os.getenv('NEW_REPO_URL')

if not new_repo_url:
    raise ValueError("The environment variable 'NEW_REPO_URL' is not set.")

def update_yaml(file_path, occurrence, clone_dir):
    full_file_path = os.path.join(clone_dir, file_path)

    if not os.path.exists(full_file_path):
        print(f"File not found: {full_file_path}")
        return

    print(f"Processing file: {full_file_path}")

    try:
        with open(full_file_path, 'r') as file:
            data = yaml.safe_load(file)
            print(f"Loaded data from {full_file_path}")
    except (IOError, yaml.YAMLError) as e:
        print(f"Error reading {full_file_path}: {e}")
        return

    def find_and_update(data, count=0):
        if isinstance(data, dict):
            for key, value in data.items():
                if key == 'repoURL':
                    count += 1
                    if count == occurrence:
                        print(f"Updating {key} in {file_path} to {new_repo_url}")
                        data[key] = new_repo_url
                count = find_and_update(value, count)
        elif isinstance(data, list):
            for item in data:
                count = find_and_update(item, count)
        return count

    updated_count = find_and_update(data)

    if updated_count > 0:
        try:
            with open(full_file_path, 'w') as file:
                yaml.dump(data, file)
                print(f"Updated {full_file_path} with {updated_count} changes.")
        except IOError as e:
            print(f"Error writing {full_file_path}: {e}")
    else:
        print(f"No updates made to {full_file_path}.")

# Example usage
if __name__ == "__main__":
    clone_dir = 'Template_Repo'
    files_to_modify = {
        'bic/applications/additional-secrets.yaml': 2,
        'bic/applications/btp-secrets.yaml': 1,
        'bic/applications/postgres-app.yaml': 1
    }

    for file_path, occurrence in files_to_modify.items():
        update_yaml(file_path, occurrence, clone_dir)
