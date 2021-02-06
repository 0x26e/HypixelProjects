import json
import grequests
from pprint import pprint

# Returns formatted Smash Heroes Stats
def getSmashHeroes(raw_stats, achievements):

    print(raw_stats)

    # Setup container to hold stats
    sorted_stats = {"General": {}}

    # Setup name conversions
    smash_stat_name_conversions = {"smash_level_total": "smash_level", "games": "games_played", }

    # Setup proper names container
    smash_stat_names = ["active_class", "coins", "wins", "losses", "kills", "deaths", "damage_dealt", "quits"]

    # For every stat in names
    for stat, stat_proper in smash_stat_name_conversions.items():

        # Check if key is in dict, if not set as 0
        sorted_stats["General"][stat_proper] = raw_stats.get(stat, 0)


    # For every stat in proper names
    for stat in smash_stat_names:

        # Check if key is in dict, if not set as 0
        sorted_stats["General"][stat] = raw_stats.get(stat, 0)

    # Setup Smash Heroes classes
    smash_classes = {"THE_BULK": "bulk", "GENERAL_CLUCK": "generalcluck", "BOTMUN": "botmon", "CAKE_MONSTER": "cakemonster", "TINMAN": "tinman",
                    "SKULLFIRE": "skullfire", "FROSTY": "cryomancer", "PUG": "pug", "MARAUDER": "marauder", "DUSK_CRAWLER": "voidcrawler",
                    "SPODERMAN": "spooderman", "GOKU": "karakot", "SHOOP_DA_WHOOP": "shoop", "SANIC": "sanic", "SERGEANT_SHIELD": "sgtshield",
                    "GREEN_HOOD": "greenhood"}

    # Setup Smash Heroes class stats
    smash_class_stats = ["wins", "losses", "games", "kills"]

    # For every class in smash classes
    for smash_class, smash_class_proper in smash_classes.items():

        # Setup class container, add stats with default as 0 if they are not available
        sorted_stats[smash_class_proper] = {
            smash_stat: raw_stats["class_stats"][smash_class].get(smash_stat, 0)
            for smash_stat in smash_class_stats
            }

    # Return cleaned up stats
    return sorted_stats


# Gets all player stats
def getAllStats(url):

    # Async call to url
    resp = grequests.get(url)

    # For every response
    for data in grequests.map([resp]):

        # Load data with JSON
        data = json.loads(data.content)

        # If response successful
        if(data["success"]):

            # Set up player container
            finalized_stats = {"game_stats": {}}

            # If stats for games are present
            if "stats" in data["player"]:

                # If no game stats, add default containers
                data["player"]["stats"] = {
                    gamemode: data["player"]["stats"].get(gamemode, {})
                    for gamemode in hypixel_stats_gamemodes
                }

                # Check every game
                for gm, gm_proper in hypixel_stats_gamemodes.items():

                    # Add proper stats to proper container
                    finalized_stats["game_stats"][gm_proper[0]] = gm_proper[1](data["player"]["stats"][gm], data["player"]["achievements"])

            # If achievements are present
            if "achievements" in data["player"]:
                #stats = getAchievements()
                pass
            else:
                data["player"]["achievements"] = {}


            # Return proper stats container
            return(finalized_stats)

# Get API key from API_KEY.json
API_FILE = open("API_KEY.json", "r")
API_KEY = json.loads(API_FILE.read())["API_KEY"]

# Player to test
NAME = "Hyplex"
# UUID of player to test
UUID = "bec9029b-efb3-4c85-925d-f2e97640cf92"

# URL for Hypixel player endpoint
URL = f"https://api.hypixel.net/player?key={API_KEY}&uuid={UUID}"

# List of gamemodes
hypixel_stats_gamemodes = {"SuperSmash": ("smash_heroes", getSmashHeroes)}

reformed_stats = getAllStats(URL)

pprint(reformed_stats)
