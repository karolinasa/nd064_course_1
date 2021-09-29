FROM python:2.7

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 3111

# commands to run on container start
CMD [ "python", "init_db.py" ]

CMD [ "python", "app.py" ]
