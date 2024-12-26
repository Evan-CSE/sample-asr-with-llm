FROM python:3.12
WORKDIR /usr/local/app

COPY src ./
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 8080


CMD ["uvicorn", "CommandRequestHandler:app", "--host", "0.0.0.0", "--port", "8080"]