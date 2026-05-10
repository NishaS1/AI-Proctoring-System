import sqlite3

def init():
    conn = sqlite3.connect('proctor.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS sessions
                 (id INTEGER PRIMARY KEY, student TEXT, start TEXT, end TEXT, score INTEGER)''')
    c.execute('''CREATE TABLE IF NOT EXISTS logs
                 (id INTEGER PRIMARY KEY, session_id INTEGER, timestamp TEXT, event TEXT)''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init()