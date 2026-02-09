import random
import requests
import time

API_URL = "http://127.0.0.1:8000/predict"

def generate_transaction():
    txn = {
        "Time": random.uniform(0, 172800),
        "Amount": random.uniform(1, 2000)
    }

    # PCA features
    for i in range(1, 29):
        txn[f"V{i}"] = random.uniform(-5, 5)

    return txn


def send_to_api(transaction):
    try:
        response = requests.post(API_URL, json=transaction)
        print("Status Code:", response.status_code)
        print("Raw Response:", response.text)
        return response.json()
    except Exception as e:
        print("API Error:", e)
        return None



def run_simulation(iterations=20, delay=1):
    for i in range(iterations):
        txn = generate_transaction()
        result = send_to_api(txn)

        if result and "fraud_probability" in result:
            print(f"Fraud Probability: {result['fraud_probability']:.4f}")
            print("Result:", result["prediction"])
        else:
            print("API Error:", result)


        time.sleep(delay)


if __name__ == "__main__":
    run_simulation()
