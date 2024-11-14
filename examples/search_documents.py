import os
from dotenv import load_dotenv

load_dotenv()

database_password = os.environ.get('DATABASE_PASSWORD')

print(f"Database Password: {database_password}")

def connect_to_database(username, password):
    print("Connecting to database...")
    if password == database_password:
        print("Connected to database successfully.")
    else:
        print("Failed to connect to the database. Incorrect password.")

connect_to_database('admin', os.environ.get('DATABASE_PASSWORD'))