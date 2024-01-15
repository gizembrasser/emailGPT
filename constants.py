import os
from dotenv import load_dotenv

load_dotenv()

# Get environment variables
EMAIL_SERVER = os.getenv("EMAIL_SERVER")
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
PASSWORD = os.getenv("PASSWORD")

# Declare path to file directory
DATA_DIR = os.path.join(os.getcwd(), "data")

# Declare the path to the data files
EMAIL_FILE = os.path.join(DATA_DIR, "emails.txt")
