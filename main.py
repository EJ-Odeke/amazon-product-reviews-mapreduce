import re
import json
from mrjob.job import MRJob
from mrjob.step import MRStep

class Wordcounter(MRJob):

    def mapper(self, _, line):

        review = json.loads(line)

        review_text = review.get('reviewText', '')

        tokens = re.findall(r"\b\w+\b", review_text.lower())

        for token in tokens:
            yield token, 1

    def combiner(self, key, values):
        yield key, sum(values)

    def reducer(self, key, values):
        yield None, (sum(values),key)

    def steps(self):
        return [
            MRStep(
                mapper=self.mapper,

                reducer=self.reducer
            )
        ]

if __name__ == '__main__':
    Wordcounter.run()