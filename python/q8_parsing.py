# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import csv

with open('football.csv') as football_data:
  data = list(csv.reader(football_data))

header = data[0]
data = data[1:]

lowest_diff = None
team = ''

for row in data:
  diff_goal = int(row[5])-int(row[6])
  diff = abs(diff_goal)
  if lowest_diff is None or diff < lowest_diff:
    lowest_diff = diff
    team = row[0]
print(team)  
