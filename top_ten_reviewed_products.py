import json
from mrjob.job import MRJob
from mrjob.step import MRStep

class TopTenReviewedProducts(MRJob):

    def mapper_count_reviews(self, _, line):
        review = json.loads(line)

        product_id = review.get('asin')

        if product_id:
            yield product_id, 1

    def reducer_count_reviews(self, product_id, counts):
        yield None, (sum(counts), product_id)

    def reducer_find_top_ten(self, _, product_counts):
        top_ten = sorted(product_counts, reverse=True)[:10]

        for count, product_id in top_ten:
            yield product_id, count

    def steps(self):
        return [
            MRStep(
                mapper=self.mapper_count_reviews,
                reducer=self.reducer_count_reviews
            ),
            MRStep(
                reducer=self.reducer_find_top_ten
            )
        ]

if __name__ == '__main__':
    TopTenReviewedProducts.run()