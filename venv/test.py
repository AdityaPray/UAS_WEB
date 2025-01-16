import pymysql

def connect():
    try:
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='web',
            cursorclass=pymysql.cursors.DictCursor
        )
        return connection
    except pymysql.MySQLError as e:
        print(f"Error connecting to database: {e}")
        return None


def test_query():
    connection = connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM `rekomendasi _wisata`")
            results = cursor.fetchall()
            print(results)
    except pymysql.MySQLError as e:
        print(f"Error executing query: {e}")
    finally:
        connection.close()

test_query()
