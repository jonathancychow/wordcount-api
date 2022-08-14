from bs4 import BeautifulSoup
from string import punctuation
import requests
import unicodedata

class Scraper:

    @classmethod    
    def get_text(cls, url)->list:

        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        text = soup.get_text()
        # cleaned_word = [word.lower() for line in text.splitlines() for word in line.split(' ') if (word and word not in punctuation)]
        cleaned_word = [word.lower() for line in text.splitlines() for word in unicodedata.normalize("NFKD", line).split(' ') if (word and word not in punctuation)]
        for idx, word in enumerate(cleaned_word):
            cleaned_word[idx] = word.replace(word[0],'') if word[0] in punctuation else word
            cleaned_word[idx] = word.replace(word[-1],'') if word[-1] in punctuation else word

        return cleaned_word
        # return [t for t in text.splitlines() if t]


if __name__ == '__main__':

    b = Scraper.get_text('https://www.oneword.com/home/')
    # b = Scraper.get_text('https://codedamn.com')
    # b = Scraper.get_text('https://www.bbc.com')
    from counter import Wordcounter
    d = Wordcounter.count_words(b)
