import json
import praw

def main():
    bot = praw.Reddit("RedditBot")
    print("Logged in as %s" % bot.user.me())

    return 0

if __name__ == "__main__":
    print("Exited with code %d" % main())