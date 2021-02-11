import grequests
import json
from pprint import pprint
import time

auc_requirements = {"Baby_Yeti_pet": {"item_name": "] Baby Yeti", "tier": "LEGENDARY", "category": "misc", "price": 999999999},
                    "Bat_pet": {"item_name": "] Bat", "tier": "MYTHIC", "category": "misc", "price": 999999999},
                    "Bee_pet": {"item_name": "] Bee", "tier": "LEGENDARY", "category": "misc", "price": 999999999},
                    "Black_Cat_Pet": {"item_name": "] Black Cat", "tier": "LEGENDARY", "category": "misc", "price": 999999999},
                    "Blaze_Pet": {"item_name": "] Blaze", "tier": "LEGENDARY", "category": "misc", "price": 999999999},
                    "Blue_Whale_Pet": {"item_name": "] Blue Whale", "tier": "LEGENDARY", "category": "misc", "price": 999999999},
                    "Dolphin_Pet": {"item_name": "] Dolphin", "tier": "LEGENDARY", "category": "misc", "price": 999999999},
                    "Elephant_Pet": {"item_name": "] Elephant", "tier": "LEGENDARY", "category": "misc", "price": 999999999},
                    "Ender_Dragon_Pet": {"item_name": "] Ender Dragon", "tier": "LEGENDARY", "category": "misc", "price": 999999999},
                    "Enderman_Pet": {"item_name": "] Enderman", "tier": "LEGENDARY", "category": "misc", "price": 999999999},
                    "Endermite_Pet": {"item_name": "] Endermite", "tier": "LEGENDARY", "category": "misc", "price": 999999999},
                    "Flying_Fish_Pet": {"item_name": "] Flying Fish", "tier": "LEGENDARY", "category": "misc", "price": 999999999},
                    "Ghoul_Pet": {"item_name": "] Ghoul", "tier": "LEGENDARY", "category": "misc", "price": 999999999},
                    "Tiger_Pet": {"item_name": "] Tiger", "tier": "LEGENDARY", "category": "misc", "price": 999999999}
                    }

API_FILE = open("API_KEY.json", "r")
API_KEY = json.loads(API_FILE.read())["API_KEY"]

data = {}
auction_final = []
auction_final_cheapest = {}
auction_final_cheapest_sorted = []

start_time = time.time()

url_base = f"https://api.hypixel.net/skyblock/auctions?key={API_KEY}"

def checkAuctionItem(auction_item):

    # Check if item is BIN
    if("bin" not in auction_item):
        return (False, "Not BIN")

    # Check if item is already claimed
    if(auction_item["claimed"] == True):
        return (False, "Already claimed")

    # For unique obj ruleset
    for id in auc_requirements:

        # Start as valid item
        valid = True

        # For every rule in obj ruleset
        for req in auc_requirements[id]:

            # Make sure rule isn't price
            if(req != "price"):

                # Make sure it follows the rule
                if(auc_requirements[id][req] not in auction_item[req]):

                    # No longer valid
                    valid = False
                    break

        # Found a potential match with a filter!
        if(valid):

            # Found a  match with a filter AND price! (Success)
            if(auction_item["starting_bid"] < auc_requirements[id]["price"]):
                dashed_uuid = auction_item['uuid'][:8] + '-' + auction_item['uuid'][8:12] + '-' + auction_item['uuid'][12:16]
                dashed_uuid += '-' + auction_item['uuid'][16:20] + '-' + auction_item['uuid'][20:]
                return (True, (id, f"/viewauction {dashed_uuid}", auction_item['starting_bid'], auction_item["item_name"]))


    # Broke on one of the requirements
    return (False, "Not all requirements met")


# Async to first page
resp = grequests.get(url_base)

# Get page 0 (and pages count)
for res in grequests.map([resp]):
    data = json.loads(res.content)
    total_pages = data['totalPages']
    print(f"Total Pages found: {data['totalPages']}")

    # Verify success
    if(data["success"]):
        # Get items from page 0
        for auction_item in data["auctions"]:
            try:
                item_ans = checkAuctionItem(auction_item)
                # Passed filter
                if(item_ans[0]):
                    auction_final.append(item_ans[1])
                # Failed filter
                else:
                    pass
            except:
                pprint(data)

    # Unsuccessful GET request
    else:
        print(f"Failed GET request: {data['cause']}")


first_page_time = time.time()

# Get all page urls
urls = []
for page_count in range(1, total_pages+1):
    urls.append(f"{url_base}&page={page_count}")

# Async to remaining pages
resp = (grequests.get(url) for url in urls)

made_requests_time = time.time()

# Get items from remaining pages
for res in grequests.map(resp):
    data = json.loads(res.content)

    # Verify success
    if(data["success"]):
        # Get items from pages 1 -> n
        for auction_item in data["auctions"]:
            try:
                item_ans = checkAuctionItem(auction_item)
                # Passed filter
                if(item_ans[0]):
                    auction_final.append(item_ans[1])
                # Failed filter
                else:
                    pass
            except:
                pprint(data)

    # Unsuccessful GET request
    else:
        print(f"Failed GET request: {data['cause']}")

# Debug for amount of items found
print(f"{len(auction_final)} items found")

# Sort out the results
auction_final = sorted(auction_final, key=lambda x: (x[0], x[2]))

# Get only the cheapest of every time
for auc in auction_final:

    # If not in new dict yet
    if(auc[0] not in auction_final_cheapest):
        auction_final_cheapest[auc[0]] = auc

    # If already in new dict, compare against previous
    else:
        if(auc[2] < auction_final_cheapest[auc[0]][2]):
            auction_final_cheapest[auc[0]] = auc

# Add all items from cheapest to cheapest_sorted
for auc in auction_final_cheapest:
    auction_final_cheapest_sorted.append(auction_final_cheapest[auc])

# Sort cheapest_sorted
auction_final_cheapest_sorted = sorted(auction_final_cheapest_sorted, key=lambda x: x[2])


pprint(auction_final_cheapest_sorted)

end_time = time.time()

print(f"Time Taken: {end_time-start_time}\n\tFirst Page: {first_page_time-start_time}\n\tFinished Requests: {made_requests_time-start_time}")
