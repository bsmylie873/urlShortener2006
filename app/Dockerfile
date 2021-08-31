FROM tiangolo/uwsgi-nginx-flask:python3.7-alpine3.7
EXPOSE 40001
WORKDIR /app
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
ENV FLASK_APP main.py
ENTRYPOINT ["python", "-m", "flask", "run", "--host=127.0.0.1"]