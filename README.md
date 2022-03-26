# Instagram Post/Photo Downloader

# Prerequisites
    
    - Instagram Account
    - Python 3.9+ (compiler)
    - Virtualenv (for installation dependencies)
    - .env file (for storing credentials)

### Getting Started

    - Create virtualenv
        $ python3 -m venv {`your_virtualenv_name`} (Recommended)
        $ py -m venv {`your_virtualenv_name`} (it works for me on Windows)
        $ virtualenv {`your_virtualenv_name`} (it works for me on windows)
    - Activate virtualenv
        $ source {`your_virtualenv_name`}/bin/activate (for linux, macOs)
        $ ./{`your_virtualenv_name`}/Scripts/activate (for windows)
    - Install dependencies
         You need to activate virtualenv before running this command
        $ pip install -r requirements.txt
    - Run the script
        $ python3 ig.py (Recommended)
        $ python ig.py (Recommended)
        $ py ig.py (it works for me on Windows)

# Getting The Post Url From Instagram (including shortcode)

    - Go to your Instagram post
![Default Home View](screenshots/instagram.png?raw=true "Title")

    - Select the post that you're desired
    - Here I chose the post that I want to download
    - You would see the post url in the address bar and the post shortcode in the url (`p/CbjNrvTPtOY/`) ["p" stands for post, "CbjNrvTPtOY" is the shortcode]
![Default Home View](screenshots/gettingshortcode.png?raw=true "Title")

    -So, next step you need to copy the account name and add between `.com/{`account_name that you copied`}/p/CbjNrvTPtOY/`.
    -You will get the post url like this `https://www.instagram.com/roses_are_rosie/p/CbjNrvTPtOY/` (for example)
![Default Home View](screenshots/postwithshortcode.png?raw=true "Title")

    - Now you can use that url to download the post when the script is running.
