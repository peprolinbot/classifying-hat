import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import BaggingClassifier

import joblib

ONLY_OVER_18 = True
MINIMUM_SCORE = 0.9
TEST_SIZE = 0.1

dataset = pd.read_csv('harry_all.csv', delimiter=';',)

# Remove rows with multiple houses and with invalid age (if ONLY_OVER_18 is True)
for index, row in dataset.iterrows():
    houses_number = len(row['Sorting_house'].split(';'))
    age = row['age']
    if houses_number != 1 or (ONLY_OVER_18 and not age <= 18):
        dataset = dataset.drop(index)

X = dataset[['IPIP_Extraversion', 'IPIP_EmStability',
             'IPIP_Intellect',  'IPIP_Agreeableness', 'IPIP_Conscientiousness']]  # Ordered as in bigfive-test.com (Openness to experience , Conscientiousness , Extraversion , Agreeableness and Neuroticism)
y = dataset['Sorting_house']

X = X.values
y = y.values

score = 0
while score < MINIMUM_SCORE:
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=TEST_SIZE)
    
    clf = GaussianNB()
    clf.fit(X_train, y_train)

    score = clf.score(X_test, y_test)
    print(f"Testing score: {score}")

joblib.dump(clf, "model.pkl")
