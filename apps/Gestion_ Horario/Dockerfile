FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# ESTA ES LA LÍNEA QUE LO ARREGLA TODO PARA SIEMPRE
ENV PYTHONPATH=/app

# Arrancamos con el módulo directo (así nunca falla el import)
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]