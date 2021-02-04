# This is a script for parsing achievement data from the Hypixel API resources/achievements endpoint.

import grequests
import json

# Url for getting achievements from resources endpoint
url = "https://api.hypixel.net/resources/achievements"

# Setup bin for our achievements
ach_list = []

# Async call to url
resp = grequests.get(url)

# For every response
for data in grequests.map([resp]):

    # Load data with JSON
    data = json.loads(data.content)

    # If response successful
    if(data["success"]):

        # For every gamemode
        for gm in data["achievements"]:

            # For every one-time achievement in that gamemode
            for ach in data["achievements"][gm]["one_time"]:

                # Temporary Achievement link to simplify
                achievement = data["achievements"][gm]["one_time"][ach]

                # Filter for adding played unlocked percentages
                if("gamePercentUnlocked" in achievement):
                    game_percent_unlocked = achievement["gamePercentUnlocked"]
                else:
                    game_percent_unlocked = 101

                if("globalPercentUnlocked" in achievement):
                    global_percent_unlocked = achievement["globalPercentUnlocked"]
                else:
                    global_percent_unlocked = 101

                # Temporary achievement object
                current_ach = (gm, achievement["name"], achievement["description"], global_percent_unlocked, game_percent_unlocked)

                # Add achievement to achievements list container
                ach_list.append(current_ach)

# Sort by "played" (local) percentage:
ach_list.sort(key=lambda tup: tup[3])

# Show top 5
for i in range(5):
    print(ach_list[i])

# Sort by global percentage
ach_list.sort(key=lambda tup: tup[4])

# Show top 5
for i in range(5):
    print(ach_list[i])
