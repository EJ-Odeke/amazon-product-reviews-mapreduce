import json
import re
from mrjob.job import MRJob
from mrjob.step import MRStep

class SentimentAnalysis(MRJob):

    positive_words = {
        "good", "great", "excellent", "amazing",
        "love", "perfect", "nice", "awesome", "best"
    }

    negative_words = {
        "bad", "poor", "terrible", "worst",
        "hate", "awful", "boring", "disappointing"
    }

    def mapper(self, _, line):
        review = json.loads(line)

        product_id = review.get('asin')
        text = review.get('reviewText', '')

        if not product_id or not text:
            return

        words = re.findall(r"\b\w+\b", text.lower())

        pos_count = sum(1 for w in words if w in self.positive_words)
        neg_count = sum(1 for w in words if w in self.negative_words)

        if pos_count > neg_count:
            sentiment = "positive"
        elif neg_count > pos_count:
            sentiment = "negative"
        else:
            sentiment = "neutral"

        yield product_id, sentiment

    def reducer(self, product_id, sentiments):
        result = {"positive": 0, "negative": 0, "neutral": 0}

        for s in sentiments:
            result[s] += 1

        yield product_id, result

if __name__ == '__main__':
    SentimentAnalysis.run()