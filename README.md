# Flask-BSON

Let your Flask endpoints speak `application/bson`.

A Flask extension that gives you utilities to allow your Flask endpoints to process and respond in the BSON format.

## Installation

You can install the extension with ``pip`` like

```
pip install flask-bson
```

## Usage

The extennsion relies on two pieces of functionality basically. The `accept_bson` view decorator which parses requests into a usable `requests.bson_data` dictionary, and `bsonify` which works a lot like the much-loved `jsonify` -- it turns a dictionary into a valid BSON response.

Here's a full sample implementation:

```
from flask import Flask, request
from flask_bson import accept_bson, bsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
@accept_bson(require_bson = True)
def echobson():
return bsonify(request.bson_data)

if __name__ == '__main__':
app.run(debug=True)
```
