# python-searchengine

Simple search engine implementation in Python for illustrative purposes to go with [this blog post](https://bart.degoe.de/building-a-full-text-search-engine-150-lines-of-code/).
The corpus of pages contains in directory, file 'posts.csv'.
Run web-service on localhost with Flask.


## Requirements

Python 3.6-3.9

## Usage

Run from the command line:

```bash
$ virtualenv --python=(PATH to python bin e.g. /usr/bin/python3.9) venv
$ pip install -r requirements.txt
$ python main.py
```
Commands

GET
```browser
http://localhost:5000/?query="<str>"
```
####Example

![alt text](https://github.com/lag-grunge/pythontest/blob/master/query_example.png?raw=true)

####move (next, prev)

![alt text](https://github.com/lag-grunge/pythontest/blob/master/move_next_prev.png?raw=true)

DELETE
```bash
$ curl --request DELETE http://localhost:5000 -d 'delete=<int>'
```
####Example

![alt text](https://github.com/lag-grunge/pythontest/blob/master/delete_example.png?raw=true)

![alt text](https://github.com/lag-grunge/pythontest/blob/master/query_afre.png?raw=true)


