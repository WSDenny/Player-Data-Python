# Goal: extract, organize, and alter csv files containing NBA and NFL player information 
import pandas as pd
NBA_data = pd.read_csv("NBA.csv")               #reading in NBA csv
print(NBA_data)

NBA_first = NBA_data['#LastName']               #setting each column to its own variable
#print(NBA_first)
NBA_last = NBA_data['#FirstName']
#print(NBA_last)
NBA_jers = NBA_data['#Jersey Num']
#print(NBA_jers)
NBA_pos = NBA_data['#Position']
#print(NBA_pos)
NBA_hei = NBA_data['#Height']
#print(NBA_hei)
NBA_wei = NBA_data['#Weight']
#print(NBA_wei)
NBA_bdate = NBA_data['#Birth Date']
#print(NBA_bdate)

NFL_data = pd.read_csv("NFL.csv")               #reading in NFL csv
print(NFL_data)

NFL_full = NFL_data['full_name']                #setting each columb to a variable
#print(NFL_full)
NFL_num = NFL_data['number']
#print(NFL_num)
NFL_pos = NFL_data['position']
#print(NFL_pos)
NFL_hei = NFL_data['height_in_inches']
#print(NFL_hei)
NFL_wei = NFL_data['weight_in_lbs']
#print(NFL_wei)
NFL_bdate = NFL_data['date_of_birth']
#print(fname)
NFL_team = NFL_data['team']
#print(fname)