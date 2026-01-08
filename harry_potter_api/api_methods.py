from requests import get

base_url = "https://potterapi-fedeperin.vercel.app/en"

def get_all_books():
    response = get(f"{base_url}/books")
    return response.json()

def search_books_by_title(title):
    response = get(f"{base_url}/books?search={title}")
    return response.json()

def get_all_characters():
    response = get(f"{base_url}/characters")
    return response.json()

def search_characters_by_name(name):
    response = get(f"{base_url}/characters?search={name}")
    return response.json()

# def get_all_houses():
#     response = get(f"{base_url}/houses")
#     return response.json()

# def search_houses_by_name(name):
#     response = get(f"{base_url}/houses?search={name}")
#     return response.json()

def get_all_spells():
    response = get(f"{base_url}/spells")
    return response.json()

def search_spells_by_name(name):
    response = get(f"{base_url}/spells?search={name}")
    return response.json()