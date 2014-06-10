import math


class Consumer(object):
	""" Datastore of a consumer's ratings.

		Can add more ratings to the store with .rate_product()

		rate_product(<item>, <rating>)
			item := a name of an item
			rating := a number representing the consumer's opinion 
					of the product. 
	"""

	def __init__(self, name, **kwargs):
		self.name = name
		self.rating = {}
		# how many results to show the user
		self.recommendations = kwargs.get("recommendations", 5)

	def rate_product(self, item, rating):
		self.rating[item] = rating

def manhattan_distance(a, b):
	""" manhattan_distance = (your.x - other.x) + (your.y - other.y) """
	return ((a.x - b.x) + (a.y - b.y))

def euclidean_distance(a, b):
	""" e_distance = math.sqrt((your.x - other.x) ** 2 + (your.y - other.y) ** 2) """
	return math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)

def compare_consumers(a, b, algo="e"):
	""" find how similar two consumers tastes are, by using their ratings
		to compute their 'distance' from one another. """
	if algo == "m":
		pass
	else:
		# find the identical purchases
		matches = []
		for key in a.rating.keys():
			if key not in b.rating.keys():
				continue
			else:
				# a matching purchase
				i = a.rating.get(key)
				j = b.rating.get(key)
				if None not in (i, j):
					matches.append((i, j))

		# euclidean
		tracker = sum([((match[0] - match[1]) ** 2) for match in matches])
		return math.sqrt(tracker)

def minkowski(rating1, rating2, r=2):
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

def pearson(a_rating, b_rating):
	matches = 0
	summ_ab = 0
	summ_a = 0
	summ_b = 0
	summ_a2 = 0
	summ_b2 = 0
	for key in a_rating:
		if key in b_rating:
			matches += 1
			x = a_rating[key]
			y = b_rating[key]
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

def dot_product(a, b):
	return sum([(a[x] * b[x]) for x in a if x in b])

def similarity(a, b):
	""" cosine similarity

	range from 1(perfect similarity) to -1(perfect negative similarity)"""
	# find the length of vectors (a.ratings) and (b.ratings)
	X = math.sqrt(sum([a[x] ** 2 for x in a if x in b]))
	Y = math.sqrt(sum([b[x] ** 2 for x in b if x in a]))
	return dot_product(a, b) / (X * Y)

def nearestNeighbors(consumer, neighbors, func):
	""" return a list of neighbors sorted by distance. """
	distances = []
	for user in neighbors:
		if user == consumer:
			continue
		else:
			algorithms = {
				"MINKOSWI": minkowski,
				"PEARSON": pearson,
				"COSINE": similarity,
				}
			distance = algorithms[func](consumer.rating, user.rating)
			distances.append((distance, user))
	distances.sort()
	return distances

def recommend(username, users, func="MINKOSWI"):
	""" Give list of recommendations based on other users purchases.
		
		options for func := "MINKOSWI", "PEARSON", "COSINE"
	"""
	if func in ("MINKOSWI", "PEARSON", "COSINE"):
		nearest = nearestNeighbors(username, users, func)[0][1]  # the object only
	else:
		return """Error: options for func := MINKOSWI, PEARSON, COSINE"""
	recommendations = []
	# we are only recommending items the consumer has not already purchased.
	for item in nearest.rating.keys():
		if item not in username.rating.keys():
			recommendations.append((item, nearest.rating[item]))
	recommendations.sort()
	return recommendations

def recommender(consumer, users, func, k):
	""" implement recommend() with (K)Nearest Neighbors."""
	if func in ("MINKOSWI", "PEARSON", "COSINE"):
		# 1:: get a list of users ordered by function()
		nearest = nearestNeighbors(consumer, users, func)
	else:
		return """Error: options for func := MINKOSWI, PEARSON, COSINE"""
	nearest.sort(reverse=True)
	recommendations = {}
	consumer_ratings = consumer.rating
	totalDistance = 0.
	for i in range(k):
		totalDistance += nearest[i][0]
	for i in range(k):
		# lookup once
		user_weight = nearest[i][0] / totalDistance
		user_ratings = nearest[i][1].rating
		# iterate through this user's rates purchases...
		for artist in user_ratings:
			if not artist in consumer_ratings:
				# if its not already recommended, add it
				if artist not in recommendations:
					recommendations[artist] = (
						user_ratings[artist] * user_weight)
				# otherwise, update the rating
				else:
					recommendations[artist] = (
						recommendations[artist]
						+ user_ratings[artist] * user_weight)
	# morph data into a sortable sequence
	recommendations = [(value, key) for key, value in recommendations.items()]
	recommendations.sort()
	# return only the number of recommendations the consumer wants.
	return recommendations[:consumer.recommendations]


if __name__ == "__main__":
	Hailey = Consumer("Hailey")
	Veronica = Consumer("Veronica")
	Jordyn = Consumer("Jordyn")
	Angelica = Consumer("Angelica")
	Bill = Consumer("Bill")
	Chan = Consumer("Chan")
	Dan = Consumer("Dan")
	Sam = Consumer("Sam")

	# products
	blues_traveler = "Blues Traveler"
	broken_bells = "Broken Bells"
	deadmau5 = "Deadmau5"
	norah_jones = "Norah Jones"
	phoenix = "Phoenix"
	slightly_stoopid = "Slightly Stoopid"
	the_strokes = "The Strokes"
	vampire_weekend = "Vampire Weekend"

	# add ratings
	Hailey.rate_product(broken_bells, 4)
	Hailey.rate_product(deadmau5, 1)
	Hailey.rate_product(norah_jones, 4)
	Hailey.rate_product(the_strokes, 4)
	Hailey.rate_product(vampire_weekend, 1)

	Veronica.rate_product(blues_traveler, 3)
	Veronica.rate_product(norah_jones, 5)
	Veronica.rate_product(phoenix, 4)
	Veronica.rate_product(slightly_stoopid, 2.5)
	Veronica.rate_product(the_strokes, 3)
	
	Jordyn.rate_product(broken_bells, 4.5)
	Jordyn.rate_product(deadmau5, 4)
	Jordyn.rate_product(norah_jones, 5)
	Jordyn.rate_product(phoenix, 5)
	Jordyn.rate_product(slightly_stoopid, 4.5)
	Jordyn.rate_product(the_strokes, 4)
	Jordyn.rate_product(vampire_weekend, 4)

	Angelica.rate_product(blues_traveler, 3.5)
	Angelica.rate_product(broken_bells, 2)
	Angelica.rate_product(norah_jones, 4.5)
	Angelica.rate_product(phoenix, 5)
	Angelica.rate_product(slightly_stoopid, 1.5)
	Angelica.rate_product(the_strokes, 2.5)
	Angelica.rate_product(vampire_weekend, 2)

	Bill.rate_product(blues_traveler, 2.0)
	Bill.rate_product(broken_bells, 3.5)
	Bill.rate_product(deadmau5, 4)
	Bill.rate_product(phoenix, 2)
	Bill.rate_product(slightly_stoopid, 3.5)
	Bill.rate_product(vampire_weekend, 3)

	Chan.rate_product(blues_traveler, 5)
	Chan.rate_product(broken_bells, 1)
	Chan.rate_product(deadmau5, 1)
	Chan.rate_product(norah_jones, 3)
	Chan.rate_product(phoenix, 5)
	Chan.rate_product(slightly_stoopid, 1)

	Dan.rate_product(blues_traveler, 3)
	Dan.rate_product(broken_bells, 4)
	Dan.rate_product(deadmau5, 1)
	Dan.rate_product(phoenix, 3)
	Dan.rate_product(slightly_stoopid, 4.5)
	Dan.rate_product(the_strokes, 4)
	Dan.rate_product(vampire_weekend, 2)

	Sam.rate_product(blues_traveler, 5)
	Sam.rate_product(broken_bells, 2)
	Sam.rate_product(norah_jones, 3)
	Sam.rate_product(phoenix, 5)
	Sam.rate_product(slightly_stoopid, 4)
	Sam.rate_product(the_strokes, 5)

	users = (Hailey, Veronica, Jordyn, Angelica, Bill, Chan, Dan, Sam)

	print("** Hailey's results:\n\n{}\n".format(recommend(Hailey, users)))
	print("** Veronica's results:\n\n{}\n".format(recommend(Veronica, users, "PEARSON")))
	print("** Jordyn's results:\n\n{}\n".format(recommend(Jordyn, users, "COSINE")))
	print("** Angelica's results:\n\n{}\n".format(recommend(Angelica, users)))
	print("** Bill's results:\n\n{}\n".format(recommend(Bill, users, "PEARSON")))

	print("Pearson Test :: Angelica, Bill: 	{}".format(
		pearson(Angelica.rating, Bill.rating)))
	print("Pearson Test :: Angelica, Hailey: 	{}".format(
		pearson(Angelica.rating, Hailey.rating)))
	print("Pearson Test :: Angelica, Jordyn: 	{}".format(
		pearson(Angelica.rating, Jordyn.rating)))

	print("Similarity of Angelica to Veronica: 	{}".format(
		similarity(Angelica.rating, Veronica.rating)))
	print("Similarity of Angelica to Hailey: 	{}".format(
		similarity(Angelica.rating, Hailey.rating)))
	print("Similarity of Angelica to Jordyn: 	{}".format(
		similarity(Angelica.rating, Jordyn.rating)))
	print("\n")
	print("** Hailey's results:\n\n{}\n".format(recommender(Hailey, users, "PEARSON", 3)))
	print("** Veronica's results:\n\n{}\n".format(recommender(Veronica, users, "PEARSON", 4)))
	print("** Jordyn's results:\n\n{}\n".format(recommender(Jordyn, users, "COSINE", 3)))
	print("** Angelica's results:\n\n{}\n".format(recommender(Angelica, users, "MINKOSWI", 5)))
	print("** Bill's results:\n\n{}\n".format(recommender(Bill, users, "PEARSON", 5)))
