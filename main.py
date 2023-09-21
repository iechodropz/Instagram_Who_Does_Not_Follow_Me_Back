from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from go_to_url import go_to_url
from start_web_driver import start_web_driver
from input_credentials import input_credentials
from login import login
from scroll import scroll
from get_usernames import get_usernames
from filter_usernames import filter_usernames
from initial_user_inputs import initial_user_inputs

username, max_followers = initial_user_inputs()
followers_url = f"https://www.instagram.com/{username}/followers/"
following_url = f"https://www.instagram.com/{username}/following/"
login_url = "https://www.instagram.com/accounts/login/"
driver = start_web_driver()
go_to_url(driver, login_url)
username, password = input_credentials()
login(driver, username, password)
go_to_url(driver, followers_url)
followers_popup = driver.find_element(By.XPATH, "//div[@class='_aano']")
scroll(driver, followers_popup)
soup = BeautifulSoup(driver.page_source, "html.parser")
followers = get_usernames(soup)
go_to_url(driver, following_url)
following_popup = driver.find_element(By.XPATH, "//div[@class='_aano']")
scroll(driver, following_popup)
soup = BeautifulSoup(driver.page_source, "html.parser")
following = get_usernames(soup)
usernames = list(following - followers)
filter_usernames(driver, usernames, max_followers)
