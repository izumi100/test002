from flask import Flask, request, jsonify

app = Flask(__name__)

# 仮のデータベース
data = [
    {'id': 1, 'title': 'Pythonについての基本情報'},
    {'id': 2, 'title': 'JavaScriptの入門'},
    {'id': 3, 'title': 'HTMLとCSSのガイド'},
    {'id': 4, 'title': 'FlaskでのWeb開発'}
]

@app.route('/search')
def search():
    query = request.args.get('query', '')
    results = [item for item in data if query.lower() in item['title'].lower()]
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
