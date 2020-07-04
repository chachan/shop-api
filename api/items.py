import os
import json

from pymongo import MongoClient

from http.server import BaseHTTPRequestHandler

def connect_to_db():
    client = MongoClient(os.environ.get('MONGODB_URL'))

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        message = {'message': 'OK'}
        self.wfile.write(message.encode(message))
        return
