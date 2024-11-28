import os
import time
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

try:
    database_password = os.environ['DATABASE_PASSWORD']  # Using direct access to ensure KeyError is raised if not found
except KeyError:
    print("Error: DATABASE_PASSWORD not set in the environment variables.")
    exit(1)  # Exits the program if no database password is provided

tracked_files = {}  # Initialized to keep track of files and their modification times.

print(f"Database Password: {database_password}")

def connect_to_database(username, password):
    print("Connecting to database...")
    if password == database_password:
        print("Connected to database successfully.")
    else:
        print("Failed to connect to the database. Incorrect password.")

def track_file(file_path):
    """Add a file to the tracking list."""
    try:
        if os.path.isfile(file_path):
            tracked_files[file_path] = os.path.getmtime(file_path)
            print(f"Started tracking {file_path}")
        else:
            print(f"The file {file_path} does not exist and cannot be tracked.")
    except Exception as e:
        print(f"An error occurred while attempting to track {file_path}: {e}")

def check_tracked_files():
    """Check the status of tracked files and log changes."""
    for file_path, last_mod_time in tracked_files.items():
        try:
            if os.path.isfile(file_path):
                current_mod_time = os.path.getmtime(file_path)
                if current_mod_time != last_mod_time:
                    print(f"File {file_path} was modified.")
                    print(f"Previous modification time: {datetime.fromtimestamp(last_mod_time).strftime('%Y-%m-%d %H:%M:%S')}")
                    print(f"Current modification time: {datetime.fromtimestamp(current_mod_time).strftime('%Y-%m-%d %H:%M:%S')}")
                    tracked_files[file_path] = current_mod_time  # Update the tracking info
                else:
                    print(f"No changes detected for {file_path}.")
            else:
                print(f"The file {file_path} was removed or cannot be accessed.")
        except Exception as e:
            print(f"An error occurred while checking {file_path}: {e}")

# Example usage
try:
    connect_to_database('admin', os.environ.get('DATABASE_PASSWORD'))
except TypeError:
    print("Database connection failed. Check if DATABASE_PASSWORD is correctly set.")

# Add files to track
try:
    track_file('/path/to/your/document.txt')  # Replace '/path/to/your/document.txt' with your actual file path
except FileNotFoundError:
    print("Failed to track file: File not found.")

# Check tracked files for changes periodically
# For constant monitoring, you can put this in a loop with a sleep timer
try:
    check_tracked_files()
except Exception as generalError:
    print(f"An unexpected error occurred: {generalError}")