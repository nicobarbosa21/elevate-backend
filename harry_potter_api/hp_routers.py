from fastapi import APIRouter
from harry_potter_api import api_methods as harry_potter

router = APIRouter(
    prefix="/harry_potter",
    tags=["harry_potter"]
)

@router.get("/books")
def get_books():
    return harry_potter.get_all_books()

@router.get("/books/{title}")
def search_books(title: str):
    return harry_potter.search_books_by_title(title)

@router.get("/characters")
def get_characters():
    return harry_potter.get_all_characters()

@router.get("/characters/{name}")
def search_characters(name: str):
    return harry_potter.search_characters_by_name(name)

@router.get("/spells")
def get_spells():
    return harry_potter.get_all_spells()

@router.get("/spells/{name}")
def search_spells(name: str):
    return harry_potter.search_spells_by_name(name)