import config
from extract.wikidata import WikiData
from extract.musicbrainz import MusicBrainz
from extract.openlibrary import OpenLibrary

people = ["Q20882479", "Q47447", "Q1200066", "Q615", "Q134237"]
person_data = {}


def main():
    extract()

def extract():

    wikidata = WikiData()
    musicbrainz = MusicBrainz()
    openlibrary = OpenLibrary()

    data = wikidata.request(config.wiki_url, people[2], config.user_agent)
    human = wikidata.is_human(data)
    print("Is human:", human)
    celebrity = wikidata.is_celebrity(data)
    print("Is celebrity:", celebrity)
    if human and celebrity:
        musicbrainz_id = wikidata.get_musicbrainz_id(data)
        print("MusicBrainz ID:", musicbrainz_id)
        openlibrary_id = wikidata.get_openlibrary_id(data)
        print("Open Library ID:", openlibrary_id)


    if musicbrainz_id:
        #music_data = musicbrainz.request(config.musicbrainz_url, musicbrainz_id)
        #print(music_data)
        pass
    if openlibrary_id:
        book_data = openlibrary.request(config.openlibrary_url, openlibrary_id)
        print(book_data)

    


if __name__ == "__main__":
    main()