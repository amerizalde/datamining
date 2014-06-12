import loaders
import filters
import random
from pprint import pprint

# load the data into memory
ratings = loaders.loadRatingsDB(path="C:/backup/_scripts/py/datamining/data/BX-Dump/")
books = loaders.loadBooksDB(path="C:/backup/_scripts/py/datamining/data/BX-Dump/")
# list of all users
users = [v for k, v in ratings.items()]

def main():
	# pick a user
	lucky_winner = random.choice(users)
	# find recommendations
	isbns = filters.recommender(lucky_winner, users, "PEARSON", 4)
	# isbns is a list of tuples. get book names, key should be tuple[1]
	for book in isbns:
		key = book[1]
		pprint(books[key])

for i in xrange(20):
	print("Test Iteration {}".format(i))
	main()
	print("\n")
