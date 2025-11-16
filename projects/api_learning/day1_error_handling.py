import requests

url = "https://v2.jokeapi.dev/joke/Any"
try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    data = response.json()

    if "type" not in data:
        print("Unexpected response format.")
    else:
        if data["type"] == "single":
            print("Joke:", data.get("joke", "No joke found."))
        else:
            print("Setup:", data.get("setup", "No setup found."))
            print("Punchline:", data.get("delivery", "No delivery found."))
except requests.exceptions.Timeout:
    print("Error: The request timed out. Please check your internet.")
except requests.exceptions.ConnectionError:
    print("Error: Could not connect to the server. Please check your internet.")
except requests.exceptions.HTTPError as e:
    print("HTTP Error:", e)
except ValueError:
    print("Error: Could not decode the response as JSON.")
except Exception as e:
    print("Unexpected error:", e)