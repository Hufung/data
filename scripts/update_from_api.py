import requests
import json
import os

# --- Configuration ---
# This is the API endpoint you want to get data from.
API_URL = "https://api.data.gov.hk/v1/carpark-info-vacancy?data=info"

# This is the path to the file in your repository where you want to save the data.
# Make sure the directory (e.g., 'data/') exists in your repo.
OUTPUT_FILE_PATH = "carpark_data.json"
# --- End of Configuration ---

def fetch_api_data():
    """
    Fetches data from the specified API endpoint.
    """
    try:
        response = requests.get(API_URL)
        # Raise an exception for bad status codes (4xx or 5xx)
        response.raise_for_status()
        
        # Assuming the API returns JSON data
        data = response.json()
        print(f"Successfully fetched data from {API_URL}")
        return data
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return None

def save_data_to_file(data, filepath):
    """
    Saves the given data to a file as JSON.
    """
    if data is None:
        print("No data to save.")
        return

    try:
        # Ensure the directory exists
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Write the data to the file
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        print(f"Successfully saved data to {filepath}")
        
    except IOError as e:
        print(f"Error writing data to file: {e}")
    except TypeError as e:
        print(f"Error serializing data to JSON: {e}")

if __name__ == "__main__":
    api_data = fetch_api_data()
    if api_data:
        save_data_to_file(api_data, OUTPUT_FILE_PATH)
