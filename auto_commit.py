import os
import random
import datetime
from git import Repo

# Path to your repository
repo_path = "/Users/vir/Documents/GitHub/autocommit-bot"
log_file = os.path.join(repo_path, "cron_debug.log")


# Function to log messages
def log_message(message):
    with open(log_file, "a") as log:
        log.write(f"{datetime.datetime.now()}: {message}\n")


try:
    # Initialize the repository
    repo = Repo(repo_path)
    log_message("Initialized Git repository.")

    # Number of random commits to make
    num_commits = random.randint(10, 30)
    log_message(f"Number of commits to make: {num_commits}")

    for i in range(num_commits):
        # Generate a timestamp for the commit
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

        # Write a change to a file
        with open(os.path.join(repo_path, "activity_log.txt"), "a") as file:
            file.write(f"Commit {i+1} at {timestamp}\n")
        log_message(f"Written Commit {i+1} at {timestamp} to activity_log.txt")

        # Stage and commit the changes
        repo.git.add("activity_log.txt")
        repo.index.commit(f"Auto-commit: {timestamp}")
        log_message(f"Committed changes: Auto-commit {timestamp}")

    # Push the changes to the remote repository
    log_message("Attempting to push changes...")
    origin = repo.remote(name="origin")
    try:
        origin.push()
        log_message("Push successful.")
    except Exception as push_error:
        log_message(f"Push failed: {push_error}")

    # Pull the latest changes from the remote repository
    log_message("Pulling latest changes from remote...")
    try:
        repo.git.pull()
        log_message("Pull successful.")
    except Exception as pull_error:
        log_message(f"Pull failed: {pull_error}")

except Exception as e:
    log_message(f"Script failed: {e}")
