from selenium import webdriver
import time


def start_web_driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)
    time.sleep(5)
    return driver
