import random
import string

from bs4 import BeautifulSoup
from fastapi.testclient import TestClient
from .main import app
from app.services.counter import Wordcounter
from app.services.scraper import Scraper

from string import punctuation

client = TestClient(app)

def test_counter():

    number_of_repeat = 3 
    letters = string.ascii_letters    
    random_words = ["".join(random.sample(letters,random.randint(1,10))) for _ in range(100)]
    for _ in range(number_of_repeat):
        random_words.append('word')
        random_words.append('text')
        random_words.append('sentence')

    counting = Wordcounter.count_words(random_words)
    assert counting['word'] == number_of_repeat 
    assert counting['text'] == number_of_repeat 
    assert counting['sentence'] == number_of_repeat 

def test_scraper_string_to_list():

    with open("test.html") as fp:
        soup = BeautifulSoup(fp, 'html.parser')

    a = Scraper.text_string_to_list(soup.get_text())
    assert isinstance(a, list) is True    

def test_scraper_get_text():
    text_list = Scraper.get_text('https://www.bbc.com')
    for text in text_list:
        assert len(text.splitlines()) == 1
        assert punctuation not in text

def test_health_endpoint():
    # response = client.get("/health", headers={"X-Token": "coneofsilence"})
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "name": "wordcountingservice",
        "status": "ok",
        "version": "1.0.0"
    }

def test_count_endpoint():
    # response = client.get("/health", headers={"X-Token": "coneofsilence"})
    # response = client.get("/count")
    response = client.get(
        "/count",
        # headers={"X-Token": "coneofsilence"},
        # body
        json={"url":"https://www.oneword.com/home/"},
    )

    assert response.status_code == 200
    assert response.json()['the'] == 2 
    assert response.json()['write'] == 3 
    assert response.json()['of'] == 2 
    assert response.json()['facebook'] == 1 
