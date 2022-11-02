import sqlite3

try:
    conn = sqlite3.connect("sql_test.py")
    cursor = conn.cursor()
    
except sqlite3.Error as error:
    print("Error", error)
    
lesson = cursor.execute("SELECT * FROM 'lesson'")
print(lesson.fetchall())
    
# finally:
#     if (conn):
#         conn.close()