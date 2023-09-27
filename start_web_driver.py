from selenium import webdriver
from time_sleep import time_sleep


def start_web_driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)
    time_sleep()
    return driver
