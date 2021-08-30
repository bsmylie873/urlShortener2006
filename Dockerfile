FROM python:3.7
EXPOSE 40001

WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt
RUN make /app

CMD ["python", "app/app.py"]