import joblib

def load_model():
    model = joblib.load("regression.joblib")
    return model

def predict_price(model, size, nb_rooms, garden):
    prediction = model.predict([[size, nb_rooms, garden]])
    if prediction[0] < 0:
        return 0
    return prediction[0]
