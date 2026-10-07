# Tutorial 2 - Section 10: manual test client (run with the container up)
if __name__ == "__main__":
    import requests

    response = requests.post(
        "http://localhost:8000/predict",
        json={"features": [5.1, 3.5, 1.4, 0.2]},
    )
    print(response.json())
