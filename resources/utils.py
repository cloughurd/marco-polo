import json
import sqlite3

with open('states.json', 'r') as f:
    states = json.load(f)

print(states)

con = sqlite3.connect('marcopolo.db')
cur = con.cursor()

#cur.execute('CREATE TABLE state (id TEXT PRIMARY KEY, name TEXT)')
#cur.execute('CREATE TABLE city (id INTEGER PRIMARY KEY, name TEXT, state_id TEXT, is_capital INTEGER, FOREIGN KEY (state_id) REFERENCES state(id))')

for s in states:
    cur.execute(f"INSERT INTO state VALUES ('{s['abbreviation']}', '{s['name']}')")
    cur.execute(f"INSERT INTO city VALUES (NULL, '{s['capital']}', '{s['abbreviation']}', 1)")
    for c in s['cityList']:
        cur.execute(f"INSERT INTO city VALUES (NULL, '{c}', '{s['abbreviation']}', 0)")

con.commit()

res = cur.execute('SELECT * FROM state')
print(res.fetchall())

res = cur.execute('SELECT * FROM city')
print(res.fetchall())

con.close()
