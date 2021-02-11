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
            for ach, achievement in data["achievements"][gm]["one_time"].items():

                # Filter for adding played unlocked percentages
                game_percent_unlocked = achievement.get("gamePercentUnlocked", 101)
                global_percent_unlocked = achievement.get("globalPercentUnlocked", 101)

                # Temporary achievement object
                current_ach = (gm, achievement["name"], achievement["description"], game_percent_unlocked, global_percent_unlocked)

                # Add achievement to achievements list container
                ach_list.append(current_ach)

# Sort by "played" (local) percentage:
ach_list.sort(key=lambda tup: tup[3])

# Feedback
print("Top 5 rarest achievements (local):")

# Show top 5
for i in range(5):
    print(ach_list[i])

# Feedback
print("Top 5 rarest achievements (global):")

# Sort by global percentage
ach_list.sort(key=lambda tup: tup[4])

# Show top 5
for i in range(5):
    print(ach_list[i])
