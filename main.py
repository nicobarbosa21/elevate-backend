from fastapi import FastAPI
from jokes_api import jokes

app = FastAPI()

@app.get("/random_joke")
def get_joke():
    return jokes.get_random_joke()

@app.get("/oneliner_joke")
def get_oneliner():
    return jokes.get_oneliner_joke()

@app.get("/observational_joke")
def get_observational():
    return jokes.get_observational_joke()

@app.get("/wordplay_joke")
def get_wordplay():
    return jokes.get_wordplay_joke()

@app.get("/long_joke")
def get_long():
    return jokes.get_long_joke()

@app.get("/stereotype_joke")
def get_stereotype():
    return jokes.get_stereotype_joke()
