FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ .
EXPOSE 5000
RUN adduser --disabled-password --gecos '' appuser && chown -R appuser /app
USER appuser
CMD ["python", "app.py"]
