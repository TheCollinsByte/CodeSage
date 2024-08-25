import os
import subprocess
import json
from datetime import datetime

# Function to get the latest commit details
def get_latest_commit_info():
    commit_hash = subprocess.check_output(["git", "rev-parse", "HEAD"]).strip().decode('utf-8')
    commit_info = subprocess.check_output(["git", "show", "--pretty=format:%H|%an|%ae|%ad|%s", "-s", commit_hash]).decode('utf-8')

    commit_details = commit_info.split('|')
    commit_data = {
        "commit_hash": commit_details[0],
        "author_name": commit_details[1],
        "author_email": commit_details[2],
        "date": commit_details[3],
        "message": commit_details[4],
        "timestamp": datetime.now().isoformat()
    }

    return commit_data

# Function to get the diff of the latest commit
def get_commit_diff():
    diff = subprocess.check_output(["git", "diff", "HEAD~1", "HEAD"]).decode('utf-8')
    return diff

# Main function to collect and save data
def collect_commit_data():
    commit_data = get_latest_commit_info()
    commit_diff = get_commit_diff()

    # Merge commit info and diff into one dictionary
    commit_data["diff"] = commit_diff

    # Save the data to a JSON file
    commit_hash = commit_data['commit_hash']
    with open(f'../data/{commit_hash}.json', 'w') as json_file:
        json.dump(commit_data, json_file, indent=4)

    print(f"Commit data for {commit_hash} collected and saved.")

if __name__ == "__main__":
    collect_commit_data()
