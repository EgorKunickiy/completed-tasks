FROM python:3
COPY requirements.txt .
RUN pip install -r requirements.txt
ADD create_db.py /http_server/
ADD data_for_db.py /http_server/
ADD database_for_server.py /http_server/
ADD mathematical_logic.py /http_server/
ADD structure_of_table.py /http_server/
ADD mathematical_http_server.py /http_server/
CMD ["python", "/http_server/mathematical_http_server.py"]