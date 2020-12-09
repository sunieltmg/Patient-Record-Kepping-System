from bs4 import BeautifulSoup
import os
import requests

source=requests.get('https://www.springdale.edu.np/index.php').text
with open(source) as html_file:
    soup=BeautifulSoup(html_file,'lxml')

print(soup)
