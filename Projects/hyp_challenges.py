# This is a script for parsing challenge data from the Hypixel API resources/challenges endpoint.

import grequests
import json

# Url for getting achievements from resources endpoint
url = "https://api.hypixel.net/resources/challenges"

# Setup bin for our achievements
challenge_list = []
possible_rewards = []

# Async call to url
resp = grequests.get(url)

# For every response
for data in grequests.map([resp]):

    # Load data with JSON
    data = json.loads(data.content)

    # If response successful
    if(data["success"]):

        # For every gamemode
        for gm in data["challenges"]:

            # For every quest in that gamemode
            for challenge in data["challenges"][gm]:

                # Add challenge to challenges list container
                challenge_list.append((challenge["name"]))

                # For every reward from this quest
                for reward in challenge["rewards"]:

                    # Add unique types to possible_rewards container
                    if(reward["type"] not in possible_rewards):
                        possible_rewards.append(reward["type"])

# Show all possible rewards from a challlenge
print(possible_rewards)

# Show all challenges
print(challenge_list)
