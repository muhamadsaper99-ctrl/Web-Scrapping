# Importing Libraries
from base64 import encode
from os import write
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

# ------------------------------------------

url = 'https://london.vetshow.com/exhibitors?&page='

# Making file for companies.
f = open("London Exhibitors.csv","w")
header = "ID, Company Name\n"
f.write(header)

# Looping in Pages.
id = 0
for i in range(1,27):
    d_url = url + str(i)
    site = urlopen(d_url)
    html = site.read()
    site.close()
    soup = bs(html,"html.parser")

    # Making a list has all cards of the page
    containers = soup.find_all("li",{"class":"m-exhibitors-list__items__item"})

    # Getting the page cards and add it to the file.
    for c in containers:
        ctitle = c.find_all("h2", {"class": "m-exhibitors-list__items__item__header__title"})
        company_title = ctitle[0].text.strip()
        print(type(ctitle))
        id = id + 1
        # Add the card to the file in a row.
        f.write(str(id) + "," + company_title + "\n")

        # To ensure that the page is done successfully.
        print("Page", i, "Done")
f.close()