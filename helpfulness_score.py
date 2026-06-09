import json
from mrjob.job import MRJob
from mrjob.step import MRStep

class HelpfulnessScore(MRJob):

    def mapper(self, _, line):
        review = json.loads(line)

        product_id = review.get('asin')
        helpful = review.get('helpful')

        if product_id and helpful:
            helpful_votes = helpful[0]
            total_votes = helpful[1]

            if total_votes > 0:
                score = helpful_votes / total_votes
                yield product_id, (score, 1)

    def combiner(self, product_id, values):
        total_score = 0
        count = 0

        for score, c in values:
            total_score += score
            count += c

        yield product_id, (total_score, count)

    def reducer(self, product_id, values):
        total_score = 0
        count = 0

        for score, c in values:
            total_score += score
            count += c

        if count > 0:
            average_score = total_score / count
            yield product_id, round(average_score, 4)

if __name__ == '__main__':
    HelpfulnessScore.run()