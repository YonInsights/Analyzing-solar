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

#Matplotlib and Seaborn to visualize the data

import matplotlib.pyplot as plt
import seaborn as sns

# Plotting GHI for each dataset
plt.figure(figsize=(14, 7))

plt.subplot(3, 1, 1)
plt.plot(benin_df['Timestamp'], benin_df['GHI'], label='Benin GHI')
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(sierraleone_df['Timestamp'], sierraleone_df['GHI'], label='Sierra Leone GHI')
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(togo_df['Timestamp'], togo_df['GHI'], label='Togo GHI')
plt.legend()

plt.show()
# Correlation matrix for Benin
print("Benin Correlation Matrix:")
print(benin_df.corr())

# Correlation matrix for Sierra Leone
print("\nSierra Leone Correlation Matrix:")
print(sierraleone_df.corr())

# Correlation matrix for Togo
print("\nTogo Correlation Matrix:")
print(togo_df.corr())

# Visualizing the correlation matrix
plt.figure(figsize=(14, 7))

plt.subplot(3, 1, 1)
sns.heatmap(benin_df.corr(), annot=True)
plt.title('Benin Correlation Matrix')

plt.subplot(3, 1, 2)
sns.heatmap(sierraleone_df.corr(), annot=True)
plt.title('Sierra Leone Correlation Matrix')

plt.subplot(3, 1, 3)
sns.heatmap(togo_df.corr(), annot=True)
plt.title('Togo Correlation Matrix')

plt.show()
# Convert Timestamp to datetime
benin_df['Timestamp'] = pd.to_datetime(benin_df['Timestamp'])
sierraleone_df['Timestamp'] = pd.to_datetime(sierraleone_df['Timestamp'])
togo_df['Timestamp'] = pd.to_datetime(togo_df['Timestamp'])

# Plotting time series for GHI
plt.figure(figsize=(14, 7))

plt.subplot(3, 1, 1)
plt.plot(benin_df['Timestamp'], benin_df['GHI'], label='Benin GHI')
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(sierraleone_df['Timestamp'], sierraleone_df['GHI'], label='Sierra Leone GHI')
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(togo_df['Timestamp'], togo_df['GHI'], label='Togo GHI')
plt.legend()

plt.show()


import matplotlib.pyplot as plt
import seaborn as sns

# Plotting GHI for each dataset
plt.figure(figsize=(14, 7))

plt.subplot(3, 1, 1)
plt.plot(benin_df['Timestamp'], benin_df['GHI'], label='Benin GHI')
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(sierraleone_df['Timestamp'], sierraleone_df['GHI'], label='Sierra Leone GHI')
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(togo_df['Timestamp'], togo_df['GHI'], label='Togo GHI')
plt.legend()

plt.show()

