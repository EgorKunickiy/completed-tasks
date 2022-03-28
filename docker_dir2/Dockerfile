FROM python:3
RUN pip install SQLAlchemy
RUN pip install psycopg2
ADD ./create_db.py /server/
ADD ./data_for_db.py /server/
ADD ./database_for_server.py /server/
ADD ./mathematical_logic.py /server/
ADD ./structure_of_table.py /server/
ADD ./mat_socket_client.py /server/
ADD ./mathematical_socket_server.py /server/
WORKDIR /server/
EXPOSE 5000
CMD ["python", "/server/mathematical_socket_server.py"]
CMD ["python", "/server/mat_socket_client.py", "add 5 6"]

