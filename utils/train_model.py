import pandas as pd

import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

import joblib

ONLY_OVER_18 = False
TEST_SIZE = 0.25

dataset = pd.read_csv('harry_all.csv', delimiter=';',)

bigfive_column_keys = ['IPIP_Extraversion', 'IPIP_EmStability',
                       'IPIP_Intellect',  'IPIP_Agreeableness', 'IPIP_Conscientiousness']  # With the bigfive-test.com naming, these are: Extraversion, Neuroticism, Openness to experience, Agreeableness and Conscientiousness


# Remove rows with multiple houses or with invalid age (if ONLY_OVER_18 is True)
for index, row in dataset.iterrows():
    houses_number = len(row['Sorting_house'].split(';'))
    age = row['age']
    if houses_number != 1 or (ONLY_OVER_18 and age < 18):
        dataset = dataset.drop(index)

# Calculate a list's boundaries, outside of these, a value is considered an outlier


def get_bounds(data):
    q1, q3 = np.percentile(sorted(data), [25, 75])

    iqr = q3 - q1

    lower_bound = q1 - (1.5 * iqr)
    upper_bound = q3 + (1.5 * iqr)

    bounds = {
        "lower_bound": lower_bound,
        "upper_bound": upper_bound
    }

    return bounds


# Calculate boundaries for each house's personality traits
house_groups = dataset.groupby('Sorting_house')
house_bounds = {}
for name, group in house_groups:
    bounds = {}
    for key in bigfive_column_keys:
        bounds[key] = get_bounds(group[key])
    house_bounds[name] = bounds

for index, row in dataset.iterrows():
    house = row['Sorting_house']
    bounds = house_bounds[house]

    for key in bigfive_column_keys:
        trait_bounds = bounds[key]
        lower_bound = trait_bounds['lower_bound']
        upper_bound = trait_bounds['upper_bound']

        val = row[key]
        if val <= lower_bound or val >= upper_bound:
            dataset = dataset.drop(index)
            break


X = dataset[bigfive_column_keys]
y = dataset['Sorting_house']

X = X.values
y = y.values

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=TEST_SIZE, random_state=42)

clf = GaussianNB()
clf.fit(X_train, y_train)

score = clf.score(X_test, y_test)
print(f"Testing score: {score}")

joblib.dump(clf, "model.pkl")
