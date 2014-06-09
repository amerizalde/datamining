## Datamining

- collaborative filtering

The goal is to recommend you the buyer an item to purchase. You want to buy a book. The system looks for other customers that are similar to you and shows you what they have purchased.

- How does the system find someone similar?

If you previously bought ANYTHING ELSE from the system, and RATED it, the system will search all other customers who rated the item you bought, and pull up any books they bought.

It will compute the Manhattan distance of your previous rating to all other customers who rated that object, and find the one closest to you.

Those customers book purchases will now be recommended to you.

    # MANHATTAN DISTANCE
    your.x = your.purchases[0].rating or 0
    your.y = your.purchases[1].rating or 0
    manhattan_distance = (your.x - other.x) + (your.y - other.y)

    # EUCLIDEAN DISTANCE - pythagorean theorem - straight line distance
    e_distance = math.sqrt((your.x - other.x) ** 2 + (your.y - other.y) ** 2)

