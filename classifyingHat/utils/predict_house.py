import joblib

clf = joblib.load("model.pkl")

def predict_house(extraversion, neuroticism, openness, agreeableness, conscientiousness):
    values = [extraversion, neuroticism, openness, agreeableness, conscientiousness] # In case the model order wasn't the same
    def calc(x, max):
        return (x/max)*50

    for m in range(len(values)):
        values[m] = calc(values[m], 120)   

    return str(clf.predict([values])[0])