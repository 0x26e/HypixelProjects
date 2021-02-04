# This is a script for parsing quest data from the Hypixel API resources/quests endpoint.

import grequests
import json

# Url for getting achievements from resources endpoint
url = "https://api.hypixel.net/resources/quests"

# Setup bin for our achievements
quest_list = []
possible_rewards = []
possible_objectives = []

# Async call to url
resp = grequests.get(url)

# For every response
for data in grequests.map([resp]):

    # Load data with JSON
    data = json.loads(data.content)

    # If response successful
    if(data["success"]):

        # For every gamemode
        for gm in data["quests"]:

            # For every quest in that gamemode
            for quest in data["quests"][gm]:

                # Add quest to quests list container
                quest_list.append((gm, quest["name"], quest["description"]))

                # For every reward from this quest
                for reward in quest["rewards"]:

                    # Add unique types to possible_rewards container
                    if(reward["type"] not in possible_rewards):
                        possible_rewards.append(reward["type"])

                # For every reward from this quest
                for obj in quest["objectives"]:

                    # Add unique types to possible_rewards container
                    if(obj["type"] not in possible_objectives):
                        possible_objectives.append(obj["type"])

# Show all possible rewards from a quest
print(possible_rewards)

# Show all possible objectives for a quest
print(possible_objectives)











#
