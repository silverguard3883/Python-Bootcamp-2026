from bs4 import BeautifulSoup
import requests
import smtplib


URL = "https://appbrewery.github.io/instant_pot/"
SMTP_SERVER = "smtp.gmail.com"
EMAIL_ADDRESS = "example@gmail.com"
EMAIL_PASSWORD = "ASecurePassword123456"
BUY_PRICE = 75.00

headers = {
    "User-Agent": "CCBot/2.0 (https://commoncrawl.org/faq/)",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "If-Modified-Since": "Sun, 21 Apr 2024 20:38:18 GMT",
    "Accept-Encoding": "br,gzip",
    "Host": "myhttpheader.com",
    "x-forwarded-proto": "https",
    "x-https": "on",
    "X-Forwarded-For": "3.230.154.90"
}


response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

price_text = soup.find("span", class_="aok-offscreen").text
price = float(price_text.replace("$", ""))

"""Get product info"""
product_name = soup.find(id="productTitle").text.strip()
print(product_name)


if price < BUY_PRICE:
    message = f"{product_name} is on sale for less than {BUY_PRICE}%"

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    connection.sendmail(
        from_addr=EMAIL_ADDRESS,
        to_addrs=EMAIL_ADDRESS,
        msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
    )


