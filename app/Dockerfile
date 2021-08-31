FROM tiangolo/uwsgi-nginx-flask:python3.7-alpine3.7
EXPOSE 40001
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY app.py /app
CMD ["python","main.py"]