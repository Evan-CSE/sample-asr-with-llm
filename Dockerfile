FROM python:3.12
WORKDIR /usr/local/app

RUN apt-get update && apt-get install -y \
    ffmpeg \
    portaudio19-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
COPY src ./src/
COPY run.py ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir uvicorn[standard]


EXPOSE 8080


CMD ["python", "run.py"]