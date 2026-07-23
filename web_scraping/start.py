from bs4 import BeautifulSoup
import requests


def web_scrape():
    target = requests.get('https://quotes.toscrape.com/')
    target_in_html = BeautifulSoup(target.text, 'html.parser')
    quotes = target_in_html.findAll('span', attrs={'class': 'text'})
    authors = target_in_html.findAll('small', attrs={'class': 'author'})

    for author, quote in zip(authors, quotes):
        print(f'{author.text}:\n  {quote.text}')


def main():
    web_scrape()


if __name__ == '__main__':
    main()