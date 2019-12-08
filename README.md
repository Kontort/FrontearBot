# RedditBot

A simple python wrapper for PRAW, the Reddit API wrapper. This is designed to make it far easier to quickly get a reddit bot working, and have it perform complex tasks with very minimal programming.

## Usage

- Although not required, it's recommended that you create a fresh reddit account, then create an [application](https://www.reddit.com/prefs/apps/)
- Install [PRAW](https://praw.readthedocs.io/en/latest/) via `pip install praw`
- Create an **./info.json**, and populate it according to the following format:

    ```json
    {
        "username": "",
        "password": "",
        "client_id": "",
        "client_secret": "",
        "user_agent": ""
    }
    ```

    Please see this [wiki](https://github.com/Kontort/RedditBot/wiki/Information-about-info.json) post for more information about this file

## License

This project is licensed under the [GNU General Public License v3](https://tldrlegal.com/license/gnu-general-public-license-v3-(gpl-3)) &#8212; you may copy, distribute and modify the software as long as you track changes/dates in source files.
