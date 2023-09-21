import re
from bs4 import BeautifulSoup


def followers_count(driver):
    soup = BeautifulSoup(driver.page_source, "html.parser")
    a = soup.find(
        "a",
        class_="x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _alvs _a6hd",
    )

    followers_count = a.find("span").find("span").text
    followers_count_int = re.findall(r"\d+", followers_count)
    followers_count_int = int("".join(followers_count_int))

    if followers_count[-1] == "K":
        followers_count_int *= 1000
    elif followers_count[-1] == "M":
        followers_count_int *= 1000000

    return followers_count_int
