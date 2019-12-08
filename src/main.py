import praw
import logging

def main():
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)

    logger = logging.getLogger("prawcore")
    logger.setLevel(logging.DEBUG)
    
    logger.addHandler(handler)

    reddit = praw.Reddit("FrontearBot")
    print("Logged in as %s" % reddit.user.me())

    return 0

if __name__ == "__main__":
    ret = main()
    print("\nExited with code %d" % ret)