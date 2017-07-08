import urllib
from bs4 import BeautifulSoup
url = "http://www.ifeng.com"
html = ""


def getHTML():
    response = urllib.urlopen(url)
    global html
    html = response.read()
    print html


def parse():
    soup = BeautifulSoup(html, "html.parser")
    importDiv = soup.select("div[id=headLineDefault]")

    head = importDiv[0]
    ulList = head.select("ul[class=FNewMTopLis]")
    newsList = ulList[0]
    liList = newsList.select("li")

    for index in range(len(liList)):
        item = liList[index]
        aList = item.select("a")
        if len(aList) == 1:
            print item.string


while(True):

    getHTML()
    parse()
    # time.sleep(600)


