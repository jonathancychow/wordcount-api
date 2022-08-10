from bs4 import BeautifulSoup

import requests
# from app.api.config import config

class Scraper:

    @classmethod    
    def get_text(cls, url)->list:

        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        text = soup.get_text()
        return [t for t in text.splitlines() if t]


if __name__ == '__main__':

    b = Scraper.get_text('https://www.oneword.com/home/')
    # Scraper.get_html("https://codedamn.com")
    a = 1 
