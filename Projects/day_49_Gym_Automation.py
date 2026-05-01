import time

import ec
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

# Add your credentials at the top of your script
ACCOUNT_EMAIL = "silverguard@test.com"  # The email you registered with
ACCOUNT_PASSWORD = "password123"      # The password you used during registration
GYM_URL = "https://appbrewery.github.io/gym/"


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://appbrewery.github.io/gym/")

#Store Chrome profile info
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver.find_element(By.ID, "login-button").click()
driver.find_element(By.ID, "email-input").send_keys(f"{ACCOUNT_EMAIL}")
driver.find_element(By.ID, "password-input").send_keys(f"{ACCOUNT_PASSWORD}")
driver.find_element(By.ID, "submit-button").click()

time.sleep(5)

booking = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")

booked_counter = 0
waitlist_counter = 0
already_done_counter = 0
tues_6pm_counter = 0
new_booking = ""
new_waitlist = ""

for booking in booking:
    day_group = booking.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
    day_title = day_group.find_element(By.TAG_NAME, "h2").text

    if "Tue" or "Thu" in day_title:
        time_text = booking.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text
        if "6:00 PM" in time_text:
            class_name = booking.find_element(By.CSS_SELECTOR, "h3[id^='class-name-']").text

            button = booking.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")
            button.click()

            if button.text == "Booked":
                print(f"Already booked: {class_name} on {day_title}")
                already_done_counter += 1
            elif button.text == "Waitlisted":
                print(f"Already on waitlist: {class_name} on {day_title}")
                already_done_counter += 1
            elif button.text == "Book Class":
                button.click()
                print(f"Successfully booked: {class_name} on {day_title}")
                booked_counter += 1
                new_booking = time_text
            elif button.text == "Join Waitlist":
                button.click()
                print(f"Joined waitlist for: {class_name} on {day_title}")
                waitlist_counter += 1
                new_waitlist = time_text
            tues_6pm_counter += 1
            break

print("--- BOOKING SUMMARY ---")
print(f"Classes booked: {booked_counter}")
print(f"Waitlisted: {waitlist_counter}")
print(f"Already on waitlist/booked: {already_done_counter}")
print(f"Total classes: {tues_6pm_counter}")
print(f"[New Booking]: {new_booking}")
print(f"[New Waitlist]: {new_waitlist}")

total_booked = already_done_counter + booked_counter + waitlist_counter
print(f"\n--- Total Tuesday/Thursday 6pm classes: {total_booked} ---")
print("\n--- VERIFYING ON MY BOOKINGS PAGE ---")

my_bookings_link = driver.find_element(By.ID, "my-bookings-link")
my_bookings_link.click()

os.wait.until(ec.presence_of_element_located((By.ID, "my-bookings-page")))

verified_count = 0

all_bookings = driver.find_elements(By.CSS_SELECTOR, "div[id*='card-']")

for booking in all_bookings:
    try:
        when_paragraph = booking.find_element(By.XPATH, ".//p[strong[text()='When:']]")
        when_text = when_paragraph.text

        if ("Tue" in when_text or "Thu" in when_text) and "6:00 PM" in when_text:
            class_name = booking.find_element(By.TAG_NAME, "h3").text
            print(f"Verified: {class_name}")
            verified_count += 1
    except NoSuchElementException:
        pass

print(f"\n--- VERIFICATION RESULT ---")
print(f"Expected: {total_booked} bookings")
print(f"Found: {verified_count} bookings")

if total_booked == verified_count:
    print("SUCCESS: All bookings verified!")
else:
    print(f"MISMATCH: Missing {total_booked - verified_count} bookings")

