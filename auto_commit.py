import os
import random
import datetime
from git import Repo

# Path to your repository
repo_path = "/Users/vir/Documents/GitHub/autocommit-bot"
log_file = os.path.join(repo_path, "cron_debug.log")

# List of random commit messages
commit_messages = [
    "Update activity log 📄",
    "Automated commit ✅",
    "Daily log entry 📝",
    "Streak saver 🔥",
    "Added new timestamp ⏰",
    "Keep the streak alive 💪",
    "Refresh log file 🕒",
    "Improved activity log 🚀",
    "Systematic log update 🔄",
    "Log entry update 📈",
]


# Function to log messages
def log_message(message):
    with open(log_file, "a") as log:
        log.write(f"{datetime.datetime.now()}: {message}\n")


try:
    # Initialize the repository
    repo = Repo(repo_path)
    log_message("Initialized Git repository.")

    # Sync local repository with remote
    try:
        log_message("Fetching changes from remote repository...")
        repo.git.fetch()
        log_message("Resetting local branch to match remote...")
        repo.git.reset("--hard", "origin/main")
        log_message("Local repository successfully synced with remote.")
    except Exception as sync_error:
        log_message(f"Error during sync: {sync_error}")

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

        # Choose a random commit message
        random_message = random.choice(commit_messages)
        log_message(f"Selected commit message: {random_message}")

        # Stage and commit the changes
        repo.git.add("activity_log.txt")
        repo.index.commit(f"{random_message}: {timestamp}")
        log_message(f"Committed changes: {random_message}: {timestamp}")

    # Push the changes to the remote repository
    log_message("Attempting to push changes...")
    origin = repo.remote(name="origin")
    try:
        origin.push()
        log_message("Push successful.")
    except Exception as push_error:
        log_message(f"Push failed: {push_error}")

except Exception as e:
    log_message(f"Script failed: {e}")
