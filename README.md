# Learning Space for WebScraping
## by Kim Robinson

#### Technologies used
* Python
* Beautiful Soup Library
* smtp service
* python datetime

#### About
With goals to learn Python and webscraping, I followed this [youtube tutorial](https://www.youtube.com/watch?v=XVv6mJpFOb0) and created directory: scrape_local and scrape_requests.
Hitting roadblocks with trying to scrape recreation.gov and reservations.gov, I focused on creating a simple, Working webscraper to scrape, filter results and send email on a timed interval.

### Setup & Installation
This is just a learning space for me, but if you want to try out the code:
1. Clone to your local computer
2. Install via terminal in your working directory:
```
$ python3 -m pip install
$ pip install beautifulsoup4
$ pip install lxml
$ pip install requests
$ pip install python-dotenv
```
3. For email_test.py & scrape_jobs: Create a .env file in your root directory and make sure your .gitignore has .env already saved and committed to your git history.  Add to your .env file (replacing the values with your own):
```
PW_SMT={YOUR-SENDER-PASSWORD}
SENDER_EMAIL={YOUR-SENDER-EMAIL}
REC_EMAIL={DESIRED-RECEIVER-EMAIL}
```
(I used a gmail app password, which can be created via Manage your google Account>Security>2-step-verification>App passwords)
4. To run the script, `$ python3 <name-of-file>`

#### WIP
scrape_yurts (the response is Not html)

#### License
MIT License, see license.md for more information