FROM python:3.7-alpine
EXPOSE 40001
WORKDIR /app
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc muscl-dev linux-headers
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY . /app
CMD flask run