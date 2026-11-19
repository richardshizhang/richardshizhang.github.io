"""Serve the site at http://localhost:8642 the way GitHub Pages does, byte ranges included.

Python's built-in `http.server` ignores Range requests, so browsers treat the music as unseekable
and the player can't skip ahead or back. This is that server plus ranges, nothing else.

    python3 tools/serve.py          # or: python3 tools/serve.py 9000
"""
import os
import re
import sys
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8642


class Handler(SimpleHTTPRequestHandler):
    def send_head(self):
        self.remaining = None
        match = re.fullmatch(r"bytes=(\d*)-(\d*)", self.headers.get("Range", "").strip())
        path = self.translate_path(self.path)
        if not match or not any(match.groups()) or not os.path.isfile(path):
            return super().send_head()
        size = os.path.getsize(path)
        first, last = match.groups()
        if first:
            start, end = int(first), min(int(last) if last else size - 1, size - 1)
        else:  # "bytes=-500" means the last 500 bytes
            start, end = max(size - int(last), 0), size - 1
        if start > end:
            self.send_response(416)
            self.send_header("Content-Range", f"bytes */{size}")
            self.send_header("Content-Length", "0")
            self.end_headers()
            return None
        f = open(path, "rb")
        f.seek(start)
        self.send_response(206)
        self.send_header("Content-Type", self.guess_type(path))
        self.send_header("Content-Range", f"bytes {start}-{end}/{size}")
        self.send_header("Content-Length", str(end - start + 1))
        self.end_headers()
        self.remaining = end - start + 1
        return f

    def copyfile(self, source, outputfile):
        if self.remaining is None:
            return super().copyfile(source, outputfile)
        while self.remaining > 0:
            chunk = source.read(min(64 * 1024, self.remaining))
            if not chunk:
                break
            outputfile.write(chunk)
            self.remaining -= len(chunk)

    def end_headers(self):
        self.send_header("Accept-Ranges", "bytes")
        super().end_headers()


if __name__ == "__main__":
    server = ThreadingHTTPServer(("127.0.0.1", PORT), partial(Handler, directory=ROOT))
    print(f"Serving {ROOT} at http://localhost:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
