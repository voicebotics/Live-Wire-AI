import requests
import os
from dotenv import load_dotenv

# Load API keys from .env file
load_dotenv()

GHL_API_KEY = os.getenv("GHL_API_KEY")
GHL_BASE_URL = "https://api.gohighlevel.com/v1"

# Function to fetch client's past info
def fetch_client_data(client_id):
    response = requests.get(f"{GHL_BASE_URL}/contacts/{client_id}", headers={
        "Authorization": f"Bearer {GHL_API_KEY}"
    })
    return response.json() if response.status_code == 200 else {"error": "Client data not found or error with API."} # returns the contact's (client's) info
