def initial_user_inputs():
    username = input("Please enter username of account: ")

    max_followers = ""
    while not max_followers.isdigit():
        max_followers = int(
            input(
                "Please specify the maximum number of follower an unverified account can have: "
            )
        )

        if not max_followers.isdigit():
            print("Please enter a valid number for maximum number of followers.")

    return username, max_followers
