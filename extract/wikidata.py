import requests 
import config


class WikiData:
    def __init__(self):
        pass
    
    # Safely retrieve from 'statements' or fallback to 'claims'
    def use_claims(self, data, id):
       result = (
           data.get("statements", {}).get(id) 
           or data.get("claims", {}).get(id) 
           or []
       )
       return result

    # Requesting celebrity data from wikidata API and returning JSON
    @staticmethod
    def request(url, wikidata_id, agent):
        headers = {'User-Agent': agent}
        raw_data = requests.get(f"{url}{wikidata_id}", headers=headers)
        print("Wikidata request: ", raw_data.status_code)

        if raw_data.status_code == 200:
            return raw_data.json()
        else:
            print("There occured an error when handling your wikidata request.") 

    #Checking if entry is a human
    def is_human(self, data): 
        for stmt in self.use_claims(data, "P31"):
            # Check standard dump structure (mainsnak -> datavalue -> value -> id)
            q_id_dump = (
                stmt.get("mainsnak", {})
                .get("datavalue", {})
                .get("value", {})
                .get("id")
            )
            
            # Check REST API / processed dump structure (value -> content)
            q_id_api = stmt.get("value", {}).get("content")
            
            if q_id_dump == config.HUMAN_ID or q_id_api == config.HUMAN_ID:
                return True

        return False
    
    # Check if person is actor, musician, or author
    def is_celebrity(self, data):
        for stmt in self.use_claims(data, "P106"):
            # Check standard dump structure (mainsnak -> datavalue -> value -> id)
            q_id_dump = (
                stmt.get("mainsnak", {})
                .get("datavalue", {})
                .get("value", {})
                .get("id")
            )

            # Check REST API / processed dump structure (value -> content)
            q_id_api = stmt.get("value", {}).get("content")

            if q_id_dump in config.OCCUPATIONS or q_id_api in config.OCCUPATIONS:
                return True
        return False
    
    def get_musicbrainz_id(self, data):
        for stmt in self.use_claims(data, "P434"):
            # Check standard dump structure (mainsnak -> datavalue -> value -> id)
            q_id_dump = (
                stmt.get("mainsnak", {})
                .get("datavalue", {})
                .get("value", {})
            )

            # Check REST API / processed dump structure (value -> content)
            q_id_api = stmt.get("value", {}).get("content")

            if q_id_dump:
                return q_id_dump
            elif q_id_api:
                return q_id_api
            else:
                return False
            
    def get_openlibrary_id(self, data):
        for stmt in self.use_claims(data, "P648"):
            # Check standard dump structure (mainsnak -> datavalue -> value -> id)
            q_id_dump = (
                stmt.get("mainsnak", {})
                .get("datavalue", {})
                .get("value", {})
            )

            # Check REST API / processed dump structure (value -> content)
            q_id_api = stmt.get("value", {}).get("content")

            if q_id_dump:
                return q_id_dump
            elif q_id_api:
                return q_id_api
            else:
                return False

if __name__ == "__main__":
    print("--- Testin wikidata extraction ---")
