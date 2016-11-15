__author__ = 'franc'


from lxml import html
import requests
page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
tree = html.fromstring(page.content)
print tree

#https://scrapy.org/
#http://jarroba.com/scraping-python-beautifulsoup-ejemplos/
# http://iwt2-javierj.tumblr.com/post/45923472556/ejemplo-de-web-scraping-con-python-y-beautiful