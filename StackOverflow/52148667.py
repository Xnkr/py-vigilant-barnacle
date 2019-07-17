from collections import defaultdict
import csv


def spliter(row):
    left_team, right_team = row
    return {
        'left': left_team[:-2].strip(),
        'left_score': int(left_team[-2:].strip()),
        'right': right_team[:-2].strip(),
        'right_score': int(right_team[-2:].strip())
    }

data = """Lions 3, Snakes 3
Tarantulas 1, FC Awesome 0
Lions 1, FC Awesome 1
Tarantulas 3, Snakes 1
Lions 4, Grouches 0"""

with open('52148667.csv') as data_obj:
    reader = csv.reader(data_obj)
    data_dicts2 = [spliter(row) for row in reader]
with open('52148667.csv') as data_obj:
    data_list3 = [line.rstrip('\n') for line in data_obj.readlines()]
    



data_list = data.splitlines()

print(data_list)
print(data_list3)

def splitter(row):
    left_team, right_team = row.split(',')
    return {
        'left': left_team[:-2].strip(),
        'left_score': int(left_team[-2:].strip()),
        'right': right_team[:-2].strip(),
        'right_score': int(right_team[-2:].strip())
    }

data_dicts = [splitter(row) for row in data_list]


team_scores = defaultdict(int)
for game in data_dicts2:
    if game['left_score'] == game['right_score']:
        team_scores[game['left']] += 1
        team_scores[game['right']] += 1
    elif game ['left_score'] > game['right_score']:
        team_scores[game['left']] += 3
        team_scores[game['right']] += 0
    else:
        team_scores[game['left']] += 0
        team_scores[game['right']] += 3

from operator import itemgetter

teams_sorted = sorted(team_scores.items(), key=itemgetter(1), reverse=True)

for idx, (team, score) in enumerate(teams_sorted, 1):
    print(f'{idx}. {team} {score} pts')