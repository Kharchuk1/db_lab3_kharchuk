import csv
import string
import psycopg2
import random

username = 'Kharchuk'
password = 'kharchuk'
database = 'lab_3'

csv_file = 'latest_RAPTOR_by_team.csv'

query_0 = '''
DELETE FROM statistic;
DELETE FROM player;
DELETE FROM team
'''

query_1 = '''
INSERT INTO team (team_id, team_name) VALUES (%s, %s)
'''

query_2 = '''
INSERT INTO player (player_id, player_name, poss, team_id) VALUES (%s, %s, %s, %s)
'''

query_3 = '''
INSERT INTO statistic (stat_id, player_id, minutes_played, raptor_box_total) VALUES (%s, %s, %s, %s)
'''

conn = psycopg2.connect(user=username, password=password, dbname=database)

def func(line):
    temp_line = line[2:]
    res = list()
    for i in range(len(line)-5):
        if temp_line[i] != "'":
            res.append(temp_line[i])
        else:
            break
    return ''.join(res)

with conn:
    cur = conn.cursor()
    cur.execute(query_0)
    with open(csv_file, 'r') as inf:
        reader = csv.DictReader(inf)
        for idx, row in enumerate(reader):
            values = (idx+1, row['team'])
            cur.execute(query_1, values)
            if values[0]==10:
                break


    with open(csv_file, 'r') as inf:
        reader = csv.DictReader(inf)
        for idx, row in enumerate(reader):
            values = (row['player_id'], row['player_name'], row['poss'],idx+1)
            cur.execute(query_2, values)
            if values[3]==10:
                break
    
    with open(csv_file, 'r') as inf:
        reader = csv.DictReader(inf)
        for idx, row in enumerate(reader):
            values = (idx+1, row['player_id'], row['mp'], row['raptor_box_total'])
            cur.execute(query_3, values)
            if values[0]==10:
                break
    conn.commit()