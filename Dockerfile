FROM python:3

COPY requirements.txt .

RUN pip install -- user hashids~=1.3.1
RUN pip install -- user Flask~=1.1.2
RUN pip install -- user python-dotenv~=0.19.0
RUN pip install -- user gunicorn==19.9.0

CMD [ "python", ".app.py" ]