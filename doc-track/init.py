import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Get the DATABASE_URL environment variable
DATABASE_URL = os.getenv('DATABASE_URL')