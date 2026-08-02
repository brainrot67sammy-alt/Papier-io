#!/usr/bin/env python3
"""Prosty lokalny serwer do Territorial IO.
Uruchom: python3 server.py
Potem otwórz: http://localhost:8000/territorial-io.html
"""
from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

PORT = 8000
DIR = os.path.dirname(os.path.abspath(__file__)) or "."
os.chdir(DIR)

print(f"Folder:  {DIR}")
print(f"Serwer:  http://localhost:{PORT}/territorial-io.html")
print("Zatrzymaj: Ctrl+C")
HTTPServer(("", PORT), SimpleHTTPRequestHandler).serve_forever()
