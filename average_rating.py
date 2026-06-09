import json
from mrjob.job import MRJob
from mrjob.step import MRStep

class AverageRatingPerProduct(MRJob):

    def mapper(self, _, line):
        review = json.loads(line)
        product_id = review.get('asin')
        rating = review.get('overall')

        if product_id and rating is not None:
            yield product_id, (float(rating), 1)

    def combiner(self, product_id, values):
        total_rating = 0
        total_count = 0

        for rating, count in values:
            total_rating += rating
            total_count += count

        yield product_id, (total_rating, total_count)

    def reducer(self, product_id, values):
        total_rating = 0
        total_count = 0

        for rating, count in values:
            total_rating += rating
            total_count += count

        average_rating = total_rating / total_count

        yield product_id, round(average_rating, 2)

if __name__ == '__main__':
    AverageRatingPerProduct.run()