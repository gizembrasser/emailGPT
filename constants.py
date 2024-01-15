import os
from dotenv import load_dotenv

load_dotenv()

# Get environment variables
EMAIL_SERVER = os.getenv("EMAIL_SERVER")
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
PASSWORD = os.getenv("PASSWORD")

# Declare path to file directory
FILE_DIR = os.path.join
