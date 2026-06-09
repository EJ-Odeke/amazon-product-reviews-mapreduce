import json
from mrjob.job import MRJob
from mrjob.step import MRStep

class ReviewCountPerProduct(MRJob):

    #  count reviews per product
    def mapper(self, _, line):
        review = json.loads(line)

        product_id = review.get('asin')
        if product_id:
            yield product_id, 1

    def combiner(self, product_id, counts):
        yield product_id, sum(counts)

    def reducer_count(self, product_id, counts):
        yield None, (product_id, sum(counts))

    #  sort results
    def reducer_sort(self, _, product_counts):

        sorted_results = sorted(product_counts, key=lambda x: x[1])  # ascending by count

        for product_id, total in sorted_results:
            yield product_id, total

    def steps(self):
        return [
            MRStep(
                mapper=self.mapper,
                combiner=self.combiner,
                reducer=self.reducer_count
            ),
            MRStep(
                reducer=self.reducer_sort
            )
        ]

if __name__ == '__main__':
    ReviewCountPerProduct.run()