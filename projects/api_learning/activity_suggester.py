import requests
import time

def get_random_activity():
    url = "https://www.boredapi.com/api/activity"

    for _ in range(3):
        try:
            response = requests.get(url, timeout=5)
            data = response.json()

            print("\n--- Activity Suggestion ---")
            print(f"Activity: {data.get('activity')}")
            print(f"Type: {data.get('type')}")
            print(f"Participants: {data.get('participants')}\n")
            return
        except Exception as e:
            print("Retrying…", e)
            time.sleep(2)

    print("Could not reach the API after several attempts.")

get_random_activity()
