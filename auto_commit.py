import os
import subprocess
import datetime
import sys

# Your repo path (update this to your actual path)
REPO_PATH = r"C:\Users\user\Desktop\myproject"
DUMMY_FILE = "auto_log.txt"  # File we will keep editing

TOTAL_COMMITS = 3000         # Number of commits to make
COMMITS_PER_PUSH = 1000      # Push every commit

print("Script started")

try:
    os.chdir(REPO_PATH)
    print(f"Changed directory to: {REPO_PATH}")
except Exception as e:
    print(f"Failed to change directory: {e}")
    sys.exit(1)

print("🚀 Starting automated commits...")

for i in range(1, TOTAL_COMMITS + 1):
    try:
        # Edit the file
        with open(DUMMY_FILE, "a") as f:
            f.write(f"Commit #{i} - {datetime.datetime.now()}\n")
        print(f"Updated {DUMMY_FILE} for commit #{i}")
    except Exception as e:
        print(f"Failed to write to {DUMMY_FILE}: {e}")
        sys.exit(1)

    try:
        # Stage the file
        subprocess.run(["git", "add", DUMMY_FILE], check=True)
        print(f"Staged {DUMMY_FILE}")
    except subprocess.CalledProcessError as e:
        print(f"git add failed: {e}")
        sys.exit(1)

    try:
        # Commit changes
        subprocess.run(["git", "commit", "-m", f"Auto Commit #{i}"], check=True)
        print(f"Committed Auto Commit #{i}")
    except subprocess.CalledProcessError as e:
        print(f"git commit failed: {e}")
        sys.exit(1)

    # Push commits in batches
    if i % COMMITS_PER_PUSH == 0 or i == TOTAL_COMMITS:
        try:
            print(f"📤 Pushing at commit #{i}...")
            subprocess.run(["git", "push", "origin", "main"], check=True)
            print(f"Pushed commit #{i} successfully")
        except subprocess.CalledProcessError as e:
            print(f"git push failed: {e}")
            sys.exit(1)

print("✅ All commits done and pushed.")
