from collections import Counter

class Wordcounter:

    @classmethod    
    def count_words(cls, words:list):

        return dict(Counter(words))


