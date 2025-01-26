import os
import random
import datetime
from git import Repo

# Set the repository path (adjust this to your cloned repo's directory)
repo_path = "/Users/vir/Documents/GitHub/autocommit-bot"
repo = Repo(repo_path)

# Number of random commits to make
num_commits = random.randint(10, 30)

for i in range(num_commits):
    # Generate a timestamp for each commit
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

    # Write a change to a file
    with open(os.path.join(repo_path, "activity_log.txt"), "a") as file:
        file.write(f"Commit {i+1} at {timestamp}\n")

    # Stage and commit the change
    repo.git.add("activity_log.txt")
    repo.index.commit(f"Auto-commit: {timestamp}")

# Push the changes
origin = repo.remote(name="origin")
origin.push()
