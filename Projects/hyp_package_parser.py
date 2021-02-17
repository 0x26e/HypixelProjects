import grequests
import json
from pprint import pprint

# Get API key
API_FILE = open("API_KEY.json", "r")
API_KEY = json.loads(API_FILE.read())["API_KEY"]

# Setup players to include
players = []
urls = []
gamemode = ""
player_packages = []

# Generate urls
for player in players:
    urls.append(f"https://api.hypixel.net/player?key={API_KEY}&name={player}")

# Send out requests
resp = (grequests.get(url) for url in urls)

# Loop through responses
for idx, data in enumerate(grequests.map(resp)):

    # To save time later
    data = json.loads(data.content)

    # In case there is an error
    if(not data["success"]):
        print(idx, data["cause"])

    # No mistakes in API call
    else:
        try:
            # Filter out bad players (and leave logs)
            if(data["player"] == None):
                print(idx, "Bad name", players[idx])
            elif("stats" not in data["player"]):
                print(idx, "Bad name", players[idx])
            elif(gamemode not in data["player"]["stats"]):
                print(idx, "Bad name", players[idx])

            # To save time later
            p = data["player"]["stats"][gamemode]["packages"]

            # Add player to list
            player_packages.append( ( len(p), data["player"]["displayname"] ) )

        except Exception as e:
            print(e)

# Sort players by package length
sorted_players = sorted(player_packages, key=lambda k: k[0], reverse=True)

# Output sorted players
pprint(sorted_players)
