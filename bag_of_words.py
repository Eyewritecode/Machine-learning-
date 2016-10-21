import numpy as np
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
count  = CountVectorizer()
sw = stopwords.words("english")
docs = np.array([
	'The sun is shining',
	'The weather is sweet',
	'The sun is shining and the weather is sweet'])
bag = count.fit(docs)
bag = count.transform(docs)
print(bag)
print(count.vocabulary_)
print(len(sw))