FROM maximhq/bifrost:latest

USER root

RUN apk add --no-cache python3

COPY deploy/fly/config.json /app/data/config.json
COPY deploy/fly/entrypoint.sh /app/fly-entrypoint.sh
COPY deploy/fly/parse_database_url.py /app/parse_database_url.py

RUN chmod +x /app/fly-entrypoint.sh /app/parse_database_url.py && \
  chown -R appuser:appuser /app

USER appuser

ENTRYPOINT ["/app/fly-entrypoint.sh"]
CMD ["/app/main"]
