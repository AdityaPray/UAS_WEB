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

def fetch_all_places():
    connection = connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM `rekomendasi_wisata`")
            results = cursor.fetchall()
            print("DEBUG: Results from database:", results)
            return results
    finally:
        connection.close()


def insert_place(nama, url_gambar, deskripsi):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute('INSERT INTO  `rekomendasi_wisata` (nama, url_gambar, deskripsi) VALUES (%s, %s, %s)',
                           (nama, url_gambar, deskripsi))
            connection.commit()
    finally:
        connection.close()

def fetch_place_by_id(id):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM  `rekomendasi_wisata` WHERE id = %s', (id,))
            return cursor.fetchone()
    finally:
        connection.close()

def update_place(id, nama, url_gambar, deskripsi):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute('UPDATE  `rekomendasi_wisata` SET nama = %s, url_gambar = %s, deskripsi = %s WHERE id = %s',
                           (nama, url_gambar, deskripsi, id))
            connection.commit()
    finally:
        connection.close()

def delete_place(id):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute('DELETE FROM  `rekomendasi_wisata` WHERE id = %s', (id,))
            connection.commit()
    finally:
        connection.close()
