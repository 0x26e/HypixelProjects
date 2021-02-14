# SMASH
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

# QUAKE

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
# Setup for cosmetics purchased
quake_total_items_purchased = {"None": 0, "VIP": 0, "VIP+": 0, "MVP": 0, "MVP+": 0}

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

# BEDWARS

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
