import requests
from bs4 import BeautifulSoup

url = 'https://theinfosphere.org/Episode_Transcript_Listing'

r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

# Get all href tags
href = soup.find_all('a', href = True)

# Get all Links
links = [a['href'] for a in href]

f = open('title.txt', 'w')

for link in links:
    if link.startswith('/Transcript'):
        f.write(link + '\n')

f.close()
    
