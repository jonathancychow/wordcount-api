from bs4 import BeautifulSoup
from string import punctuation

import re
import requests
import unicodedata

class Scraper:

    @staticmethod
    def text_string_to_list(text_string)->list:
        cleaned_word = [word.lower() for line in text_string.splitlines() for word in unicodedata.normalize("NFKD", line).split(' ') if (word and word not in punctuation)]
        cleaned_word = [re.sub(r'[^\w\s]', '', word) for word in cleaned_word if re.sub(r'[^\w\s]', '', word)]

        return cleaned_word

    @classmethod    
    def get_text(cls, url)->list:

        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        text = soup.get_text()

        return cls.text_string_to_list(text)


if __name__ == '__main__':

    b = Scraper.get_text('https://www.oneword.com/home/')
    # b = Scraper.get_text('https://codedamn.com')
    # b = Scraper.get_text('https://www.bbc.com')
    from counter import Wordcounter
    d = Wordcounter.count_words(b)
