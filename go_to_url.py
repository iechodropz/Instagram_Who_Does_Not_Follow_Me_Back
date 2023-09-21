import time


def go_to_url(driver, url):
    driver.get(url)
    time.sleep(5)
