import urllib.request
from bs4 import BeautifulSoup, Tag
import pprint

url = 'https://www.typingstudy.com/lesson/1'
url_contents = urllib.request.urlopen(url).read()

soup = BeautifulSoup(url_contents, 'html.parser')

print(soup.prettify())





'''
website incompatible

lesson_container = soup.find('div', id="lesson-container")

print(lesson_container)

lesson_soup = BeautifulSoup(lesson_container, 'html.parser')
lesson_soup.find_all('span')'''

'''
print(soup.div)





def has_class(tag):
    return tag.has_attr('class')


p = soup.find_all(has_class)

print(p)

# print(soup.prettify())

for tag in soup.find_all(True):
    print(tag.name)


for tag in soup.find_all(True):
    print(tag.name)'''