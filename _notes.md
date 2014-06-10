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

#### Minkowski Algorithm

The Minkowski algorithm simplifies the definition of the functions for Manhattan and Euclidean distance, by adding an argument 'r'. If 'r'=1, then the result will be the Manhattan formula, and if 'r'=2, the Euclidean formula.

    def minkowski(rating1, rating2, r):
        """ Computes the Minkowski Distance. 
        Both rating1 and rating2 are dicts of the form
        {"Item Name": {"rating": rating, "coeff": coeff}}
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

#### Pearson Correlation Coefficient

Bob has a pattern of rating anything 1 if he dislikes, and 4 if he likes. Period.

Sue has as pattern of rating things anywhere between 2 and 4.

How does Bob's 4 evaluate to Sue's 4 ?

    def pearson(a, b):
        matches = 0
        summ_ab = 0
        summ_a = 0
        summ_b = 0
        summ_a2 = 0
        summ_b2 = 0
        for key in a.rating:
            if key in b.rating:
                matches += 1
                x = a.rating[key]
                y = b.rating[key]
                # x * y for [x] for [y]
                summ_ab += x * y
                # sum[x]
                summ_a += x
                # sum[y]
                summ_b += y
                # x ** 2 for [x]
                summ_a2 += x ** 2
                # y ** 2 for [y]
                summ_b2 += y ** 2
        
        denominator = math.sqrt(
            summ_a2 - (summ_a ** 2) / matches) * math.sqrt(
            summ_b2 - (summ_b ** 2) / matches)
        if denominator == 0:
            return denominator
        else:
            return (summ_ab - (summ_a * summ_b) / matches) / denominator

#### Cosine Similarity

When comparing data sets of sparse data, handling all the shared zeros becomes an issue. An example would be when recommending books; you have two books written in English, and are trying to compute similarity by the words used in the texts. Most of the matches will be of articles (the, a, are, etc.) and of no use, and the words you consider important matches would be sparse if existant at all. Cosine similarity ignores those 0 to 0 matches.

    def similarity(a, b):
        """ cosine similarity
    
        range from 1(perfect similarity) to -1(perfect negative similarity)
        """
        # find the length of vectors (a.ratings) and (b.ratings)
        X = math.sqrt(sum([a.rating[x] ** 2 for x in a.rating if x in b.rating]))
        Y = math.sqrt(sum([b.rating[x] ** 2 for x in b.rating if x in a.rating]))
        return dot_product(a, b) / (X * Y)
