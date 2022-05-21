import requests
URL = "http://laspositascollege.edu/class-schedule/"
html_doc = requests.get(URL)

#print(html_doc.text)

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc.content, 'html.parser')
#print (soup)

for anchor in soup.find_all("a", class_="btn btn-lpc btn-350"):
    print(anchor)

print("----anchor.get_text()-----")
for anchor in soup.find_all("a", class_="btn btn-lpc btn-350"):
    print(anchor.get_text())
print("----anchor.href-----")
for anchor in soup.find_all("a", class_="btn btn-lpc btn-350"):
    print(anchor['href'])