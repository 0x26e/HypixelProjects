import json
import grequests
from pprint import pprint
import sys


# Get number of stats from nested dict/lists
def get_total_keys(data):

    if not isinstance(data, dict):
        return 0

    nested_keys = sum(get_total_keys(value) for key, value in data.items())
    return len(data) + nested_keys

# Get number of bytes from nested dict/lists
def get_total_bytes(data):

    if not isinstance(data, dict):
        return sys.getsizeof(data)

    nested_bytes = sum(get_total_keys(value) for key, value in data.items())
    return sys.getsizeof(data) + nested_bytes


# ! # Add stats from achievements
# Returns formatted Smash Heroes Stats
def getSmashHeroes(raw_stats, achievements):

    # Setup better naming
    CLASS_STATS = raw_stats.get("class_stats", {})

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
            smash_stat: CLASS_STATS[smash_class].get(smash_stat, 0)
            for smash_stat in smash_class_stats
            }

        # Add proper class stats with default as 0
        sorted_stats[smash_class_proper]["overall"].update({
            smash_stat_proper: CLASS_STATS[smash_class].get( smash_stat, 0)
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
                smash_stat: CLASS_STATS[smash_class].get( f"{smash_stat}_{gm}", 0)
                for smash_stat in smash_class_stats
            }

        """
        class_deaths = {
            class_1: total_deaths_to_class_1,
            class_2: total_deaths_to_class_2,
            ...,
            class_n: total_deaths_to_class_n,
        }
        """
        def get_total_deaths_by_class(class_stats, killer_class):
            """
            class_stats: stats of the class which we want the total deaths of
            killer_class: the class that killed the class of `class_stats`
            """
            return sum(
                class_stats.get(ability, {}).get("smashed", 0)
                for ability in smash_classes_abilities.get(killer_class, {})
            )

        for c_smash_class, smash_class_proper in smash_classes.items():
            class_stats = CLASS_STATS[c_smash_class]

            sorted_stats[smash_class_proper]["class_deaths"] = {
                killer_class: get_total_deaths_by_class(class_stats, killer_class)
                for killer_class in smash_classes
            }

    # Return cleaned up stats
    return sorted_stats


# ! # Known bugs: Losses need to be fixed
# ! # Add stats from achievements
# Returns formatted Bedwars stats
def getBedwars(raw_stats, achievements):

    # Setup container to hold stats
    sorted_stats = {"general": {}, "cosmetic_boxes": {}}

    # List of active stats
    bedwars_active_stats = {"activeProjectileTrail": "projectile_trail", "spray_storage_new": "sprays", "activeIslandTopper": "island_topper",
        "activeDeathCry": "death_cry", "activeNPCSkin": "npc_skin", "glyph_storage_new": "glyphs", "activeKillMessages": "kill_messages",
        "activeKillEffect": "kill_effect", "activeVictoryDance": "victory_dance", "selected_ultimate": "ultimate"
        }

    # List of gamemodes
    bedwars_gamemodes = {"eight_one": "one", "eight_two": "two", "four_three": "three", "four_four": "four", "castle": "castle",
        "eight_one_ultimate": "one_ultimate", "eight_two_ultimate": "two_ultimate", "four_four_ultimate": "four_ultimate",
        "eight_one_rush": "one_rush", "four_four_rush": "four_rush",
        "eight_two_voidless": "two_voidless", "four_four_voidless": "four_voidless",
        "eight_two_lucky": "two_lucky", "four_four_lucky": "four_lucky"
        }

    # Setup proper name conversions
    bedwars_stat_name_conversions = {"winstreak": "winstreak", "losses": "losses", "wins_bedwars": "wins", "games_played_bedwars": "games_played",
        "beds_lost_bedwars": "beds_lost", "beds_broken_bedwars": "beds_broken", "permanent _items_purchased_bedwars": "permament_items_purchased",
        "kills": {
            "kills": "total",
            "projectile_kills_bedwars": "projectile",
            "void_kills_bedwars": "void",
            "fall_kills_bedwars": "fall_damage",
            "entity_explosion_kills_bedwars": "explosion",
            "entity_attacK_kills_bedwars": "mob"},
        "final_kills": {
            "final_kills_bedwars": "total",
            "projectile_final_kills_bedwars": "projectile",
            "void_final_kills_bedwars": "void",
            "fall_final_kills_bedwars": "fall_damage",
            "entity_explosion_final_kills_bedwars": "explosion",
            "entity_attacK_final_kills_bedwars": "mob"},
        "deaths": {
            "deaths_bedwars": "total",
            "projectile_deaths_bedwars": "projectile",
            "void_deaths_bedwars": "void",
            "fall_deaths_bedwars": "fall_damage",
            "suffocation_deaths_bedwars": "suffocation",
            "entity_explosion_deaths_bedwars": "explosion",
            "entity_attacK_deaths_bedwars": "mob"},
        "final_deaths": {
            "final_deaths_bedwars": "total",
            "projectile_final_deaths_bedwars": "projectile",
            "void_final_deaths_bedwars": "void",
            "fall_final_deaths_bedwars": "fall_damage",
            "suffocation_deaths_bedwars": "suffocation",
            "entity_explosion_final_deaths_bedwars": "explosion",
            "entity_attack_final_deaths_bedwars": "mob"},
        "resources": {
            "resources_collected_bedwars": "total",
            "iron_resources_collected_bedwars": "iron",
            "gold_resources_collected_bedwars": "gold",
            "diamond_resources_collected_bedwars": "diamond",
            "emerald_resources_collected_bedwars": "emerald"}
        }
    # ! # games_played_bedwars_1, items_purchased_bedwars, _items_purchased_bedwars
    # ! # Kills: custom_kills_bedwars, fire_tick_kills_bedwars, contact_kills_bedwars, fire_kills_bedwars
    # ! # Final Kills: custom_final_kills_bedwars, fire_tick_final_kills_bedwars, contact_final_kills_bedwars, fire_final_kills_bedwars
    # ! # Deaths: custom_deaths_bedwars, fire_tick_deaths_bedwars, fire_deaths_bedwars
    # ! # Final Deaths: custom_deaths_bedwars, fire_tick_deaths_bedwars, fire_deaths_bedwars

    # Setup stat names
    bedwars_stat_names = {"coins": "coins", "Experience": "experience"}

    # Setup cosmetic stat names
    bedwars_cosmetic_stat_names = {"bedwars_box": "unopened", "bedwars_halloween_boxes": "halloween_opened",
        "bedwars_easter_boxes": "easter_opened", "bedwars_christmas_boxes": "christmas_opened", "bedwars_lunar_boxes": "lunar_opened",
        "bedwars_box_commons": "common", "bedwars_box_rares": "rare", "bedwars_box_epics": "epic", "bedwars_box_legendaries": "legendary"}
    # ! # bedwars_boxes (is it including unopened or not)
    # ! # Bedwars_openedChests, Bedwars_openedCommons, Bedwars_openedRares, Bedwars_openedLegendaries, spooky_open_ach

    # Cosmetic box stats
    sorted_stats["cosmetic_boxes"] = {
        cm_stat_proper: raw_stats.get(cm_stat, 0)
        for cm_stat, cm_stat_proper in bedwars_cosmetic_stat_names.items()
        }

    # Start general stats
    sorted_stats["general"] = {
        bw_stat_proper: raw_stats.get(bw_stat, 0)
        for bw_stat, bw_stat_proper in bedwars_stat_names.items()
        }

    # Finish general stats
    for bw_stat, bw_stat_proper in bedwars_stat_name_conversions.items():

        # Check if subsection of stats
        if( isinstance(bw_stat_proper, dict) ):
            sorted_stats["general"][bw_stat] = {
                sub_bw_stat_proper: raw_stats.get(sub_bw_stat, 0)
                for sub_bw_stat, sub_bw_stat_proper in bw_stat_proper.items()
                }

        # If individual stat
        else:
            sorted_stats["general"][bw_stat_proper] = raw_stats.get(bw_stat, 0)

    # Gamemode stats
    for gm, gm_proper in bedwars_gamemodes.items():

        # Initialize container for gamemode-specific stats
        sorted_stats[gm_proper] = {}

        # For every stat that can be gamemode-specific
        for bw_stat, bw_stat_proper in bedwars_stat_name_conversions.items():

            # If individual stat
            if(not isinstance(bw_stat_proper, dict)):

                # Get the stat, default to 0
                sorted_stats[gm_proper][bw_stat_proper] = raw_stats.get(f"{gm}_{bw_stat}", 0)

            # If substats
            else:

                # Create subdict of stats
                sorted_stats[gm_proper][bw_stat] = {
                sub_bw_stat_proper: raw_stats.get(f"{gm}_{sub_bw_stat}", 0)
                for sub_bw_stat, sub_bw_stat_proper in bw_stat_proper.items()
                }

    # Active stats
    sorted_stats["active"] = {
        a_stat_proper: raw_stats.get(a_stat, "")
        for a_stat, a_stat_proper in bedwars_active_stats.items()
        }



    # Return cleaned up stats
    return sorted_stats


# Returns formatted Quake stats
# ! # Add shop stats
def getQuake(raw_stats, achievements):

    # Setup container to hold stats
    sorted_stats = {}

    # List of active stats
    quake_active_stats = {"barrel": "barrel", "case": "case", "killsound": "killsound", "sight": "laser",
        "muzzle": "muzzle", "beam": "beam", "selectedKillPrefix": "prefix_color", "trigger": "trigger"
        }

    # List of gamemodes
    quake_gamemodes = {"_teams": "teams", "_solo_tourney": "tournament", "": "solo"}

    # Setup general stat names
    quake_stat_names = (
        "coins", "highest_killstreak", "dash_cooldown", "dash_power", "weekly_kills_a", "weekly_kills_b", "monthly_kills_a", "monthly_kills_b"
        )

    # Setup mode stats
    quake_mode_stats = ("kills", "deaths", "killstreaks", "wins", "headshots", "distance_travelled", "shots_fired")

    # Set general stats
    sorted_stats["general"] = {
        q_stat: int(raw_stats.get(q_stat, 0))
        for q_stat in quake_stat_names
        }

    # Set gamemode stats
    for gm, gm_proper in quake_gamemodes.items():
        sorted_stats[gm_proper] = {
            q_stat: raw_stats.get(f"{q_stat}{gm}", 0)
            for q_stat in quake_mode_stats
            }

    # Set active stats
    sorted_stats["active"] = {
        q_stat_proper: raw_stats.get(q_stat, 0)
        for q_stat, q_stat_proper in quake_active_stats.items()
        }

    # Set general stats
    sorted_stats["general"].update({
        q_stat: sum( [ sorted_stats["solo"].get(q_stat, 0), sorted_stats["teams"].get(q_stat, 0), sorted_stats["tournament"].get(q_stat, 0) ] )
        for q_stat in quake_mode_stats
        })

    # Fix post_update stats
    sorted_stats["solo"]["post_update_kills"] = raw_stats.get("kills_since_update_feb_2017", 0)
    sorted_stats["teams"]["post_update_kills"] = raw_stats.get("kills_since_update_feb_2017_teams", 0)

    # Fix dash cooldown and power
    sorted_stats["general"]["dash_cooldown"] += 1
    sorted_stats["general"]["dash_power"] += 1

    # Add stats from tiered achievements
    sorted_stats["general"]["godlikes"] = achievements.get("quake_godlikes", 0)
    sorted_stats["general"]["weapons"] = achievements.get("quake_weapon_arsenal", 0)

    # Setup for armor
    quake_hats = (
        ("exodiahat", 200000, "None"), ("discohat", 75000, "None"), ("radianthat", 50000, "None"), ("bouncyhat", 25000, "None"),
        ("crafterhat", 15000, "None"), ("explosivehat", 5000, "None"), ("librarianhat", 2500, "None"), ("hypixelhat", 2000, "None"),
        ("bobhat", 1500, "None"), ("ecologyhat", 1000, "None"), ("lighthat", 1000, "None"), ("engineeringhat", 1000, "None"),
        ("richyrichhat", 1000, "None"), ("jeeperscreepershat", 900, "None"), ("walkingdeadhat", 900, "None"), ("controlfreakhat", 850, "None"),
        ("cavemanhat", 850, "None"), ("hipsterhat", 850, "None"), ("majestichat", 700, "None"), ("tnt", 700, "None"), ("dispenser", 700, "None"),
        ("diamond", 700, "None"), ("redstone", 700, "None"), ("lantern", 700, "None"), ("spaceman", 700, "None"), ("melon", 350, "None"),
        ("cactus", 350, "None"), ("showoff", 0, "None")
        )
    quake_chestplates = (
        ("exodiakit", 200000, "None"), ("discokit", 75000, "None"), ("swegkit", 4500, "None"), ("budderkit", 3375, "None"), ("medievalkit", 2750, "None"),
        ("fashionistakit", 2250, "None"), ("snowkit", 2250, "None"), ("slimekit", 2250, "None"), ("spacekit", 2250, "None"), ("revengekit", 2250, "None"),
        ("invaderkit", 2250, "None"), ("specopskit", 2250, "None"), ("swatkit", 2250, "None"), ("marinekit", 2250, "None"), ("commander", 2250, "None"),
        ("majestic", 2250, "None"), ("elite", 2250, "None"), ("soldier", 650, "None")
        )
    quake_lowers = (
        ("exodia", 200000, "None"), ("disco", 75000, "None"), ("swegkit", 4500, "None"), ("budderkit", 3375, "None"), ("medievalkit", 2750, "None"),
        ("fashionistakit", 2250, "None"), ("snowkit", 2250, "None"), ("slimekit", 2250, "None"), ("spacekit", 2250, "None"), ("revengekit", 2250, "None"),
        ("invaderkit", 2250, "None"), ("specopskit", 2250, "None"), ("swatkit", 2250, "None"), ("marinekit", 2250, "None"), ("commander", 2250, "None"),
        ("majestic", 2250, "None"), ("elite", 2250, "None"), ("soldier", 650, "None")
        )

    # Resolve for best hat
    best_quake_hat = raw_stats.get("hat", False)
    if(not best_quake_hat):
        for q_hat in quake_hats:
            if(q_hat[0] in raw_stats["packages"]):
                best_quake_hat = q_hat[0]
                break

    if(not best_quake_hat):
        best_quake_hat = "NONE"

    # Resolve for best chestplate
    best_quake_chestplate = raw_stats.get("armor", False)
    if(not best_quake_chestplate):
        for q_chest in quake_chestplates:
            if(q_chest[0] in raw_stats["packages"]):
                best_quake_chestplate = q_chest[0]
                break

    if(not best_quake_chestplate):
        best_quake_chestplate = "NONE"

    # Resolve for best leggings
    best_quake_leggings = raw_stats.get("leggings", False)
    if(not best_quake_leggings):
        for q_lower in quake_lowers:
            if(f"{q_lower[0]}_leggings" in raw_stats["packages"]):
                best_quake_leggings = f"{q_lower[0]}_leggings"
                break

    if(not best_quake_leggings):
        best_quake_leggings = "NONE"

    # Resolve for best boots
    best_quake_boots = raw_stats.get("boots", False)
    if(not best_quake_boots):
        for q_lower in quake_lowers:
            if(f"{q_lower[0]}_boots" in raw_stats["packages"]):
                best_quake_boots = f"{q_lower[0]}_boots"
                break

    if(not best_quake_boots):
        best_quake_boots = "NONE"

    # Get best armor set
    sorted_stats["active"]["armor"] = {
        "hat": best_quake_hat,
        "chestplate": best_quake_chestplate,
        "leggings": best_quake_leggings,
        "boots": best_quake_boots,
        }

    # Setup for weapon
    quake_weapons = {
        "basic_railgun": ("WOOD_HOE", "YELLOW", "SMALL_BALL", "NONE", "ONE_POINT_FIVE"),
        "superior_railgun": ("IRON_HOE", "RED", "BURST", "NONE", "ONE_POINT_FOUR"),
        "hyper_beam_railgun": ("GOLD_HOE", "YELLOW", "STAR", "NONE", "ONE_POINT_THREE"),
        "creeper_railgun": ("DIAMOND_HOE", "GREEN", "CREEPER", "NONE", "ONE_POINT_TWO"),
        "bfg": ("SHINY_STONE_HOE", "BLUE", "LARGE_BALL", "NONE", "ONE_POINT_ONE"),
        "budder_slapper": ("SHINY_GOLD_HOE", "YELLOW", "SMALL_BALL", "GOLD", "ONE_POINT_FIVE"),
        "redstoner": ("SHINY_WOOD_HOE", "RED", "BURST", "REDSTONE", "ONE_POINT_TWO"),
        "bling_bling_thing": ("SHINY_DIAMOND_HOE", "PURPLE", "LARGE_BALL", "DIAMOND", "ONE_POINT_ZERO"),
        "the_turtle": ("IRON_HOE", "GREEN", "LARGE_BALL", "IRON", "TWO_POINT_FIVE"),
        "lovegun": ("SHINY_GOLD_HOE", "RED", "STAR", "REDSTONE", "NINE_POINT_THREE"),
        "the_harvester": ("STONE_HOE", "GREEN", "SMALL_BALL", "MELON", "ONE_POINT_FIVE"),
        "blue_lagoon": ("DIAMOND_HOE", "BLUE", "BURST", "PRISMARINE", "ONE_POINT_ONE"),
        "cookie_cannon": ("GOLD_HOE", "EMERALD", "BURST", "COMMAND_BLOCK", "ONE_POINT_ONE"),
        "the_worm": ("STONE_HOE", "GREEN", "SMALL_BALL", "NONE", "FIVE_POINT_ZERO"),
        "the_snail": ("STONE_HOE", "RED", "CREEPER", "WOOD", "NINE_POINT_ZERO"),
        "le_bizarre": ("SHINY_DIAMOND_HOE", "ORANGE", "SMALL_BALL", "LAPIS", "ONE_POINT_FOUR"),
        "fabled_railgun": ("SHINY_DIAMOND_HOE", "DIAMOND", "STAR", "PRISMARINE", "ONE_POINT_TWO"),
        "apple_corer": ("SHINY_IRON_HOE", "GOLD", "STAR", "OBSIDIAN", "ZERO_POINT_NINE"),
        "railgun_of_darkness": ("SHINY_GOLD_HOE", "BLACK", "LARGE_BALL", "OBSIDIAN", "ZERO_POINT_NINE"),
        "platinum_smelter": ("SHINY_IRON_HOE", "SILVER", "BURST", "IRON", "ZERO_POINT_EIGHT_FIVE"),
        "the_reaper": ("SHINY_DIAMOND_HOE", "BLACK", "LARGE_BALL", "SOUL_SAND", "ZERO_POINT_EIGHT_FIVE")
        }

    # Setup case prefixes
    quake_case_prefixes = {
        "WOOD_HOE": "Slightly",
        "STONE_HOE": "Mostly",
        "SHINY_WOOD_HOE": "Spectacularly",
        "SHINY_STONE_HOE": "Brilliant",
        "IRON_HOE": "Excellently",
        "GOLD_HOE": "Awesomely",
        "DIAMOND_HOE": "Undeniably",
        "SHINY_GOLD_HOE": "Luxury",
        "SHINY_DIAMOND_HOE": "Lucky",
        "SHINY_IRON_HOE": "Executive"
        }

    # Setup laser prefixes
    quake_laser_prefixes = {
        "YELLOW": "Shining",
        "GREEN": "Glowing",
        "WHITE": "Lofty",
        "RED": "Radiant",
        "BLUE": "Resplendant",
        "PURPLE": "Majestic",
        "PINK": "Stunning",
        "GOLD": "Grandiose",
        "EMERALD": "Dignified",
        "DIAMOND": "Royal",
        "GRAY": "Pearly",
        "ORANGE": "Not-a-fruit",
        "SILVER": "Lustrous",
        "BLACK": "Absorbing"
        }

    # Setup muzzle suffixes
    quake_muzzle_suffixes = {
        "NONE": "AK",
        "CLAY": "CL",
        "WOOD": "WO",
        "GOLD": "GD",
        "REDSTONE": "RED",
        "IRON": "IN",
        "ENDER_STONE": "EST",
        "DIAMOND": "DMD",
        "QUARTZ": "QA",
        "EMERALD": "EM",
        "LAPIS": "LA",
        "OBSIDIAN": "BBY",
        "SPONGE": "HYPE",
        "SEA_LANTERN": "SL",
        "COMMAND_BLOCK": "CMD",
        "PRISMARINE": "PRM",
        "MELON": "MEL",
        "PUMPKIN": "PMK",
        "SOUL_SAND": "SMS"
        }

    # Setup trigger suffixes
    quake_trigger_suffixes = {
        "ONE_POINT_FIVE": "1.0",
        "NINE_POINT_ZERO": "WTF",
        "FIVE_POINT_ZERO": "5.0",
        "TWO_POINT_FIVE": "2.5",
        "ONE_POINT_FOUR": "2.0",
        "ONE_POINT_THREE": "3.0",
        "ONE_POINT_TWO": "1337",
        "ONE_POINT_ONE": "2013",
        "ONE_POINT_ZERO": "99",
        "ZERO_POINT_NINE": "-1",
        "ZERO_POINT_EIGHT_FIVE": "404"
        }

    # Setup barrel suffixes
    quake_barrel_suffixes = {
        "SMALL_BALL": "(S)",
        "LARGE_BALL": "(L)",
        "CREEPER": "(C)",
        "BURST": "(B)",
        "STAR": "(*)"
        }

    # Current weapon build
    quake_current_weapon_parts = (
        sorted_stats["active"]["case"],
        sorted_stats["active"]["laser"],
        sorted_stats["active"]["barrel"],
        sorted_stats["active"]["muzzle"],
        sorted_stats["active"]["trigger"]
        )

    # Get current weapon name
    for q_weapon, q_weapon_parts in quake_weapons.items():
        if(quake_current_weapon_parts == q_weapon_parts):
            sorted_stats["active"]["weapon"] = q_weapon

    if("weapon" not in sorted_stats["active"]):
        q_weapon_name = ""
        q_weapon_name += quake_case_prefixes[sorted_stats["active"].get("case", "WOOD_HOE")] + " "
        q_weapon_name += quake_laser_prefixes[sorted_stats["active"].get("laser", "YELLOW")] + " Railgun "
        q_weapon_name += quake_muzzle_suffixes[sorted_stats["active"].get("muzzle", "NONE")]
        q_weapon_name += quake_trigger_suffixes[sorted_stats["active"].get("trigger", "ONE_POINT_THREE")]
        q_weapon_name += quake_barrel_suffixes[sorted_stats["active"].get("barrel", "SMALL_BALL")]
        sorted_stats["active"]["weapon"] = q_weapon_name

    # # Resolve for max shop (and rank)

    # Setup for cosmetics purchased
    total_items_purchased = {"None": 0, "VIP": 0, "VIP+": 0, "MVP": 0, "MVP+": 0}

    # Add hats to cosmetic totals
    for q_hat in quake_hats:
        if(q_hat[0] in raw_stats["packages"]):
            total_items_purchased[q_hat[2]] += 1

    # Total coins spent on chestplates
    for q_hat in quake_hats:
        if(q_hat[0] in raw_stats["packages"]):
            total_items_purchased[q_hat[2]] += 1

    sorted_stats["items_purchased"] = total_items_purchased

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

# List of gamemodes
hypixel_stats_gamemodes = {
    "SuperSmash": ("smash_heroes", getSmashHeroes),
    # "Bedwars": ("bedwars", getBedwars),
    # "Quake": ("quake", getQuake),
    }

reformed_stats = getAllStats(URL)

pprint(reformed_stats)

print("Total stats parsed: ", get_total_keys(reformed_stats))

print("Total bytes stored: ", get_total_bytes(reformed_stats))
