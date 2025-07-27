
# Dockerfile for Cloud Manager CLI
FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "cloud_manager_cli.py"]
