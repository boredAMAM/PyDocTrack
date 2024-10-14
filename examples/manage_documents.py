import os
from dotenv import load_dotenv

load_dotenv()

def demo_env_variables():
    example_api_key = os.getenv("EXAMPLE_API_KEY", "DefaultApiKey")
    print(f"Using API Key: {example_api_key}")

if __name__ == "__main__":
    demo_env_variables()