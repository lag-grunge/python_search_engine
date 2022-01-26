# python-searchengine

Simple search engine implementation in Python for illustrative purposes to go with [this blog post](https://bart.degoe.de/building-a-full-text-search-engine-150-lines-of-code/).
The corpus of pages contains in directory, file 'posts.csv'.
Run web-service on localhost with Flask.


## Requirements

Python 3.9

## Usage

Run from the command line:

```bash
$ pip install -r requirements.txt
$ python main.py
```
Commands

GET
```browser
http://localhost:5000/?query="<str>"
```
DELETE
```bash
$ curl --request DELETE http://localhost:5000 -d 'delete=<int>'
```
