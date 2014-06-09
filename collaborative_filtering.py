import math


class Consumer(object):
	""" Datastore of a consumer's ratings.

		Can add more ratings to the store with .rate_product()

		rate_product(<item>, <rating>)
			item := a name of an item
			rating := a number representing the consumer's opinion 
					of the product. 
	"""

	def __init__(self, name):
		self.name = name
		self.rating = {}
		self.max_rating = 0

	def rate_product(self, item, rating):
		self.rating[item] = rating

def manhattan_distance(a, b):
	""" manhattan_distance = (your.x - other.x) + (your.y - other.y) """
	return ((a.x - b.x) + (a.y - b.y))

def euclidean_distance(a, b):
	""" e_distance = math.sqrt((your.x - other.x) ** 2 + (your.y - other.y) ** 2) """
	return math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)

def dot_product(a, b):
	return sum([(a.rating[x] * b.rating[x]) for x in a.rating if x in b.rating])

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

def nearestNeighbors(consumer, neighbors):
	""" return a list of neighbors sorted by distance. """
	distances = []
	for user in neighbors:
		if user == consumer:
			continue
		else:
			# distance = compare_consumers(consumer, user)
			distance = minkowski(consumer.rating, user.rating, 2)
			distances.append((distance, user))
	distances.sort()
	return distances

def recommend(username, users):
	""" Give list of recommendations based on other users purchases. """
	nearest = nearestNeighbors(username, users)[0][1]  # the object only
	recommendations = []
	# we are only recommending items the consumer has not already purchased.
	for item in nearest.rating.keys():
		if item not in username.rating.keys():
			recommendations.append((item, nearest.rating[item]))
	recommendations.sort()
	return recommendations

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


def similarity(a, b):
	""" cosine similarity

	range from 1(perfect similarity) to -1(perfect negative similarity)"""
	return dot_product(a, b) / (
		sum([a.rating[x] ** 2 for x in a.rating if x in b.rating]) * sum(
			[b.rating[x] ** 2 for x in b.rating if x in a.rating]))


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

	users = (Hailey, Veronica, Jordyn)

	print("Hailey's results:\n{}".format(recommend(Hailey, users)))
	print("Veronica's results:\n{}".format(recommend(Veronica, users)))
	print("Jordyn's results:\n{}".format(recommend(Jordyn, users)))
	print("Angelica's results:\n{}".format(recommend(Angelica, users)))
	print("Bill's results:\n{}".format(recommend(Bill, users)))

	print("Pearson Test: {}".format(pearson(Angelica, Bill)))
	print("Pearson Test: {}".format(pearson(Angelica, Hailey)))
	print("Pearson Test: {}".format(pearson(Angelica, Jordyn)))

	print("Similarity: {}".format(similarity(Angelica, Bill)))
	print("Similarity: {}".format(similarity(Angelica, Hailey)))
	print("Similarity: {}".format(similarity(Angelica, Jordyn)))
