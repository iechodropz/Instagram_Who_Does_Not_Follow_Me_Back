from time_sleep import time_sleep


def go_to_url(driver, url):
    driver.get(url)
    time_sleep()
