from requests import get

base_url = "https://italian-jokes.vercel.app"

def get_random_joke():
    response = get(f"{base_url}/api/jokes")
    return response.json()

def get_oneliner_joke():
    response = get(f"{base_url}/api/jokes?subtype=One-liner")
    return response.json()

def get_observational_joke():
    response = get(f"{base_url}/api/jokes?subtype=Observational")
    return response.json()

def get_wordplay_joke():
    response = get(f"{base_url}/api/jokes?subtype=Wordplay")
    return response.json()

def get_long_joke():
    response = get(f"{base_url}/api/jokes?subtype=Long")
    return response.json()

def get_stereotype_joke():
    response = get(f"{base_url}/api/jokes?subtype=Stereotype")
    return response.json()
