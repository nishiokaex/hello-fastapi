from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # URLパースしてルーティング
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        query = parse_qs(parsed_path.query)
        
        # ルーティング処理
        if path == "/":
            response = {"message": "Hello World from Vercel!"}
        elif path == "/health":
            response = {"status": "healthy"}
        elif path == "/hello":
            response = {"message": "Hello from FastAPI API!"}
        elif path.startswith("/hello/"):
            name = path.split("/hello/")[1]
            response = {"message": f"Hello {name}!"}
        else:
            response = {"error": "Not Found"}
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())
            return
        
        # レスポンス送信
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())