import json
from flask import Flask, request, jsonify
from loadpages import loadpages
from index import indexpages
from index import search

sizequery = 20
sizecorp = 1500
data = loadpages(sizecorp)
index, pages = indexpages(data)
app = Flask(__name__)

@app.route('/', methods=['GET'])
def query_pages():
    print(request.args)
    data = request.args.get('query', str)
    q = json.loads(data)
    it = search(q, index, pages, ranking=False)
    for i in range(sizequery):
        try:
            p = pages[next(it)]
            jsonify({p.id: [p.created_date, p.rubrics, p.text]})
        except StopIteration:
            break
    if i == 0:
        return jsonify({'error': 'data not found'})
    else:
        return jsonify({'score': "{$1} results, query stops".format(i)})

# @app.route('/', methods=['DELETE'])
# def delete_record(index, pages):
#     i = request.data
#     for ind in index:
#

if __name__=='__main__':
    app.run(debug=True)


