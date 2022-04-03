FROM python:3.10

WORKDIR /dir

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY math_server/package .

ENTRYPOINT ["python"]