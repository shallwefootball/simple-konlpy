
from http.server import BaseHTTPRequestHandler
import json
from urllib.parse import parse_qs
from konlpy.tag import Kkma

kkma = Kkma()

class handler(BaseHTTPRequestHandler):

    def do_POST(self):

        data_string = self.rfile.read(int(self.headers['Content-Length'])).decode('utf-8')
        pq = parse_qs(data_string)
        search_query = pq['query'][0]

        kol = kkma.pos(search_query,True,True)
        res_kol = json.dumps(kol, ensure_ascii=False)
        
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        
        self.wfile.write(res_kol.encode())

        return