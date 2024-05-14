FROM python:3-alpine

RUN pip install --upgrade pip


COPY challenge /challenge/

WORKDIR /challenge


RUN pip install -r requirements.txt &&\
    chmod +x source.py db.py


ENTRYPOINT [ "./source.py" ]