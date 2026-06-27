import sqlite3
conn = sqlite3.connect('horoscope.db')
cursor = conn.cursor()
def get_forecast(sign_name):
    conn = sqlite3.connect('horoscope.db')
    cursor = conn.cursor()

    cursor.execute(
        "SELECT forecast FROM signs WHERE name = ?",
        (sign_name,)
    )

    result = cursor.fetchone()

    conn.close()

    if result:
        return result[0]

    return None
import sqlite3

def get_all_signs():
    conn = sqlite3.connect('horoscope.db')
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM signs")
    rows = cursor.fetchall()

    conn.close()

    return [row[0] for row in rows]