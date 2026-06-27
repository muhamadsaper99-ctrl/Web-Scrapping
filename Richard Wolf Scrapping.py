# Importing Libraries
from base64 import encode
from os import write
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
#---------------------------------------------------
url = "https://www.richard-wolf.com/en/contact/sales-service-network"
f = open("Richard Wolf.csv","w",encoding='utf-8')
f.write("ID, Company Name, Category, Country, Email, Phone, Website\n")
site = urlopen(url)
html = site.read()
site.close()
soup = bs(html,"html.parser")
# print(soup)
id = 1
container = soup.find_all("div",{"class","contactperson display__table"})
for i in container:
    t = i.find_all("div",{"class","contactperson__title headline--h3"})
    title = t[0].text.strip().split(",")[0].strip()
    pe = i.find_all("a")
    phone = pe[0].text.strip()
    email = pe[1].text.strip()
    c = i.find_all("div",{"class","contactperson__type tagline"})
    country = c[0].text.split("|")[1].strip()
    if len(pe) == 4:
        website = pe[2].text.strip()
        f.write(str(id) + "," + title + "," + "" + "," + country + "," + email + "," + phone + "," + website + "\n")
    else:
        f.write(str(id) + "," + title + "," + "" + "," + country + "," + email + "," + phone + "," + "" + "\n")
    print(f"Company {id} Done.")
    id += 1
f.close()