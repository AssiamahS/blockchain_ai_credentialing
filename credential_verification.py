import json
import joblib

def load_model():
    return joblib.load('ai/model.pkl')

def verify_credentials(data):
    model = load_model()
    credentials = data['data']
    verification_status = model.predict([credentials])
    return verification_status[0]

# Example usage
with open('data/sample_credentials.json', 'r') as file:
    sample_credentials = json.load(file)

status = verify_credentials(sample_credentials)
print("Verification Status:", status)
