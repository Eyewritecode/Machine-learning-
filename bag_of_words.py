import numpy as np
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import CountVectorizer
count  = CountVectorizer()
stemmer = SnowballStemmer("english")
sw = stopwords.words("english")
docs = np.array([
	'The sun is shine',
	'The weather is sweetness',
	'The sun is shining and the weather is sweet',
	'Today was sunny as hell'])

stemmed_words = []
for word in docs:
	stemmed_words.append(stemmer.stem(word))

#make a bag of words from stemmed words
bag = count.fit(stemmed_words)
bag = count.transform(stemmed_words)

print(bag) #prints out the tuple(d, t) f
print(bag.toarray()) #formats the output in feature vectors
print(count.vocabulary_) #prints out (t, f)
print(len(sw)) #prints out the size of our stopwords
