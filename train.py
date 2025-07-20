
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import joblib
import os
import pandas as pd

# Load datasets
print("Loading datasets...")
fake = pd.read_csv("data/Fake.csv")
true = pd.read_csv("data/True.csv")

# Add labels
fake['label'] = 1
true['label'] = 0

# Combine and shuffle
df = pd.concat([fake, true])
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Use 'text' or fallback to 'title'
if 'text' in df.columns:
    X = df['text']
else:
    X = df['title']
y = df['label']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Vectorization
vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Model training
print("Training model...")
model = LogisticRegression()
model.fit(X_train_vec, y_train)

# Evaluation
y_pred = model.predict(X_test_vec)
print(classification_report(y_test, y_pred))

# Save model and vectorizer
print("Saving model...")
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/fake_news_model.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")
print("Done.")
