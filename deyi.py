# -*- coding: utf-8 -*-
# @Author: liuhao
# @Date:   2017-02-23 21:51:46
# @Last Modified by:   liuhao
# @Last Modified time: 2017-02-23 23:10:53
from bs4 import BeautifulSoup
import urllib

deyihHome = ""
def getDeyi():
	response = urllib.urlopen("http://www.deyi.com")
	global deyiHome
	deyiHome = response.read()

def parseTopNews():
	soup = BeautifulSoup(deyiHome,"html.parser")
	center = soup.select("div[id=icf_center_front]")
	topNewsList = center[0].select("div[class=article_brief]")
	print len(topNewsList)

	for item in topNewsList:
		topNews = item
		a = topNews.select("a")
		print a[0].string
	
getDeyi()
parseTopNews()
