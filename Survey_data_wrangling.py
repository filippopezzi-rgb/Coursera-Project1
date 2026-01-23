import pandas as pd
import matplotlib.pyplot as plt

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/VYPrOu0Vs3I0hKLLjiPGrA/survey-data-with-duplicate.csv"
df = pd.read_csv(url)

# Display the first few rows of the DataFrame
print(df.head())

#Count the number of duplicate rows in the dataset
duplicate_rows = df.duplicated()
num_duplicates = duplicate_rows.sum()
print(f"Number of duplicate rows: {num_duplicates}")

#Display the first 5 duplicate rows
print("First 5 duplicate rows:")
print(df[duplicate_rows].head())

# Identify duplicate rows based on selected columns: MainBranch, Employment, RemoteWork
duplicate_rows_subset = df.duplicated(subset=['MainBranch', 'Employment', 'RemoteWork'], keep=False)
num_duplicates_subset = duplicate_rows_subset.sum()
print(f"\nNumber of duplicate rows based on MainBranch, Employment, RemoteWork: {num_duplicates_subset}")

# Display the first 5 duplicate rows based on subset
print("First 5 duplicate rows based on subset:")
print(df[duplicate_rows_subset].head())

# Analyze which columns frequently contain identical values within these duplicate rows
dup_df = df[duplicate_rows_subset]
grouped = dup_df.groupby(['MainBranch', 'Employment', 'RemoteWork'])
identical_cols = grouped.agg(lambda x: x.nunique() == 1)
freq_identical = identical_cols.sum().sort_values(ascending=False)
print("\nFrequency of columns being identical within duplicate groups (based on MainBranch, Employment, RemoteWork):")
print(freq_identical)

# Distribution by MainBranch
plt.figure(figsize=(10, 6))
dup_df['MainBranch'].value_counts().plot(kind='bar')
plt.title('Distribution of Duplicate Rows by MainBranch')
plt.xlabel('MainBranch')
plt.ylabel('Number of Duplicate Rows')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('duplicates_by_mainbranch.png')
plt.show()

# Distribution by Employment
plt.figure(figsize=(12, 8))
counts = dup_df['Employment'].value_counts().sort_values(ascending=True)
counts.plot(kind='barh')
plt.title('Distribution of Duplicate Rows by Employment', fontsize=15)
plt.ylabel('Employment', fontsize=12)
plt.xlabel('Number of Duplicate Rows', fontsize=12)
for index, value in enumerate(counts):
    plt.text(value + 1, index, f'{value}', va='center', fontsize=10)
plt.yticks(fontsize=9)
plt.tight_layout()
plt.savefig('duplicates_by_employment.png')
plt.show()

# Distribution by RemoteWork
plt.figure(figsize=(10, 6))
dup_df['RemoteWork'].value_counts().plot(kind='bar')
plt.title('Distribution of Duplicate Rows by RemoteWork')
plt.xlabel('RemoteWork')
plt.ylabel('Number of Duplicate Rows')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('duplicates_by_remotework.png')
plt.show()

# Distribution by Country
plt.figure(figsize=(10, 6))
dup_df['Country'].value_counts().plot(kind='bar')
plt.title('Distribution of Duplicate Rows by Country')
plt.xlabel('Country')
plt.ylabel('Number of Duplicate Rows')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('duplicates_by_country.png')
plt.show()

#Critical columns to define uniqueness
critical_columns = ['Country', 'Age', 'Employment']
duplicates_critical = df.duplicated(subset=critical_columns).sum()
print(f"\nNumber of duplicate rows based on critical columns (Country, Age, Employment): {duplicates_critical}")

#Remove duplicates based on critical columns
df_cleaned = df.drop_duplicates(subset=critical_columns)
print(f"\nOriginal dataset shape: {df.shape}")
print(f"Cleaned dataset shape: {df_cleaned.shape}")
print(f"Number of rows removed: {df.shape[0] - df_cleaned.shape[0]}")




