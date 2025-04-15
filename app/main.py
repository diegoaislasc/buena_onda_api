from app.database import conn

cur = conn.cursor()

cur.execute('SELECT *'
            ' FROM '
            'artist;')
row = cur.fetchone()
print('Found', row)
