# coding:utf-8
import unittest

import array, random
from struct import *
from flask import Flask, request
from flask_bson import accept_bson, bsonify
import bson

app = Flask(__name__)

@app.route('/', methods=['POST'])
@accept_bson(require_bson = True)
def echobson():
    return bsonify(request.bson_data)


class BasicTestCase(unittest.TestCase):

    def setUp(self):
        self.cli = app.test_client()

    def test_basic(self):
        testdata = bson.dumps({ 'helo':'world', 'array':[1,2,3,4] })
        assert self.cli.post(
                '/',
                data = testdata,
                headers = { 'Content-Type': 'application/bson' }
            ).get_data() == testdata

    def test_binary(self):
        testdata = bson.dumps({
            'helo':'world', 'array':[1,2,3,4],
            'bin': array.array('B', [random.randrange(255) for x in range(100)]).tostring()
            })
        assert self.cli.post(
                '/',
                data = testdata,
                headers = { 'Content-Type': 'application/bson' }
            ).get_data() == testdata

    def test_non_bson(self):
        assert self.cli.post(
                '/',
                data = 'just a plain string',
                headers = { 'Content-Type': 'application/bson' }
            ).get_data().startswith('Error, request:')

    def test_missing_header(self):
        testdata = bson.dumps({ 'helo':'world', 'array':[1,2,3,4] })
        assert self.cli.post(
                '/',
                data = testdata,
            ).get_data().startswith('Error, request: must supply BSON content')

if __name__ == '__main__':
    unittest.main()
