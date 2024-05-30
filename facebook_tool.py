from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.driver import ChromeDriverManager
import requests

# ফেসবুক অ্যাকাউন্টের তথ্য
accounts = [
    {"email": "example1@gmail.com", "password": "password1"},
    {"email": "example2@gmail.com", "password": "password2"},
    {"email": "example3@gmail.com", "password": "password3"},
]

# ওয়েবড্রাইভার সেটআপ করুন
driver = ChromeDriverManager().install()

# নির্দিষ্ট পোস্টের URL
post_url = "https://www.facebook.com/123456789012345/posts/1234567890123456"

# প্রতিটি অ্যাকাউন্টের জন্য লগ ইন করুন এবং পোস্টে লাইক করুন
for account in accounts:
    driver.get("https://www.facebook.com/")

    # ইমেল এবং পাসওয়ার্ড ইনপুট ফিল্ডগুলি খুঁজুন এবং পূরণ করুন
    email_field = driver.find_element_by_id("email")
    password_field = driver.find_element_by_id("pass")
    email_field.send_keys(account["email"])
    password_field.send_keys(account["password"])

    # লগ ইন বোতামে ক্লিক করুন
    login_button = driver.find_element_by_id("u_fb_login_button")
    login_button.click()

    # পোস্টে যান
    driver.get(post_url)

    # লাইক বোতামে ক্লিক করুন
    like_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Like']")))
    like_button.click()

    # অ্যাকাউন্ট থেকে লগ আউট করুন
    driver.get("https://www.facebook.com/logout/")

# ওয়েবড্রাইভার বন্ধ করুন
driver.quit()
