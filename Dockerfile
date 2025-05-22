FROM python:3.11

WORKDIR /app
COPY . .

RUN apt-get update && apt-get install -y \
    gcc \
    libpython3-dev \
    libssl-dev \
    libffi-dev \
    make \
    curl \
    unzip && \
    pip install --no-cache-dir -r requirements.txt

EXPOSE 5001
CMD ["python", "app.py"]
