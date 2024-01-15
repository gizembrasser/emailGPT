import os
import sys
import json

grandparent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(grandparent_dir)

from constants import DATA_DIR, EMAIL_FILE
from scripts.emails import get_emails


# Create directory for data files if it doesn't exist
def create_data_files():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)


# Write a list of email dictionaries to a JSON file
def write_to_json(data):
    with open(EMAIL_FILE, "w") as f:
        json.dump(data, f, indent=4) # `indent` adds indentation for better readability


"""write_to_json(get_emails(10))"""