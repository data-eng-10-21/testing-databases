from db import cursor

def premium_user_count():
    cursor.execute("SELECT COUNT(*) FROM customers WHERE category = 'premium'")
    return cursor.fetchall()