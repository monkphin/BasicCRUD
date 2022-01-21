FROM python:3

WORKDIR /usr/webapp

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY ./webapp/app.py app.py

EXPOSE 5000

CMD [ "python", "app.py" ]