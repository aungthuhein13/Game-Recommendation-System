import pandas as pd
from sklearn.preprocessing import MinMaxScaler
df = pd.read_csv("../game_info.csv")

# Create a MinMaxScaler object
scaler = MinMaxScaler()

# Assuming 'rating' and 'metacritic' are the columns you want to normalize
# Reshape the data using .values.reshape(-1, 1) because scaler expects 2D array
df['rating'] = scaler.fit_transform(df['rating'].values.reshape(-1, 1))
df['metacritic'] = scaler.fit_transform(df['metacritic'].values.reshape(-1, 1))

df.to_csv('../game_info_preprocessed.csv', index=False)




