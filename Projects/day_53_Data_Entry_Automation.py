from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

GOOGLE_FORM_LINK = "https://docs.google.com/forms/d/e/1FAIpQLSeUhkPkOhecyaExeUYzDdnAUPTCq6aVErW_huM4sxEk-Jnn6g/viewform?usp=header"
ZILLOW_LINK = "https://appbrewery.github.io/Zillow-Clone/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)

response = requests.get(ZILLOW_LINK)
soup = BeautifulSoup(response.text, "html.parser")

listings = soup.select("li[class*='ListItem']")

listing_links = []
listing_price = []
listing_address = []

for listing in listings:
    link_tag = listing.select_one("a[data-test='property-card-link']")
    link = link_tag["href"] if link_tag else "N/A"
    listing_links.append(link)

    price_tag = listing.select_one("span[data-test='property-card-price']")
    price = price_tag.get_text(strip=True) if price_tag else "N/A"
    price = price.replace("+/mo", "").replace("/mo", "").strip()
    listing_price.append(price)

    address_tag = listing.select_one("address")
    address = address_tag.get_text(strip=True) if address_tag else "N/A"
    address = address.replace("|", "").replace("\n", "").strip()
    listing_address.append(address)

for address, price, link in zip(listing_address, listing_price, listing_links):
    driver.get(GOOGLE_FORM_LINK)

    form_address = wait.until(
        ec.element_to_be_clickable(
            (By.XPATH, "/html/body/div/div[3]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
        )
    )
    form_address.send_keys(address)

    form_price = wait.until(
        ec.element_to_be_clickable(
            (By.XPATH, "/html/body/div/div[3]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
        )
    )
    form_price.send_keys(price)

    form_link = wait.until(
        ec.element_to_be_clickable(
            (By.XPATH, "/html/body/div/div[3]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
        )
    )
    form_link.send_keys(link)

    submit_button = wait.until(
        ec.element_to_be_clickable(
            (By.XPATH, "//span[text()='Submit']")
        )
    )
    submit_button.click()

print(listing_links)
print(listing_price)
print(listing_address)



