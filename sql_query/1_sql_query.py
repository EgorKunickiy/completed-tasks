import psycopg2


def get_query():
    connect = None
    try:
        connect = psycopg2.connect(
            host="localhost",
            database="Math_expression",
            user="postgres",
            password="pass")

        cursor = connect.cursor()
        cursor.execute("SELECT * FROM math_expression WHERE result < 0")
        row = cursor.fetchone()

        while row is not None:
            print(row)
            row = cursor.fetchone()

        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connect is not None:
            connect.close()


if __name__ == '__main__':
    get_query()