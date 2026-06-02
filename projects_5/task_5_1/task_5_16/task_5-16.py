import psycopg2

try:
    connection = psycopg2.connect(
        host="localhost",
        port="5430",
        user="postgres_user",
        password="postgres_password",
        database="postgres_db"
    )
    print(" Подключение к базе данных прошло успешно!")

    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM products;")
    result = cursor.fetchone()
    print(f"Количество товаров в таблице products: {result[0]}")

    cursor.close()

except Exception as error:
    print(f" Ошибка при подключении: {error}")

finally:
    if 'connection' in locals() and connection:
        connection.close()
        print(" Соединение закрыто.")