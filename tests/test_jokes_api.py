from jokes_api import api_methods as jokes

def test_jokes_api():
    joke = jokes.get_random_joke()
    assert "joke" in joke
    assert len(joke) == 4

def test_oneliner_joke():
    joke = jokes.get_oneliner_joke()
    assert joke["subtype"] == "One-liner"

def test_observational_joke():
    joke = jokes.get_observational_joke()
    assert joke["subtype"] == "Observational"

def test_wordplay_joke():
    joke = jokes.get_wordplay_joke()
    assert joke["subtype"] == "Wordplay"

def test_long_joke():
    joke = jokes.get_long_joke()
    assert joke["subtype"] == "Long"

def test_stereotype_joke():
    joke = jokes.get_stereotype_joke()
    assert joke["subtype"] == "Stereotype"
