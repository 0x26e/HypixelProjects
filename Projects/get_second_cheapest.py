# Setup auction items
auction_items = [("item1", 6000), ("item2", 1500), ("item3", 3000), ("item4", 9000), ("item5", 4500), ("item6", 7500)]

# Set bin for cheapest
cheapest = auction_items[0]
cheapest_2 = auction_items[0]

# Loop through auction items
for auc in auction_items:

    # If new cheapest, replace
    if(auc[1] < cheapest[1]):
        cheapest = auc
    # If new 2nd cheapest, replace
    elif(auc[1] < cheapest_2[1]):
        cheapest_2 = auc

# Feedback log
print(cheapest, cheapest_2)
