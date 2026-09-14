import requests
import config

class MusicBrainz:
    def __init__(self):
        pass
    
    @staticmethod
    def request(url, id):
        headers = {"User-Agent": config.user_agent}
        data = requests.get(f"{url}{id}", headers=headers, params=config.musicbrainz_params)
        print("MusicBrainz Status Code:", data.status_code)
        return data.json()
    



if __name__ == "__main__":
    print("--- Testing the musicbrainz API request ---")