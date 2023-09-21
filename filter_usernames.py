from go_to_url import go_to_url
from followers_count import followers_count


def filter_usernames(driver, usernames, max_followers=10_000):
    i = 0
    for username in usernames:
        url = f"https://www.instagram.com/{username}/"
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[i + 1])
        go_to_url(driver, url)
        num_followers = followers_count(driver)

        if num_followers >= max_followers:
            driver.close()
            driver.switch_to.window(driver.window_handles[i])
        else:
            i += 1
