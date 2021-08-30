FROM python:3
EXPOSE 40001

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY main.py /app
CMD python main.py