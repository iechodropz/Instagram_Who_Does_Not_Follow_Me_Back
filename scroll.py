import time


def scroll(driver, element):
    while True:
        current_height = driver.execute_script(
            "return arguments[0].scrollHeight;", element
        )
        driver.execute_script(
            "arguments[0].scrollTop += arguments[0].scrollHeight - arguments[0].scrollTop;",
            element,
        )

        time.sleep(3)

        new_height = driver.execute_script("return arguments[0].scrollHeight;", element)

        if new_height == current_height:
            break
