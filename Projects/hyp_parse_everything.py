import json
import grequests
from pprint import pprint

# Get number of stats from nested dict/lists
def get_total_keys(data):

    if not isinstance(data, dict):
        return 0

    nested_keys = sum(get_total_keys(value) for key, value in data.items())
    return len(data) + nested_keys

# Returns formatted Smash Heroes Stats
def getSmashHeroes(raw_stats, achievements):

    # Setup container to hold stats
    sorted_stats = {"general": {}, "booster": {}}

    # Setup proper name conversions
    smash_stat_name_conversions = {"smash_level_total": "smash_level", "games": "games_played", "smasher": "damage_kills", "smashed": "damage_deaths"}

    # Setup stat names container
    smash_stat_names = ["active_class", "coins", "wins", "losses", "kills", "deaths", "damage_dealt", "quits",
        "games_weekly_a", "games_weekly_b", "games_monthly_a", "games_monthly_b",
        "wins_weekly_a", "wins_weekly_b", "wins_monthly_a", "wins_monthly_b",
        "losses_weekly_a", "losses_weekly_b", "losses_monthly_a", "losses_monthly_b",
        "kills_weekly_a", "kills_weekly_b", "kills_monthly_a", "kills_monthly_b"]

    # Setup Smash Heroes classes
    smash_classes = {"THE_BULK": "bulk", "GENERAL_CLUCK": "generalcluck", "BOTMUN": "botmon", "CAKE_MONSTER": "cakemonster", "TINMAN": "tinman",
        "SKULLFIRE": "skullfire", "FROSTY": "cryomancer", "PUG": "pug", "MARAUDER": "marauder", "DUSK_CRAWLER": "voidcrawler", "SPODERMAN": "spooderman",
        "GOKU": "karakot", "SHOOP_DA_WHOOP": "shoop", "SANIC": "sanic", "SERGEANT_SHIELD": "sgtshield", "GREEN_HOOD": "greenhood"
        }

    # Setup Smash Heroes class stats
    smash_class_stats = ["wins", "losses", "games", "kills", "deaths", "damage_dealt"]
    # ! # Still need to add in Smasher and Smashed

    # Setup Smash Heroes gamemodes
    smash_gamemodes = {"normal": "1v1v1v1", "2v2": "2v2", "teams": "2v2v2"}

    # Setup stats from class stats with proper naming
    smash_class_stat_conversions = {"smasher": "damage_kills", "smashed": "damage_deaths"}

    # Setup class-specific damage abilities
    smash_classes_abilities = {"THE_BULK": ("boulder", "monster_charge", "monster_mash", "seismic_slam"),
        "GENERAL_CLUCK": ("bazooka", "egg_bazooka", "reinforcements"),
        "BOTMUN": ("batarang", "grappling_hook", "botmubile"),
        "CAKE_MONSTER": ("swing_pin", "throw_cake", "cake_storm", "defecake"),
        "TINMAN": ("laser_cannon", "rocket_punch", "homing_missiles", "overload"),
        "SKULLFIRE": ("desert_eagle", "grenade", "flaming_desert_eagle"),
        "FROSTY": ("frostbolt", "freezing_breath"),
        "PUG": ("bite", "supersonic_bark", "werepug"),
        "MARAUDER": ("force_lightning", "force_pull"),
        "DUSK_CRAWLER": ("void_slash", "teleboom", "telepunch"),
        "SPODERMAN": ("spider_kick", "web_shot", "spooder_buddies"),
        "GOKU": ("ki_blast", "kame_beam"),
        "SHOOP_DA_WHOOP": ("static_laser", "charged_beam", "fir_ma_lazer", "ride_the_lightning"),
        "SANIC": ("dash", "boom", "onion_cannon"),
        "SERGEANT_SHIELD": ("shield_bash", "ricochet", "shield_quake"),
        "GREEN_HOOD": ("notched_bow", "flying_punch")
        }

    # Setup Smash Heroes class stats that are in general section
    smash_class_stats_from_general = {"xp_": "real_xp", "lastLevel_": "level", "pg_": "prestige", "masterArmor_": "hasMasterArmor"}

    # Exp Booster stats
    sorted_stats["booster"]["active_exp_booster"] = raw_stats.get("expired_booster", False)
    sorted_stats["booster"]["exp_booster_count"] = raw_stats.get("expBooster_purchases_10_plays", 0) * 10
    sorted_stats["booster"]["exp_booster_count"] += raw_stats.get("expBooster_purchases_30_plays", 0) * 30
    sorted_stats["booster"]["exp_booster_count"] += raw_stats.get("expBooster_purchases_50_plays", 0) * 50
    sorted_stats["booster"]["exp_booster_count"] += raw_stats.get("expBooster_purchases_100_plays", 0) * 100

    # For every proper stat in names
    for stat, stat_proper in smash_stat_name_conversions.items():

        # Check if key is in dict, if not set as 0
        sorted_stats["general"][stat_proper] = raw_stats.get(stat, 0)

    # For every stat in names
    for stat in smash_stat_names:

        # Check if key is in dict, if not set as 0
        sorted_stats["general"][stat] = raw_stats.get(stat, 0)

    # Setup class container
    sorted_stats.update({
        smash_class_proper: {"class_deaths": {}}
        for smash_class, smash_class_proper in smash_classes.items()
        })

    # For every class in smash classes
    for smash_class, smash_class_proper in smash_classes.items():

        # Add stats with default as 0
        sorted_stats[smash_class_proper]["overall"] = {
            smash_stat: raw_stats["class_stats"][smash_class].get(smash_stat, 0)
            for smash_stat in smash_class_stats
            }

        # Add proper class stats with default as 0
        sorted_stats[smash_class_proper]["overall"].update({
            smash_stat_proper: raw_stats["class_stats"][smash_class].get( smash_stat, 0)
            for smash_stat, smash_stat_proper in smash_class_stat_conversions.items()
            })

        # Add stats from general section with default as 0
        sorted_stats[smash_class_proper]["overall"].update({
            smash_stat_proper: int(raw_stats.get( (smash_stat + smash_class), 0))
            for smash_stat, smash_stat_proper in smash_class_stats_from_general.items()
            })

        # For every gamemode in gamemodes
        for gm, gm_proper in smash_gamemodes.items():

            # Add gamemode-specific stats with default as 0
            sorted_stats[smash_class_proper][gm_proper] = {
                smash_stat: raw_stats["class_stats"][smash_class].get( f"{smash_stat}_{gm}", 0)
                for smash_stat in smash_class_stats
                }

        # For every other class
        for c_smash_class, smash_class_abilities in smash_classes_abilities.items():

            sorted_stats[smash_class_proper]["class_deaths"][smash_classes[c_smash_class]] = 0

            for ability in smash_class_abilities:

                if(ability in raw_stats["class_stats"][c_smash_class]):
                    sorted_stats[smash_class_proper]["class_deaths"][smash_classes[c_smash_class]] += raw_stats["class_stats"][c_smash_class][ability].get( "smashed", 0)







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

# Players for testing
known_players = {"SmashHeroes": ( ("Hyplex", "bec9029b-efb3-4c85-925d-f2e97640cf92"), ("Anchor_Falls", "d0cdf17b-f8bd-4195-a8ab-c366bd5eb7c3"),
                                    ("Focus_Energy", "2de27887-dbb9-4154-8a36-029d6de5f468") ) }

player_to_test = ("SmashHeroes", 2)

# Player to test
NAME = known_players[player_to_test[0]][player_to_test[1]][0] # Hyplex
# UUID of player to test
UUID = known_players[player_to_test[0]][player_to_test[1]][1]# "bec9029b-efb3-4c85-925d-f2e97640cf92"

# URL for Hypixel player endpoint
URL = f"https://api.hypixel.net/player?key={API_KEY}&uuid={UUID}"

# List of gamemodes
hypixel_stats_gamemodes = {"SuperSmash": ("smash_heroes", getSmashHeroes)}

reformed_stats = getAllStats(URL)

pprint(reformed_stats)

print("Total stats parsed: ", get_total_keys(reformed_stats))
