#!/bin/sh
set -e

if [ -n "$DATABASE_URL" ]; then
  eval "$(python3 /app/parse_database_url.py "$DATABASE_URL")"
fi

exec /app/docker-entrypoint.sh "$@"
