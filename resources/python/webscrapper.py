# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import sys

# Set the URL you want to webscrape from
url = 'http://www.nepalstock.com/'

# Connect to the URL
response = requests.get(url)

# Parse HTML and save to BeautifulSoup object¶
soup = BeautifulSoup(response.text, "html.parser")

redelement =soup.select('div.pull-left.banner-red.banner-item div.current-index')

nepse =0
if redelement ==0:
    nepse =soup.select('div.pull-left.banner-red.banner-item div.current-index')[0].contents[0].strip()
else:
    nepse =soup.select('div.pull-left.banner-green.banner-item div.current-index')[0].contents[0].strip()
print(nepse)
sys.stdout.flush()