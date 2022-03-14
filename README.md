# python-searchengine

Simple search engine implementation in Python for illustrative purposes to go with [this blog post](https://bart.degoe.de/building-a-full-text-search-engine-150-lines-of-code/).
The corpus of pages contains in directory, file 'posts.csv'.
Run web-service on localhost with Flask.


## Requirements

Python 3.8,3.9

## Usage

Run from the command line:

```bash
$ git clone https://github.com/lag-grunge/python_search_engine/
$ cd $_
$ virtualenv --python=(PATH to python bin e.g. /usr/bin/python3.9) venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python main.py
```
Commands

GET
```browser
http://localhost:5000/?query="<str>"
```

#### Example

![alt text](https://user-images.githubusercontent.com/79085615/158174102-28fd54bb-2df7-4d0b-8aa2-608e4fe8b435.png)

move (next, prev)

![alt text](https://user-images.githubusercontent.com/79085615/158174118-37caef71-d0c0-44e5-aef2-4f004e43ffa6.png)

DELETE
```bash
$ curl --request DELETE http://localhost:5000 -d 'delete=<int>'
```

#### Example

![alt text](https://user-images.githubusercontent.com/79085615/158174112-890df077-1517-4668-bd87-bf06cd7e92e9.png)

![alt text](https://user-images.githubusercontent.com/79085615/158174114-4c72a829-23ff-46c2-8036-170798cbb86a.png)


