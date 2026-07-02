######################################## VMX ###################################################################
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re
from os import write

f = open("VMX.csv","w",encoding="utf-8")
f.write("ID, Company Name, Category, Country, Email, Phone, Website\n")

# Prepare Browser and Opening website
driver = webdriver.Chrome()
driver.get("https://register.navc.com/conference/2023/exhibitor_list.cfm")

# Wait for website to open
time.sleep(2)

# Trying to close cookies pop-up if found [Accept it]
try:
    consent_button = driver.find_element(By.CSS_SELECTOR, "button#consent-accept")
    consent_button.click()
except:
    pass

# Finds all elements [tag u followed by tag a]
titles = driver.find_elements(By.CSS_SELECTOR, "u a")

# Save the main window
main_window = driver.current_window_handle

# Loop at all titles
id = 1
for title in titles:
    try:
        # Scrolling to the next title [Just for view]
        driver.execute_script("arguments[0].scrollIntoView(true);", title)
        time.sleep(1)

        # Clicking using JavaScript [The most important row code.]
        driver.execute_script("arguments[0].click();", title)

        # Wait for open a new window that clicked
        time.sleep(2)

        # Switch to the window [Important if not written the browser will close and not open the next element]
        new_window = [window for window in driver.window_handles if window != main_window][0]
        driver.switch_to.window(new_window)

        # This POP-UP divided into 4 tables the second table has the data desired.
        tables = driver.find_elements(By.CSS_SELECTOR, " table")
        contact = tables[1].find_elements(By.CSS_SELECTOR, "tr td:first-of-type")

        # Getting Title, Phone, and Website.
        t = contact[0].text.strip().replace(","," ")
        p = contact[1].get_attribute("textContent").strip().replace("Company Phone", "")
        # Website in different tag <a>
        w = tables[1].find_element(By.CSS_SELECTOR,"td a")
        # Extract it from the attribute href then use regular expression to extract url
        utext = w.get_attribute("href")
        website = re.findall(r'https?://[^\s<>"]+|www\.[^\s<>"]+', utext)[0].split(",")[0].strip("'")
        f.write(str(id) + "," + t + "," + "" + "," + "" + "," + "" + "," + p + "," + website+ "\n")
        print(f"ID:{id}, Title: {t}, Phone: {p}, Website: {website} Done.")
        id += 1
        # Wait 5 second before close the new window
        time.sleep(2)

        # Close the new window.
        driver.close()

        # Switch to the main window.
        driver.switch_to.window(main_window)

    # Handling Error.
    except Exception as e:
        print(f"Error Happened: {e}")
        continue

# Close the browser.
driver.quit()
