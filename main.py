from Projects.hyp_parse_everything import *
import json
# Get API key from API_KEY.json
API_FILE = open("API_KEY.json", "r")
API_KEY = json.loads(API_FILE.read())["API_KEY"]

# Players for testing
known_players = {
    "Global":
    ( ("greaneye", "1fc7b5e6-c8e1-433b-a41e-7013ab0a3582"),
      ("Anchor_Falls", "d0cdf17b-f8bd-4195-a8ab-c366bd5eb7c3"), ),
    "SmashHeroes":
    ( ("Hyplex", "bec9029b-efb3-4c85-925d-f2e97640cf92"),
      ("Focus_Energy", "2de27887-dbb9-4154-8a36-029d6de5f468"), ),
    "Bedwars":
    ( ("TheCleb", "ed6dd177-717a-43b3-b17b-f02031cfac4e"), ),
    "Quake":
    ( ("Govo", "511a4cd1-138b-45b9-8d39-3680454bd6e3"),
      ("Rackals", "e2f69d3e-e11d-4870-81b6-08ed6bdf09c0"), ),
    }

# Select player for testing
player_to_test = ("SmashHeroes", 0)

# Player to test
NAME = known_players[player_to_test[0]][player_to_test[1]][0]
# UUID of player to test
UUID = known_players[player_to_test[0]][player_to_test[1]][1]

print(NAME, UUID)

# URL for Hypixel player endpoint
URL = f"https://api.hypixel.net/player?key={API_KEY}&uuid={UUID}"

reformed_stats = getAllStats(URL)

pprint(reformed_stats)

print("Total stats parsed: ", get_total_keys(reformed_stats))

print("Total bytes stored: ", get_total_bytes(reformed_stats))
