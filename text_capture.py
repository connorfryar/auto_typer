import requests
from bs4 import BeautifulSoup

url = "https://www.how-to-type.com/typing-practice/quote/"
resp =requests.get(url)

if resp.status_code==200:
    print('Successfully opened the web page')
    print('String captures: ')

    soup=BeautifulSoup(url_contents)

    t=soup.fin("div", "class=quote")
    print(t)



