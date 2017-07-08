# -*- coding: utf-8 -*-
# @Author: liuhao
# @Date:   2017-02-22 20:22:51
# @Last Modified by:   liuhao
# @Last Modified time: 2017-02-22 22:18:50
import urllib
import re

url = "https://www.douyu.com/directory/game/yz"
response = ""


def getHTML():
    res = urllib.urlopen(url)
    global response
    response = res.read()


def parseAndSaveImage():
    imgs = re.findall(r'data-original="(.*?\.jpg)"', response)
    current = 0
    for img in imgs:
        print(img)
        urllib.urlretrieve(
            img, filename="C:\\Users\\Administrator\\Desktop\\test\\%d.jpg" % current)
        current = current + 1


getHTML()
parseAndSaveImage()
