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
        cursor.execute("SELECT * FROM (SELECT SUM(count) AS sum "
                       "FROM (SELECT COUNT(*)-1 AS count "
                       "FROM Math_expression "
                       "GROUP BY (operator, number1, number2) "
                       "HAVING COUNT(*) > 1) AS prom)AS prom4 "
                       "CROSS JOIN "
                       "(SELECT sum FROM(SELECT SUM(count) AS sum "
                       "FROM (SELECT COUNT(*) AS count "
                       "FROM Math_expression "
                       "GROUP BY (operator, number1, number2) "
                       "HAVING COUNT(*) = 1) AS prom2) AS prom3)AS prom5 "
                       )
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
