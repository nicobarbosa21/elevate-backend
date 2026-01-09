from fastapi import APIRouter
from jokes_api import api_methods as jokes

router = APIRouter(
    prefix="/jokes",
    tags=["jokes"]
)

@router.get("/random_joke")
def get_joke():
    return jokes.get_random_joke()

@router.get("/oneliner_joke")
def get_oneliner():
    return jokes.get_oneliner_joke()

@router.get("/observational_joke")
def get_observational():
    return jokes.get_observational_joke()

@router.get("/wordplay_joke")
def get_wordplay():
    return jokes.get_wordplay_joke()

@router.get("/long_joke")
def get_long():
    return jokes.get_long_joke()

@router.get("/stereotype_joke")
def get_stereotype():
    return jokes.get_stereotype_joke()