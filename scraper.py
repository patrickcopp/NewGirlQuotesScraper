from urllib.request import urlopen
from bs4 import BeautifulSoup

index_url = "https://transcripts.foreverdreaming.org/viewtopic.php?f=50&t=7443"
page = urlopen(index_url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, features="html.parser")
list_tags = soup.find_all("p")

LISTER = []

for i in range(4, len(list_tags)):
    if "<strong>Note</strong>" in str(list_tags[i]):
        break
    if "<strong>Season" not in str(list_tags[i]) and len(str(list_tags[i])) > 10 and "google" not in str(list_tags[i]):
        LISTER.append(str(list_tags[i]).split("\"")[3].replace("&amp;", "&"))

for url in LISTER:
    html = urlopen(url).read().decode("utf-8")
    soup = BeautifulSoup(html, features="html.parser")
    text = soup.find(attrs={"class" : "postbody"})
    title = soup.findAll(attrs={"class" : "boxheading"})[1].get_text().replace('\n', '')
    writer = open("assets/"+title+".txt", "w", encoding="utf-8")
    good_text = text.get_text().replace(r"(adsbygoogle = window.adsbygoogle || []).push({});", "")
    writer.write(good_text)
    writer.close()