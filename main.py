from flask import Flask, jsonify
from flask_restful import reqparse
from loadpages import loadpages
from index import indexpages
from index import search

sizequery = 20
sizecorp = 1500
data = loadpages(sizecorp)
index, pages = indexpages(data)
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
parser = reqparse.RequestParser()
parser.add_argument('query')
parser.add_argument('delete', type=int)


@app.route('/', methods=['GET'])
def query_pages():
    args = parser.parse_args()
    data = args['query']
    if not data:
        return default_help()
    res = search(data, index, pages, ranking=False)
    if len(res) == 0:
        return jsonify({'error': 'data not found'})
    elif len(res) > 0:
        res_t = {str(res[p]):str(pages[res[p]]) for p in range(min(sizequery, len(res)))}
        res_t['score'] = "{0} results, {1} output, query stops".format(len(res), len(res_t))
        return res_t


@app.route('/', methods=['DELETE'])
def delete_page():
    args = parser.parse_args()
    data = args['delete']
    if not data:
        return jsonify({'result':'not data to delete'})
    for ind in index:
        if data in index[ind]:
            index[ind].remove(data)
    del_page = pages.pop(data)
    res_t = {'deleted':str(del_page)}
    res_t['result'] = "id {0} page deleted".format(data)
    return jsonify(res_t)

def default_help():
    with open('docs.json', 'r') as f:
        return f.read()

if __name__=='__main__':
    app.run(debug=False)




