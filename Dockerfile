# Decklar | Miguel Lopez | DevOps AI POC

FROM python:3.11-slim

LABEL maintainer="Miguel Lopez"
LABEL project="Decklar DevOps AI POC"
LABEL description="AI-powered system metrics monitoring"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install minimal dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user (security best practice)
RUN useradd -m appuser

WORKDIR /app

# Optimize layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chown -R appuser:appuser /app
USER appuser

EXPOSE 8000

CMD ["python", "main.py"]
