from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://appbrewery.github.io/instant_pot/")

driver2 = webdriver.Chrome(options=chrome_options)
driver2.get("https://python.org")

price_dollar = driver.find_element(By.CLASS_NAME, "a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME, "a-price-fraction")

print(f"Price: {price_dollar.text}.{price_cents.text}")

search_bar = driver2.find_element(By.NAME, "q")
print(search_bar.get_attribute("placeholder"))

button = driver.find_element(By.ID, value="submit")
print(button.size)

documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
print(documentation_link.text)

bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)

event_times = driver.find_element(By.CSS_SELECTOR, ".event_widget time")
event_names = driver.find_element(By.CSS_SELECTOR, ".event_widget a")
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }
print(events)

driver3 = webdriver.Chrome(options=chrome_options)
driver3.get("https://wikipedia.org")
article_count = driver3.find_element(By.CSS_SELECTOR, "#articlecount a")
print(article_count.text)

search = driver3.find_element(By.NAME, "search")
search.send_keys("Python", Keys.ENTER)








# driver.close()
driver.quit()




