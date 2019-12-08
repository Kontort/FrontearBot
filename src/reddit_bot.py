import praw

def main():
    reddit = praw.Reddit("RedditBot")
    print("Logged in as %s" % reddit.user.me())

    return 0

if __name__ == "__main__":
    print("Exited with code %d" % main())