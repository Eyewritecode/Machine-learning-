from sklearn import naive_bayes
import csv as csv
import numpy as np
csv_train_data = csv.reader(open("data/train_kaggle.csv", "rb"))
csv_test_data = csv.reader(open("data/test_kaggle.csv", "rb"))
csv_train_labels = csv.reader(open("data/trainLabels.csv", "rb"))
training_data=[]
test_data = []
trainLabels = []

for i in csv_train_data:
	training_data.append(i)
training_data = np.array(training_data, dtype = 'float_')


for data in csv_test_data:
	test_data.append(data)
test_data = np.array(test_data, dtype = 'float_')

for stuff in csv_train_labels:
	trainLabels.append(stuff)



clf = naive_bayes.GaussianNB()
clf.fit(training_data, trainLabels)
clf.predict(test_data)

#print clf.score(test_data)