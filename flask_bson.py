from werkzeug.wrappers import Response
from flask import request
from functools import wraps
import bson

def accept_bson(require_bson = False, stream_at=1048576*5):
    def decorator(func):
        @wraps(func)
        def decorated(*args, **kwargs):
            contype = request.headers.get('content-type').lower()
            if contype == 'application/bson':
                import sys
                try:
                    if request.content_length > stream_at:
                        chunk_size = 4096
                        data = []
                        while True:
                            chunk = request.stream.read(chunk_size)
                            if len(chunk) == 0: break
                            data.append(chunk)
                        request.bson_data = bson.loads(''.join(data))
                    else:
                        request.bson_data = bson.loads(request.get_data())
                except Exception, e:
                    return ('Error, request: ' + str(e), 400)
            elif require_bson and contype != 'application/bson':
                return ("Error, request: must supply BSON content and set "
                        "Content-Type: application/bson", 400)
            return func(*args, **kwargs)
        return decorated
    return decorator

def bsonify(obj):
    try:
        return Response(bson.dumps(obj), mimetype='application/bson')
    except Exception, e:
        return ('Error, bsonify: ' + str(e), 400)



