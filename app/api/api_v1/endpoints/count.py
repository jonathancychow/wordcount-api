import logging
from fastapi import APIRouter
from app.services.scraper import Scraper
from app.services.counter import Wordcounter
from app.schemas import Count

logger = logging.getLogger('wordcount')
# logger = logging.getLogger(__name__) 

router = APIRouter()

@router.get("/")
def get_website(Website:Count):
    logging.info(f"url:{Website.url}")
    print(f"url:{Website.url}")

    scraper:list = Scraper.get_text(Website.url)
    word_count = Wordcounter.count_words(scraper)

    return word_count