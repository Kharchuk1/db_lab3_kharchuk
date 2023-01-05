import psycopg2
import matplotlib.pyplot as plt

username = 'Kharchuk'
password = 'kharchuk'
database = 'lab_3'
host = 'localhost'
port = '5432'

#к-сть часу(хвилин) на полі кожного гравця
query_1 = '''
select * from StatPlayer
'''
'''
create view StatPlayer as
select player_name, minutes_played from statistic
join player on player.player_id=statistic.player_id
'''
#к-сть гравців по командам
query_2 = '''
select * from TeamPlayer
'''
'''
create view TeamPlayer as
select team_name, count(player_name) from player
join team on player.team_id=team.team_id
group by team_name
'''
#залежність набраних балів на полі від часу на полі
query_3 = '''
select * from ScorePlayer
'''
'''
create view ScorePlayer as
select raptor_box_total, minutes_played from statistic
order by raptor_box_total
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:
    cur = conn.cursor()
    cur.execute(query_1)
    player = []
    count_time = []

    for row in cur:
        player.append(row[0])
        count_time.append(row[1])

    x_range = range(len(player))

    figure, (bar_ax, pie_ax, graph_ax) = plt.subplots(1, 3)

    bar_ax.bar(x_range, count_time, label='Total')
    bar_ax.set_title('Total time')
    bar_ax.set_xlabel('Player')
    bar_ax.set_ylabel('Count')
    bar_ax.set_xticks(x_range)
    bar_ax.set_xticklabels(player,  rotation=90)

    cur.execute(query_2)
    teams = []
    count_player = []

    for row in cur:
        teams.append(row[0])
        count_player.append(row[1])

    pie_ax.pie(count_player, labels=teams, autopct='%1.1f%%')
    pie_ax.set_title('Teams and players')

    cur.execute(query_3)
    player = []
    score = []

    for row in cur:
        player.append(row[0])
        score.append(row[1])

    graph_ax.plot(player, score, marker='o')
    graph_ax.set_xticks(player)
    graph_ax.set_xticklabels(player, rotation=90)
    graph_ax.set_xlabel('Player')
    graph_ax.set_ylabel('Score')
    graph_ax.set_title('Score')

    for i, j in zip(player, score):
        graph_ax.annotate(j, xy=(i, j), xytext=(7, 2), textcoords='offset points')

mng = plt.get_current_fig_manager()
mng.resize(1000, 600)

plt.show()