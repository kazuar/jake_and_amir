
import requests
from bs4 import BeautifulSoup

BASE_URL = "http://scripts.jakeandamir.com/"
URL_PARAMS = "index.php?search=a&from-date=&to-date=&do-search=1"

def get_details(article):
    return None

def main():
    url = BASE_URL + URL_PARAMS
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")

    articles = soup.find_all("article")

    print "Found {0} articles".format(articles)

    for article in articles:
        details = get_details(article)

if __name__ == '__main__':
    main()
