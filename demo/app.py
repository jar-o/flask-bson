"""
    Demo server showing basic usage of the Flask-BSON extension.
"""
import sys
sys.path.append('..')
from flask import Flask, request
from flask_bson import accept_bson, bsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
@accept_bson(require_bson = True)
def echobson():
    return bsonify(request.bson_data)

if __name__ == '__main__':
    app.run(debug=True)
