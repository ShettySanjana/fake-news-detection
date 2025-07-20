import joblib
import os
def load_model():
    model_path = os.path.join("models", "fake_news_model.pkl")
    vectorizer_path = os.path.join("models", "vectorizer.pkl")

    if not os.path.exists(model_path) or not os.path.exists(vectorizer_path):
        raise FileNotFoundError("Model or vectorizer not found in 'models/' directory.")

    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)
    return model, vectorizer

def predict_news(news_text, model, vectorizer):
    vectorized_text = vectorizer.transform([news_text])
    prediction = model.predict(vectorized_text)
    return "Fake" if prediction[0] == 1 else "Real"
    