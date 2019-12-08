import json
import praw

def main():
    with open("info.json", "r") as i:
        info = json.loads(i.read())
        bot = praw.Reddit(
            username=info["username"],
            password=info["password"],
            client_id=info["client_id"],
            client_secret=info["client_secret"],
            user_agent=info["user_agent"]
        )

        print("Logged in as %s" % bot.user.me())

    return 0

if __name__ == "__main__":
    print("Exited with code %d" % main())