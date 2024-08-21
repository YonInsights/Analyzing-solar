import pandas as pd

# Define the file paths
file_paths = [
    r'D:\10 Academy_Kefya\Week 0\Analyzing solar\data\benin-malanville.csv',
    r'D:\10 Academy_Kefya\Week 0\Analyzing solar\data\sierraleone-bumbuna.csv',
    r'D:\10 Academy_Kefya\Week 0\Analyzing solar\data\togo-dapaong_qc.csv'
]

# Load the CSV files into DataFrames from the above file path
benin_df = pd.read_csv(file_paths[0])
sierraleone_df = pd.read_csv(file_paths[1])
togo_df = pd.read_csv(file_paths[2])

# Print the first 5 rows of each DataFrame to verify
print("Benin DataFrame:")
print(benin_df.head())

print("\nSierra Leone DataFrame:")
print(sierraleone_df.head())

print("\nTogo DataFrame:")
print(togo_df.head())
#summary of dataset with basic statistics
print("Benin DataFrame Summary:")
print(benin_df.describe())

print("\nSierra Leone DataFrame Summary:")
print(sierraleone_df.describe())

print("\nTogo DataFrame Summary:")
print(togo_df.describe())


