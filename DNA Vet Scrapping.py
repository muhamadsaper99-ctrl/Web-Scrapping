# Importing Libraries.

from base64 import encode
from os import write
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

# ------------------------------------------------------------------------------

f = open("DNA Vet.csv", "w")
f.write("ID, Company Name, Category, Country, Email, Phone, Website\n")
url = "https://dnavetcare.co.uk/contact-us/"
site = urlopen(url)
html = site.read()
site.close()
soup = bs(html, "html.parser")
containers = soup.find_all("div",{"class":"vc_col-sm-6"})
id = 1
for c in containers[0]:
    c1 = c.find_all("p")
    for i in c1:
        title = i.find_all("strong")
        t = title[0].text.strip()
        website = i.find_all("a")
        w = website[2].text.strip()
        email = i.find_all("a")
        e = email[1].text.strip()
        phone = i.find_all("a")
        p = phone[0].text.strip()
        f.write(str(id) + ","+t + "," +""+","+"UK"+"," + e + ","+ p + "," +w+"\n")
        id += 1

for c in containers[1]:
    c1 = c.find_all("p")
    for i in c1:
        title = i.find_all("strong")
        t = title[0].text.strip()
        website = i.find_all("a")
        w = website[2].text.strip()
        email = i.find_all("a")
        e = email[1].text.strip()
        phone = i.find_all("a")
        p = phone[0].text.strip()
        f.write(str(id) + ","+t + "," +""+","+"UK"+"," + e + ","+ p + "," +w+"\n")
        id += 1
f.close()