# syntax=docker/dockerfile:1

FROM python:3.14-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py views.py ./
COPY static ./static
COPY templates ./templates

RUN useradd --system --uid 10001 --no-create-home appuser
USER appuser

# PORT: port the service listens on
# TRUSTED_PROXY_HOPS: number of reverse proxies in front of the app to trust X-Forwarded-* from
ENV PORT=8080 \
    TRUSTED_PROXY_HOPS=0 \
    WEB_CONCURRENCY=2
EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD python -c "import os, urllib.request; urllib.request.urlopen(f'http://127.0.0.1:{os.environ.get(\"PORT\", \"8080\")}/decent', timeout=2)" || exit 1

# Shell form so ${PORT} is expanded; exec so gunicorn is PID 1 and receives signals
CMD exec gunicorn --bind "0.0.0.0:${PORT}" --workers "${WEB_CONCURRENCY}" --access-logfile - app:app
