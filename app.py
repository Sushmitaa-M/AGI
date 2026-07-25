import os , re , urllib.parse , urllib.request
from Flask import flask , jsonify , request , Request

app = flask(__name__)
req = urllib.request(f"https://www.youtube.com/search?" methods = (
