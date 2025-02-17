import mysql.connector
from mysql.connector import Error

connection = None

def init_db():
    global connection
    try:
        connection = mysql.connector.connect(
            host="localhost", # user
            user='root', # user
            password='', # passeord for database
            database="", # your database name
        )
        print("Подключение к базе данных выполнено успешно!")
    except Error as e:
        print(f"Ошибка при подключении к базе данных: {e}")

def get_user_role(telegram_id):
    if connection is None:
        print("Соединение с базой данных не установлено.")
        return None

    try:
        with connection.cursor() as cursor:
            # SQL-запрос для поиска роли по Telegram ID
            query = "SELECT Bot_role FROM users WHERE Telegram_id = %s"
            cursor.execute(query, (telegram_id,))
            result = cursor.fetchone()

            if result:
                return result[0]  # Возвращаем роль
            else:
                return None  # Пользователь не найден

    except Error as e:
        print(f"Ошибка при выполнении запроса: {e}")
        return None

import mysql.connector
from mysql.connector import Error

def add_user_to_db(
    telegram_id, username, first_name, last_name, create_time, update_time,
    membership_expiry, invitation_link, membership_type, bot_role, buy_score,
    task_score, father_code, blance, sum_blance, blance_address, is_admin, status
):
    try:
        # Подключение к базе данных
        with mysql.connector.connect(
            host="localhost",
            user="root",
            password="09PASSWORd!",
            database="tgbot",
        ) as connection:
            with connection.cursor() as cursor:
                # SQL-запрос для вставки данных
                query = """
                INSERT INTO users (
                    telegram_id, username, first_name, last_name, create_time,
                    update_time, membership_expiry, invitation_link, membership_type,
                    bot_role, buy_score, task_score, father_code, blance, sum_blance,
                    blance_address, is_admin, status
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                # Значения для вставки
                values = (
                    telegram_id, username, first_name, last_name, create_time,
                    update_time, membership_expiry, invitation_link, membership_type,
                    bot_role, buy_score, task_score, father_code, blance, sum_blance,
                    blance_address, is_admin, status
                )

                # Выполнение запроса
                cursor.execute(query, values)
                connection.commit()  # Фиксируем изменения
                print("Пользователь успешно добaавлен в базу данных!")

    except Error as e:
        print(f"Ошибка при добавлении пользователя: {e}")

