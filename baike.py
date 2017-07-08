# -*- coding: utf-8 -*-
# @Author: liuhao
# @Date:   2017-02-25 10:52:01
# @Last Modified by:   liuhao
# @Last Modified time: 2017-02-25 12:43:42

import urllib
from bs4 import BeautifulSoup

base_url = "http://baike.baidu.com/item/"
html = "";

def getHTML(url):
	response = urllib.urlopen(url)
	global html
	html = response.read()
	print html

def parse():
	soup = BeautifulSoup(html,"html.parser")
	main = soup.select("div[class=main-content]")
	if len(main)==1:
		m = main[0]
		summary = m.select("div[class=lemma-summary]")
		print type(summary)
		# if len(summary)==1:
		# 	s = summary[0]
		# 	print s
	else:
		print len(main)
		print "aaa"	

keyword = raw_input("please input  keyword that you want to check.")

getHTML(base_url+keyword)
parse()

