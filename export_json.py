import json
import psycopg2

username = 'Kharchuk'
password = 'kharchuk'
database = 'lab_3'
host = 'localhost'
port = '5432'

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

data = {}
with conn:
    cur = conn.cursor()

    for table in ('team', 'player', 'statistic'):
        cur.execute('SELECT * FROM ' + table)
        rows = []
        fields = [x[0] for x in cur.description]

        for row in cur:
            rows.append(dict(zip(fields, row)))

        data[table] = rows

with open('export_json.json', 'w') as outf:
    json.dump(data, outf, default=str)