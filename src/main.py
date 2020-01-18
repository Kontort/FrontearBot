import praw
from praw.models import Comment
import logging

DEBUG = False # if you wish to log at the debugging level. This shouldn't ideally be active unless necessary

def main():
    reddit = praw.Reddit("FrontearBot")
    print("Logged in as %s" % reddit.user.me())

    for msg in reddit.inbox.unread():
        if not isinstance(msg, Comment):
            continue

        if msg.body == "u/FrontearBot --help" or msg.body == "u/Frontear \\--help": # the backslash is added by the new website format thing. what even...
            msg.mark_read()
            msg.reply("This is a valid call!")

    return 0

if __name__ == "__main__":
    if DEBUG:
        handler = logging.StreamHandler()
        handler.setLevel(logging.DEBUG)

        logger = logging.getLogger("prawcore")
        logger.setLevel(logging.DEBUG)
    
        logger.addHandler(handler)

    print("\nExited with code %d" % main())