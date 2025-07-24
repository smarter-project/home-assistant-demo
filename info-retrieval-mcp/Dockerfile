# ──────────────────────────────── 1️⃣ build stage ────────────────────────────────
FROM python:3.12-slim-bookworm AS builder

WORKDIR /app

# Copy only dependency manifests first (leverages Docker cache)
COPY pyproject.toml .
COPY README.md .

# Install uv + poetry-core globally
RUN python -m pip install --upgrade pip && \
    python -m pip install uv poetry-core

# Copy source code
COPY src/ ./src/

# Vendor all deps + your package into /install
RUN uv pip install --prefix=/install \
    "mcp[cli]" gunicorn[uvicorn] paho-mqtt && \
    uv pip install --prefix=/install .

# ──────────────────────────────── 2️⃣ runtime stage ──────────────────────────────
FROM python:3.12-slim-bookworm AS runtime

WORKDIR /app

# Copy python environment from builder
COPY --from=builder /install /usr/local/

# Copy source code
COPY src/ ./src/
COPY README.md .
COPY initial_sensor_status.json .

# Ensure the package is importable
ENV PYTHONPATH=/app/src

# ──────────────────────────────── entrypoint ─────────────────────────────────────
EXPOSE 7001
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-w", "1", "-b", "0.0.0.0:7001", "info_retrieval_mcp.asgi:app"] 