import json
from sklearn.ensemble import RandomForestClassifier
import joblib

def load_training_data():
    with open('data/sample_credentials.json', 'r') as file:
        data = json.load(file)
    features = [list(item['data'].values()) for item in data]
    labels = [item['verified'] for item in data]
    return features, labels

def train_model():
    features, labels = load_training_data()
    model = RandomForestClassifier()
    model.fit(features, labels)
    joblib.dump(model, 'ai/model.pkl')

# Example usage
train_model()
