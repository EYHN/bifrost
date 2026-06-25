#!/usr/bin/env python3
import shlex
import sys
from urllib.parse import parse_qs, unquote, urlparse

if len(sys.argv) != 2:
    raise SystemExit("usage: parse_database_url.py <postgres-url>")

url = urlparse(sys.argv[1])
query = parse_qs(url.query)

values = {
    "PG_HOST": url.hostname or "",
    "PG_PORT": str(url.port or 5432),
    "PG_USER": unquote(url.username or ""),
    "PG_PASSWORD": unquote(url.password or ""),
    "PG_DB_NAME": (url.path or "/bifrost").lstrip("/") or "bifrost",
    "PG_SSL_MODE": query.get("sslmode", ["require"])[0] or "require",
}

for key, value in values.items():
    if value:
        print(f"export {key}={shlex.quote(value)}")
