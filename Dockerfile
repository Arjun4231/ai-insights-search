FROM python:3.10-slim-bullseye

ENV HOST=0.0.0.0

ENV LISTEN_PORT 8080

EXPOSE 8080

RUN apt-get update && apt-get install -y git

COPY . /app

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

WORKDIR app/

CMD ["streamlit", "run", "main.py", "--server.port", "8080"]