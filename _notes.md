## Datamining

- collaborative filtering

The goal is to recommend you the buyer an item to purchase. You want to buy a book. The system looks for other customers that are similar to you and shows you what they have purchased.

- How does the system find someone similar?

If you previously bought ANYTHING ELSE from the system, and RATED it, the system will search all other customers who rated the item you bought, and pull up any books they bought.

It will compute the Manhattan distance of your previous rating to all other customers who rated that object, and find the one closest to you.

Those customers book purchases that are rated highly will now be recommended to you.

    # MANHATTAN DISTANCE
    your.x = your.purchases[0].rating or 0
    your.y = your.purchases[1].rating or 0
    manhattan_distance = (your.x - other.x) + (your.y - other.y)

    # EUCLIDEAN DISTANCE - pythagorean theorem - straight line distance
    e_distance = math.sqrt((your.x - other.x) ** 2 + (your.y - other.y) ** 2)


The Minkowski algorithm simplifies the definition of the functions for Manhattan and Euclidean distance, by adding an argument 'r'. If 'r'=1, then the result will be the Manhattan formula, and if 'r'=2, the Euclidean formula.

    def minkowski(rating1, rating2, r):
        """ Computes the Minkowski Distance. 
        Both rating1 and rating2 are dicts of the form
        {"Item Name": rating, "Item Name": rating}
        """
        distance = 0
        for key in rating1:
            if key not in rating2:
                continue
            else:
                distance += pow(abs(rating1[key] - rating2[key]), r)
        # was there a common rating?
        if distance != 0:
            return pow(distance, 1/r)
        else:
            return distance

- Pearson Correlation Coefficient

Bob has a pattern of rating anything 1 if he dislikes, and 4 if he likes. Period.

Sue has as pattern of rating things anywhere between 2 and 4.

Does Bob's 4 == Sue's 4 ?

    bobs_max = max([r for r in bob.ratings])
    for key in bob.ratings:
        bob.ratings[key]["coeff"] = bobs_max - bob.ratings[key]
    
    sues_max = max([r for r in sue.ratings])
    for key in sue.ratings:
        sue.ratings[key]["coeff"] = sues_max - sue.ratings[key]

    agreements = []
    for key in bob.ratings:
        if key not in sue.ratings:
            continue
        else:
            if bob.ratings[key]["coeff"] == sue.ratings[key]["coeff"]:
                # we have a winner!
                agreements.append()

