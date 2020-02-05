##### THIS SCRIPT GOT ALL BUT 23 EPISODES PROPERLY #####
##### The episodes not writing properly are not on the website properly #####
import requests
from bs4 import BeautifulSoup

episodes = open('title.txt', 'r')
for episode in episodes:
        # The [:-1] is to get rid of the \n in the file
        # This is necessary otherwise the url will 404
        url = 'https://theinfosphere.org' + episode[:-1]
        r = requests.get(url)

        soup = BeautifulSoup(r.text, "lxml")

        # Remove Timestamp from text
        for timestamp in soup.find_all("span", {"class" : "timestamp"}):
                timestamp.decompose()

        quotes = soup.find_all("div", {"class":"poem"})

        filename = url[37:] + '.txt'
        f = open('episodes\\' + filename, "w", encoding="utf-8")
        print(filename)
        for quote in quotes:
            f.write(quote.text)

        f.close()
