import requests, random
from bs4 import BeautifulSoup

VIBES = ["inspiration", "love", "happy", "life"]

class Quote(object):
    def __init__(self, quote, author):
        self.quote = quote
        self.author = author
    
    def __repr__(self):
        return f'{self.quote}\n\t~{self.author}'

class QuoteGrabber(object):
    @staticmethod
    def grab_quote():
        vibe = VIBES[random.randint(0, len(VIBES)-1)]
        page = requests.get(f'http://quotes.toscrape.com/tag/{vibe}')
        
        if page.status_code == 200:
            # Instantiate Beautiful Soup object with page content
            soup = BeautifulSoup(page.content, 'html.parser')
        else:
            print("Your soup is some garbo my guy")
            quit()
        
        # Grab all quotes and authors from the return values
        quotes = soup.find_all('div', class_="quote")
        f = lambda q : [q.find('span', class_='text').text, \
                        q.find('small', class_='author').text]
        quote_list = list(map(f, quotes))
        
        quote = quote_list[random.randint(0, len(quote_list) - 1)]
        quote = Quote(*quote)
        return quote
