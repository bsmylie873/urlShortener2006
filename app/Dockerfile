FROM tiangolo/uwsgi-nginx-flask:python3.7-alpine3.7
EXPOSE 40001
WORKDIR /app
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=127.0.0.1
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY . /app
CMD flask run