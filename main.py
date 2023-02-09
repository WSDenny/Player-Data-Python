# Goal: extract, organize, and alter csv files containing NBA and NFL player information 
import pandas as pd
import numpy as np

def selectionSort(array, size):
    
    for ind in range(size):
        min_index = ind
 
        for j in range(ind + 1, size):
            # select the minimum element in every iteration
            if array[j] < array[min_index]:
                min_index = j
         # swapping the elements to sort the array
        (array[ind], array[min_index]) = (array[min_index], array[ind])


NBA_data = pd.read_csv("NBA.csv")               #reading in NBA csv
#print(NBA_data)

NBA_last = NBA_data['#LastName']               #setting each column to its own variable
#print(NBA_first)
NBA_first = NBA_data['#FirstName']
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

NBA_jers = NBA_jers.dropna()                    #drop null values if any
array = (NBA_jers.to_numpy())                   #convert column to list
size = len(array)

selectionSort(array, size)                      #run selection sort TC: O(n^2) Space: O(1)
#print(array)

NFL_data = pd.read_csv("NFL.csv")               #reading in NFL csv
#print(NFL_data)

NFL_full = NFL_data['full_name']                #setting each column to a variable
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

"""
for x in range(10):
    if x % 2 == 1:                              #choosing all the NFL players with odd jersey numbers between 0 and 10
        print((NFL_data[NFL_data['number'].isin([x])]))

for y in range(10, 21):
    if y % 2 == 0:                              #choosing all the NBA players with even jersey numbers between 10 and 20
        print(NBA_data[NBA_data['#Jersey Num'].isin([y])])
"""

evens_list = []                                             #creating empty sets for storage
odds_list = []
jers_list = NBA_jers.values.tolist()                        #converting dataframes to lists
num_list = NFL_num.values.tolist()
jers_list.sort()                                            #sorting lists
num_list.sort()

for x in range(1, 101, 2):
    for y in range(len(jers_list)):                         #selecting odd numbers from list and storing them
        if x == jers_list[y]:
            odds_list.append(jers_list[y])

#print(odds_list)
odds_df = pd.DataFrame(odds_list, columns = ['odds'])       #converting list into dataframe
print(odds_df)

for x in range(0, 101, 2):
    for y in range(len(num_list)):                          #selecting even numbers from list and storing them
        if x == num_list[y]:
            evens_list.append(num_list[y])

#print(evens_list)
evens_df = pd.DataFrame(evens_list, columns = ['evens'])    #converting list into dataframe
print(evens_df)
