import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer

df = pd.read_csv("../game_info_preprocessed.csv")

# Split the 'genres', 'platforms', 'developers' columns into lists
#df['genres'] = df['genres'].str.split('||')
df['platforms'] = df['platforms'].str.split('||')
df['developers'] = df['developers'].str.split('||')

# Initialize MultiLabelBinarizer
mlb = MultiLabelBinarizer()

# Perform one-hot encoding and transform it back into a DataFrame
# Join the one-hot encoded genres back with the original DataFrame
#genres_encoded = pd.DataFrame(mlb.fit_transform(df['genres']), columns=mlb.classes_)
#df = df.join(genres_encoded)

platforms_encoded = pd.DataFrame(mlb.fit_transform(df['platforms']), columns=mlb.classes_)
df = df.join(platforms_encoded, rsuffix='_platform')

developers_encoded = pd.DataFrame(mlb.fit_transform(df['developers']), columns=mlb.classes_)
df = df.join(developers_encoded, rsuffix='_developer')

# Drop the original columns as they are now redundant
df = df.drop(['platforms','developers'], axis=1)

# Save a new csv file
df.to_csv('../game_info_preprocessed.csv', index=False)

