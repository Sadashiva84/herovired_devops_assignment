# This is the question4 of the assignment
'''
In DevOps, performing regular backups of important files is crucial:

●       Implement a Python script called backup.py that takes a source directory and a destination directory as command-line arguments.

●       The script should copy all files from the source directory to the destination directory.

●       Before copying, check if the destination directory already contains a file with the same name. If so, append a timestamp to the file name to ensure uniqueness.

●       Handle errors gracefully, such as when the source directory or destination directory does not exist.

'''

import os
import sys
import shutil
from datetime import datetime

def backup_files(source_dir, dest_dir):
    # Create the destination directory if it doesn't exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Create or append to the log file
    log_file = os.path.join(dest_dir, "backup_log.txt")
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as file:
        file.write(current_time + "\n")

    # Backup files from the source directory to the destination directory
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            source_path = os.path.join(root, file)
            dest_path = os.path.join(dest_dir, file)
            shutil.copy2(source_path, dest_path)

if __name__ == "__main__":
    # Check if the source directory and destination directory are provided as command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python3 backup.py <source directory> <destination directory>")
        sys.exit(1)

    source_directory = sys.argv[1]
    destination_directory = sys.argv[2]

    backup_files(source_directory, destination_directory)
