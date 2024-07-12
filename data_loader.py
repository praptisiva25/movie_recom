import requests
import pickle

def download_and_load_pkl(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = pickle.loads(response.content)
            return data
        else:
            print(f"Failed to download file from {url}. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred while downloading from {url}: {e}")
        return None
