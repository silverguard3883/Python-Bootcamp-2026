from bs4 import BeautifulSoup
import lxml

with open("website.html", "r") as website:
    website = website.read()

soup = BeautifulSoup(website, "html.parser")
print(soup.title)
print(soup.title.text)
print(soup.prettify())


print(soup.find_all(name="a"))
print(soup.find_all(name="p"))

for tag in soup.find_all(name="a"):
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading.text)

section_heading = soup.find(name="h3", class_="section")        #"Class" is a reserved word in Python; we need the underscore after it to differentiate it

company_url = soup.select_one(selector= "p a")
print(company_url.text)



