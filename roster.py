# https://goheels.com/sports/mens-basketball/roster
import pandas as pd


# Step 1: Simple list with last names only
roster = ['Bacot', 'Davis', 'Cadeau']
# print(roster)

# Step 2: Print using a for loop
for player in roster:
    print(player)

# Step 3: Import Pandas and create DataFrame with no header
data = pd.DataFrame(roster)
print(data)

# Step 4: DataFrame with 'Last Name' header
player = {'Last Name': roster}
data = pd.DataFrame(player)
print(data)


# Step 5:  DataFrame with different columns
player = {'Last Name': roster,
          'First Name': ['Armando', 'RJ', 'Elliot'],
          'height': [83,72,73],
          'weight': [240,180,180]}
data = pd.DataFrame(player)
print(data)

# Step 6: 
player = {'Last Name': ['Bacot', 'Davis', 'Cadeau'],
          'First Name': ['Armando', 'RJ', 'Elliot'],
          'height': [83,72,73],
          'weight': [240,180,180]}
data = pd.DataFrame(player)
print(data)

# Step 7: 
player = {'Last Name': ['Bacot', 'Davis', 'Cadeau'],
          'First Name': ['Armando', 'RJ', 'Elliot'],
          'height': [83,72,73],
          'weight': [240,180,180]}
data = pd.DataFrame(player)
print(data)
# bmi = weight in kg/ height in meters squared
data ["bmi"] = (data ["weight"]/2.205)/((data ["height"]/39.37)**2)
print (data)
data. to_csv("bmi.csv" )
