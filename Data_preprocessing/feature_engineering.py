# Create a new feature 'popularity_score' as a combination of 'ratings_count' and 'suggestions_count'
# For simplicity, let's just take a weighted sum for illustration purposes.
# You can experiment with different combinations and transformations.
import pandas as pd
df = pd.read_csv("../game_info_preprocessed.csv")
df['popularity_score'] = (df['ratings_count'] * 0.5) + (df['suggestions_count'] * 0.5)

# Now, let's say you want to standardize the new 'popularity_score' feature as well
from sklearn.preprocessing import StandardScaler

# Create a StandardScaler object
standard_scaler = StandardScaler()

# Standardize the 'popularity_score' feature
df['popularity_score'] = standard_scaler.fit_transform(df['popularity_score'].values.reshape(-1, 1))
df.to_csv('../game_info_preprocessed.csv', index=False)
