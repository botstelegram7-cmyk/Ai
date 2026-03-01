# ── Base Image ────────────────────────────────────────────────────────────────
FROM python:3.11-slim

# ── Working Directory ─────────────────────────────────────────────────────────
WORKDIR /app

# ── System deps ───────────────────────────────────────────────────────────────
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc curl && \
    rm -rf /var/lib/apt/lists/*

# ── Python Dependencies ───────────────────────────────────────────────────────
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ── Copy Source ───────────────────────────────────────────────────────────────
COPY . .

# ── Environment Variables (placeholder, .env se override hoga) ───────────────
ENV BOT_TOKEN=""
ENV GROK_API_KEY=""
ENV OWNER_USERNAME="xuoqui_xin"
ENV GROK_MODEL="grok-3-latest"
ENV PORT=5000

# ── Port Expose ───────────────────────────────────────────────────────────────
EXPOSE 5000

# ── Health Check ──────────────────────────────────────────────────────────────
HEALTHCHECK --interval=30s --timeout=10s --start-period=10s --retries=3 \
    CMD curl -f http://localhost:5000/health || exit 1

# ── Start Command ─────────────────────────────────────────────────────────────
CMD ["python", "main.py"]
