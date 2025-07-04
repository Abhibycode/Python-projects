from bs4 import BeautifulSoup

import lxml

with open("website.html") as web:
    contents = web.read()

soup = BeautifulSoup(contents, "html.parser")

print(soup.title)
heading =  soup.find(name="h1", id="name")
print(heading)

all_anchors = soup.find_all(name="p")
for tags in all_anchors:
    print(tags)

company_name = soup.select_one(selector="#name")
print(company_name)