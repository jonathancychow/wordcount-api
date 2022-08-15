from bs4 import BeautifulSoup
from string import punctuation

import re
import requests
import unicodedata

class Scraper:

    @staticmethod
    def text_string_to_list(text_string)->list:
        # Splitlines, split with space, normalize and remove punctuation
        cleaned_word = [word.lower() for line in text_string.splitlines() for word in unicodedata.normalize("NFKD", line).split(' ') if (word and word not in punctuation)]
        
        # Keep character only
        cleaned_word = [re.sub(r'[^\w\s]', '', word) for word in cleaned_word if re.sub(r'[^\w\s]', '', word)]

        return cleaned_word

    @classmethod    
    def get_text(cls, url)->list:

        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        text = soup.get_text()

        return cls.text_string_to_list(text)
