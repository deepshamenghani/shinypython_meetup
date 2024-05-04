import pandas as pd
import numpy as np

# Read the unique combinations from the CSV file
unique_combinations = pd.read_csv('shinyAppCode/dog_breed_trait_combinations.csv')

# Assign a random rating between 2 and 5
unique_combinations['rating'] = np.random.randint(2, 6, unique_combinations.shape[0])

# Save the updated DataFrame to a new CSV
unique_combinations.to_csv('shinyAppCode/dog_synthetic_ratings.csv', index=False)

# Display the first few rows of the final DataFrame
print(unique_combinations.head())
