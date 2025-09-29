from http.server import HTTPServer,BaseHTTPRequestHandler
content='''<html
><h1>placeholder</h1></html>'''
class Myserver(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request recieved...")
        self.send_response(200)
        self.send_header("content-type","text")
