# random-quotes
  API which fetches quotes for you :)
#### Dependency

This assumes that you have `Python3` installed and setup.

`pip3` and `python3` is what we need for development purpose.

### How to setup

1. Install `git`.
2. Run the following commands :

```bash
$ git clone git@github.com:Skchoudhary/random-quotes.git
$ cd random-quotes
$ python3 -m venv env
$ source env/bin/activate
$ pip install -r requirement.txt
$ export FLASK_APP=app.py
$ flask run
```

To use the program we need a csv file as data set for quotes to fetch:
```csv
quote,author,tag
"Don't cry because it's over. Smile because it happened.","Dr. Seuss","smile, happy"
```
### API

Once everything is working fine install the postman plugin for your browser. And from that plugin you need to hit the endpoint as:

`localhost:<port>/quote/<tag>`

example: `//127.0.0.1:5000/quote/`