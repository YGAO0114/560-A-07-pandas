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
