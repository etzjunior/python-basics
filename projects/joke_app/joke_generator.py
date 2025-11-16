import requests

def get_joke():
    url = "https://official-joke-api.appspot.com/random_joke"

    try:
        response = requests.get(url)

        # convert response from JSON text → Python dict
        joke_data = response.json()

        setup = joke_data["setup"]
        punchline = joke_data["punchline"]

        return setup, punchline

    except Exception as e:
        print("Error fetching joke:", e)
        return None, None


print("\n🎭 Random Joke Generator 🎭")
print("-----------------------------")

setup, punchline = get_joke()

if setup and punchline:
    print("Setup:", setup)
    input("\n(Press ENTER for the punchline...)\n")
    print("Punchline:", punchline)
else:
    print("Could not fetch a joke. Try again later.")
