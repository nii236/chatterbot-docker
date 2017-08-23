FROM python:2.7
ADD run.py /
ADD db.sqlite3 /
RUN pip install chatterbot
RUN python migrate.py
CMD [ "python", "/run.py" ]
