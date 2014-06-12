
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
