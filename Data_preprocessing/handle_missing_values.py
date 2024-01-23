import pandas as pd 
df = pd.read_csv("../game_info.csv")

# A count of missing values in each column

missing_values = df.isnull().sum()
print("Below are missing values before handling")
print(missing_values)


# Handling missing values
# This fills missing genres with a placeholder value such as 'Unknown'
#df['genres'] = df['genres'].fillna('Unknown')
df['developers'] = df['developers'].fillna('Unknown')
df['platforms'] = df['platforms'].fillna('Unknown')

# Recheck the count of missing values
new_missing_values = df.isnull().sum()
print(new_missing_values)

#Overwriting the exisitng dataset with cleaned one
df.to_csv('../game_info.csv', index=False)
