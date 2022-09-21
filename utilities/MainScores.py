from flask import Flask

app = Flask(__name__)


@app.route('/scores')
def content():
    f = open("scoresPage.html", "r")
    file = f.read()
    f.close()
    return file, 200


@app.route('/list', methods=['GET'])
def endpoint():
    f = open('scores.json', 'r')
    return f.read()


app.run(port=4000)
