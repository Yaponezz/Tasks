import sqlite3

conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY,
    task TEXT
)
""")

def add_task(task):
    cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
    conn.commit()

def get_tasks():
    cursor.execute("SELECT * FROM tasks")
    return cursor.fetchall()

if __name__ == "__main__":
    while True:
        cmd = input("1-add, 2-show: ")
        
        if cmd == "1":
            task = input("Task: ")
            add_task(task)
        elif cmd == "2":
            for t in get_tasks():
                print(t)
