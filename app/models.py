import os
import mysql.connector

class ItemModel:
    def __init__(self):
        self.config = {
            'host': os.getenv('DB_HOST', ''),
            'user': os.getenv('DB_USER', ''),
            'password': os.getenv('DB_PASS', ''),
            'database': os.getenv('DB_NAME', ''),
            'charset': 'utf8mb4',
            'use_unicode': True,
            'collation': 'utf8mb4_unicode_ci'
        }

    def get_all_items(self):
        try:
            conn = mysql.connector.connect(**self.config)
            cursor = conn.cursor(dictionary=True, buffered=True)
            cursor.execute("SET NAMES utf8mb4")
            cursor.execute("SET CHARACTER SET utf8mb4")
            cursor.execute("SET character_set_connection=utf8mb4")
            cursor.execute('SELECT name FROM items')
            items = cursor.fetchall()
            cursor.close()
            conn.close()
            return items
        except Exception as e:
            print(f"Error: {e}")
            return []
