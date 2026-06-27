import sqlite3
from horo import get_horoscope_data


def update_db():
    conn = sqlite3.connect('horoscope.db')
    cursor = conn.cursor()

    
    cursor.execute("DELETE FROM signs")


    data = get_horoscope_data()

    
    for sign, forecast in data.items():
        cursor.execute(
            "INSERT INTO signs (name, forecast) VALUES (?, ?)",
            (sign, forecast)
        )

    conn.commit()
    conn.close()

    print("База обновлена")


if __name__ == "__main__":
    update_db()