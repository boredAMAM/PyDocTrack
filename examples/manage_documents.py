import os
from dotenv import load_dotenv

load_dotenv()  # Loads environment variables from a .env file.

def display_environment_variable():
    # Retrieves the API Key from environment variables; uses a default value if not found.
    apiKey = os.getenv("EXAMPLE_API_KEY", "DefaultApiKey")
    print(f"Using API Key: {apiKey}")

if __name__ == "__main__":
    display_environment_variable()