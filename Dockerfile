FROM python:3
EXPOSE 40001
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY main.py /
CMD [ "python", ".app.py" ]