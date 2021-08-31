FROM python:3.7-alpine
EXPOSE 40001
ENV_LISTEN_PORT= 40001
WORKDIR /app
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY . /app
CMD ["pytho3", "app.py"]