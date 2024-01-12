FROM python:3.10

RUN mkdir /test

WORKDIR /test

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x /test/docker/*.sh

CMD ["gunicorn", "myApp.main:app", "--workers", "1", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind=0.0.0.0:8000"]