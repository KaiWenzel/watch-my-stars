import requests
import config

class OpenLibrary:
    def __init__(self):
        pass
    
    @staticmethod
    def request(url, id):
        headers = {"User-Agent": config.user_agent, "Accept": "application/json"}
        data = requests.get(f"{url}{id}", headers=headers)
        print("Open Library Code:", data.status_code)
        work = requests.get(f"https://openlibrary.org/authors/{id}/works.json", headers=headers)
        return {"author": data.json(), "work": work.json()}

if __name__ == "__main__":
    print("--- Testing the open library API request ---")