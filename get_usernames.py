def get_usernames(soup):
    divs = soup.find_all(
        "div",
        class_="x9f619 xjbqb8w x1rg5ohu x168nmei x13lgxp2 x5pf9jr xo71vjh x1uhb9sk x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1",
    )

    usernames = set()
    for div in divs:
        if div.find("title"):
            continue

        usernames.add(
            div.find("span", class_="_aacl _aaco _aacw _aacx _aad7 _aade").text
        )

    return usernames
