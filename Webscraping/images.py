from bs4 import BeautifulSoup
import requests
from io import BytesIO
from PIL import Image
import os


def startSearch():

    search = input("Search for: ")
    params = {"q":search}
    dirName = search.replace(" ", "_").lower()

    if not os.path.isdir(dirName):
        os.makedirs(dirName)
    r = requests.get("https://bing.com/images/search", params=params)

    soup = BeautifulSoup(r.text, "html.parser")

    links = soup.findAll("a", {"class": "thumb"})

    for item in links:
        try:
            imgObj = requests.get(item.attrs["href"])
            try:
                print(item.attrs["href"])
                title = item.attrs["href"].split("/")[-1]
                img = Image.open(BytesIO(imgObj.content))
                img.save("./"+dirName+"/"+title,img.format)
            except:
                print('Could not save image')
        except:
            print('Could not request image')

    startSearch()

startSearch()
