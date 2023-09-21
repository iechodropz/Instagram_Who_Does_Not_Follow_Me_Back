from getpass import getpass


def input_credentials():
    username = input("Enter Username: ")
    password = getpass("Enter Password: ")
    return username, password
