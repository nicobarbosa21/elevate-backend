from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from jokes_api import api_methods as jokes
from harry_potter_api import api_methods as harry_potter
from main_api.db import Base, engine
from main_api.entities import employee, seniority, nationality, jobs
from main_api.routers import employee_routers, seniority_routers, nationality_routers, job_routers

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(employee_routers.router)
app.include_router(seniority_routers.router)
app.include_router(nationality_routers.router)
app.include_router(job_routers.router)

### Italian Jokes API Endpoints ###

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

### Harry Potter API Endpoints ###

@app.get("/harry_potter/books")
def get_books():
    return harry_potter.get_all_books()

@app.get("/harry_potter/books/{title}")
def search_books(title: str):
    return harry_potter.search_books_by_title(title)

@app.get("/harry_potter/characters")
def get_characters():
    return harry_potter.get_all_characters()

@app.get("/harry_potter/characters/{name}")
def search_characters(name: str):
    return harry_potter.search_characters_by_name(name)

@app.get("/harry_potter/spells")
def get_spells():
    return harry_potter.get_all_spells()

@app.get("/harry_potter/spells/{name}")
def search_spells(name: str):
    return harry_potter.search_spells_by_name(name)
