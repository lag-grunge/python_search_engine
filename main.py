from flask import jsonify, render_template
from flask_restful import reqparse
from index import Index
from loadpages import loadpages
from app import app
from query import Query

sizecorp = 1500
loadpgs = loadpages(sizecorp)
index = Index(loadpgs)
query = None

parser = reqparse.RequestParser()
parser.add_argument('query')
parser.add_argument('move')
parser.add_argument('delete', type=int)

@app.route('/', methods=['GET'])
def show_query():
    global query, index
    if not index.loadpgs:
        return jsonify({"error": "no pages"})
    args = parser.parse_args()
    q = args['query']
    if not q:
        return jsonify({"error": "no query"})
    if not query or query.query != q:
        query = Query(q, index)
    if query is None or query.res is None:
        return jsonify({"error": "no results"})
    move = args['move']
    query.set_show_params(move)
    return render_template('new.html', query=query)


@app.route('/', methods=['DELETE'])
def delete_page():
    args = parser.parse_args()
    data = args['delete']
    if not data:
        return jsonify({'result': 'not data to delete'})
    for ind in index.index:
        if data in index.index[ind]:
            index.index[ind].remove(data)
    del_page = index.pages.pop(data)
    res_t = {'deleted': str(del_page)}
    res_t['result'] = "id {0} page deleted".format(data)
    return jsonify(res_t)


if __name__ == '__main__':
    app.run(debug=False)
