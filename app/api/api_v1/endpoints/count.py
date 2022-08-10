import logging
from fastapi import APIRouter
from app.services.scraper import Scraper
from app.schemas import Count

logger = logging.getLogger('wordcount')
# logger = logging.getLogger(__name__) 

router = APIRouter()

@router.get("/")
def GetModel(url:Count):
    logging.info(f"url:{url}")
    print(f"url:{url}")

    scraper = Scraper.get_text(url)
    print(f"{scraper}")



    return 'Counting'
