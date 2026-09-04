#!/usr/bin/env python3
"""Serveur local de développement : sert dist/ sans cache. Usage : python3 tools/serve.py [port]"""
import http.server
import socketserver
import sys
from pathlib import Path

DIST = Path(__file__).resolve().parents[1] / "dist"
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=str(DIST), **kw)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()


if __name__ == "__main__":
    if not DIST.exists():
        sys.exit("dist/ n'existe pas : lancez « make » d'abord.")
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        httpd.allow_reuse_address = True
        print(f"→ http://localhost:{PORT}/  (Ctrl-C pour arrêter)")
        httpd.serve_forever()
