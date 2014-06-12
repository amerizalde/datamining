import codecs
import Consumer

def loadBookDB(path=""):
    """ load the ratings, users and titles into memory. """
    ratings = "BX-Book-Ratings.csv"
    users = dict()
    with codecs.open(path + ratings, "r", "utf8") as data:
        for line in data:
            fields = line.split(";")
            user = fields[0].strip('"')
            isbn = fields[1].strip('"')
            rating = int(fields[2].strip().strip('"'))
            # if object in dict
            if user in users:
                users[user].rate_product(isbn, rating)
            else:
                # create object and add to dict
                users[user] = Consumer.Consumer(user)
                users[user].rate_product(isbn, rating)
    return users

if __name__ == "__main__":
    import pprint as pp
    db = loadBookDB(path="C:/backup/_scripts/py/datamining/data/BX-Dump/")
    
    users = [db[user].rating for user in db if len(db[user].rating) > 0]
    pp.pprint(users)
