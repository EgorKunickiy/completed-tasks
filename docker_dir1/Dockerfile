FROM python:3
COPY requirements.txt .
RUN pip install -r requirements.txt
ADD ./create_db.py /
ADD ./data_for_db.py /
ADD ./database_for_server.py /
ADD ./mathematical_logic.py /
ADD ./structure_of_table.py /
ADD ./mathematical_http_server.py /
CMD ["python", "./mathematical_http_server.py"]