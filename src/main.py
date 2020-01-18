from praw import Reddit
from praw.models import Comment
from sys import argv
from logging import StreamHandler, getLogger, DEBUG

def setup_logging():
    handler = StreamHandler()
    handler.setLevel(DEBUG)

    logger = getLogger("prawcore")
    logger.setLevel(DEBUG)
    
    logger.addHandler(handler)

def command_help(msg):
    msg.reply(
        "Here's a list of supported commands:"
        "\n\n1. --rand"
        "\n\n"
    )

def command_rand(msg):
    msg.reply(
        "I can't be bothered. Here, the random number is 2"
        "\n\n"
    )

def main():
    reddit = Reddit("FrontearBot")
    print("Logged in as %s" % reddit.user.me())

    for msg in reddit.inbox.unread():
        if not isinstance(msg, Comment):
            continue

        if "u/FrontearBot --" in msg.body:
            msg.mark_read()

            if "help" in msg.body:
                command_help(msg)
            elif "rand" in msg.body:
                command_rand(msg)

    return 0

if __name__ == "__main__":
    setup_logging()
    print("\nExited with code %d" % main())