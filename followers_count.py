import re
from bs4 import BeautifulSoup


def followers_count(driver):
    soup = BeautifulSoup(driver.page_source, "html.parser")
    span = soup.find_all(
        "span",
        class_="html-span xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1hl2dhg x16tdsg8 x1vvkbs",
    )

    span = span[1]
    followers_count = span.text
    followers_count_int = re.findall(r"\d+", followers_count)
    followers_count_int = int("".join(followers_count_int))

    if followers_count[-1] == "K":
        followers_count_int *= 1000
    elif followers_count[-1] == "M":
        followers_count_int *= 1000000

    return followers_count_int
