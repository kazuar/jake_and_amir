
import requests
from bs4 import BeautifulSoup

BASE_URL = "http://scripts.jakeandamir.com/"
URL_PARAMS = "index.php?search=a&from-date=&to-date=&do-search=1"

def get_details(episode):
    episode_name = episode.find("td", "header-inner-title").text
    episode_video_url = episode.find("iframe")["data-src"]
    episode_date = episode.find("td", "header-inner-date").text
    episode_text = episode.find("div", "episode-script-inner").text

    episode_details = {
        "name": episode_name,
        "video_url": episode_video_url,
        "date": episode_date,
        "script": episode_text,
        "data": str(episode),
    }

    return episode_details

def main():
    url = BASE_URL + URL_PARAMS

    result = requests.get(url)
    soup = BeautifulSoup(result.text, "lxml")

    episodes = soup.find_all("article")

    print "Found {0} episodes".format(episodes)

    for episode in episodes:
        episode_details = get_episode_details(episode)

if __name__ == '__main__':
    main()
