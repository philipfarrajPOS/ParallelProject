import pandas as pd
from textblob import TextBlob
import multiprocessing as mp
import time


def calc(review):
    review_blob = TextBlob(str(review))
    polarity = review_blob.sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"


df = pd.read_csv('googleplaystore_user_reviews.csv')

reviews = df.Translated_Review

pool = mp.Pool(processes=8)

start = time.time()
new_labels = pool.map(calc, [rev for rev in reviews])
end = time.time()
print(end - start)
pool.close()

df['new labels'] = new_labels
df.to_csv("new_data.csv")
