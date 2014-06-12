import loaders
import filters
import random
from pprint import pprint

# load the data into memory
db = loaders.loadBookDB(path="C:/backup/_scripts/py/datamining/data/BX-Dump/")
# list of all users
users = [v for k, v in db.items()]
# pick a user
lucky_winner = random.choice(users)
# print recommendations
print("The PEARSON winner is:", lucky_winner.name)
pprint(filters.recommender(lucky_winner, users, "PEARSON", 4))

# pick a user
lucky_winner = random.choice(users)
# print recommendations
print("The COSINE winner is:", lucky_winner.name)
pprint(filters.recommend(lucky_winner, users, "COSINE"))
