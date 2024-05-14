FROM python:3.11

RUN apt-get update && apt-get install -y texlive-latex-base

WORKDIR /app

COPY flag.txt /flag.txt

COPY app.py /app

COPY templates /app/templates

COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

EXPOSE 8005

CMD ["python", "app.py"]
