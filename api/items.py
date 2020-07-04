import json

from pymongo import MongoClient

from http.server import BaseHTTPRequestHandler

def connect_to_db():
    client = MongoClient(f'mongodb+srv://telescoped:{password}>@cluster0-oe3qq.mongodb.net/{dbname}?retryWrites=true&w=majority')

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        message = {'message': 'OK'}
        self.wfile.write(message.encode(message))
        return
