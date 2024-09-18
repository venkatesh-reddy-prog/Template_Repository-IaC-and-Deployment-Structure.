import os
import yaml

def update_yaml(file_path, occurrence, clone_dir, new_repo_url):
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
