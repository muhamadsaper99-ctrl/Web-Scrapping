####################################### Scrapping BSAVA Congress ################################
from os import write
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import time

# File Creation.
f = open("Bsava Congress.csv","w",encoding="utf-8")
f.write("ID, Company Name, Category, Country, Email, Phone, Website\n")

# Set up the WebDriver (make sure the path to the driver is correct)
driver = webdriver.Chrome()

# Open the website
driver.get('https://www.bsavacongress.com/exhibitor-list')

# Wait for the page to load
time.sleep(5)

# Find all the company cards
company_cards = driver.find_elements(By.CLASS_NAME, 'm-exhibitors-list__items__item')
# Loop through each company card

page_source= driver.page_source
bsoup = BeautifulSoup(page_source, 'html.parser')
container = bsoup.find_all("li",{"class","m-exhibitors-list__items__item"})
id = 0
for i,card in zip(container,company_cards):
    t = i.find_all("h2")
    title = t[0].text.strip()
    e = i.find_all("div", {"class", "m-exhibitor-entry__item__body__additional__item"})
    # print( e)
    id += 1
    # Click on the card to open the pop-up
    ActionChains(driver).move_to_element(card).click(card).perform()

    # Wait for the pop-up to load
    time.sleep(2)

    # Get the page source and parse it with BeautifulSoup
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    # Extract the email, phone, and website
    company_info = soup.find_all('div', class_='m-exhibitor-entry__item__body')
    for i in company_info:
        contact = i.find_all('div', class_='m-exhibitor-entry__item__body__additional__item__value')
        w = i.find_all('a',class_="button")
        if len(w) == 1:
            website = w[0].attrs["href"]
        else: website = ""
        if len(contact) == 1:
            email = contact[0].text.strip()
            print("title:",title,"email:", email,"phone:","","website:",website)
            f.write(str(id) + "," + title + "," + "" + "," + "" + "," + email + "," + "" + "," + website + "\n")
            continue

        elif len(contact) == 2:
            email = contact[0].text.strip()
            phone = contact[1].text.strip()
            print("title:",title,"email:", email, "Phone: ", phone,"website:",website)
            f.write(str(id) + "," + title + "," + "" + "," + "" + "," + email + "," + phone + "," + website + "\n")
            continue


        else:
            email = ""
            phone = ""
            print("title:",title,"email:", email, "Phone: ", phone,"Website:",website)
            f.write(str(id) + "," + title + "," + "" + "," + "" + "," + email + "," + phone + "," + website + "\n")
            continue


    # Close the pop-up
    close_button = driver.find_element(By.CLASS_NAME, 'mfp-close')
    close_button.click()

    # Wait for the pop-up to close
    time.sleep(1)

# Close the WebDriver
driver.quit()