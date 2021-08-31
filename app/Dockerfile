FROM tiangolo/uwsgi-nginx-flask:python3.7-alpine3.7
EXPOSE 40001
WORKDIR /app
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc muscl-dev linux-headers
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY . /app
CMD flask run