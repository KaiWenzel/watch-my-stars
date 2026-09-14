wiki_url = "https://www.wikidata.org/w/rest.php/wikibase/v1/entities/items/"
musicbrainz_url = "https://musicbrainz.org/ws/2/artist/"
musicbrainz_params = params = {"fmt": "json", "inc": "release-groups+url-rels+genres+tags+aliases",}
openlibrary_url = "https://openlibrary.org/authors/"
user_agent = "CelebrityAggregator/1.0 (my_celebrity@example.com)"


HUMAN_ID = "Q5"
OCCUPATIONS = [ 
    # --- ACTORS ---
    "Q33999",          # Actor
    "Q10798782",       # Voice actor
    "Q10800557",       # Film actor
    "Q2405480",        # Television actor
    "Q2188235",        # Stage actor

    # --- WRITERS / AUTHORS ---
    "Q36180",    # Writer
    "Q6625963",   # Novelist
    "Q28389",    # Screenwriter
    "Q18844224", # Non-fiction writer
    "Q482980",   # Author
    "Q1175151",  # Poet
    "Q214917",   # Playwright

    # --- MUSICIANS ---
    "Q639669",     # Musician
    "Q177220",     # Singer
    "Q753110",     # Songwriter
    "Q85505",      # Guitarist
    "Q488205",     # Singer-songwriter
    "Q1868",       # Pianist
    "Q158852",     # Conductor
    "Q130847"
]