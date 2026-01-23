import pandas as pd
import matplotlib.pyplot as plt

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/VYPrOu0Vs3I0hKLLjiPGrA/survey-data-with-duplicate.csv"
df = pd.read_csv(url)

#Display the first few rows of the DataFrame
print(df.head())

#Count the number of duplicate rows in the dataset
duplicate_rows = df.duplicated()
num_duplicates = duplicate_rows.sum()
print(f"Number of duplicate rows: {num_duplicates}")

#Display the first 5 duplicate rows
print("First 5 duplicate rows:")
print(df[duplicate_rows].head())

#Identify duplicate rows based on selected columns: MainBranch, Employment, RemoteWork
duplicate_rows_subset = df.duplicated(subset=['MainBranch', 'Employment', 'RemoteWork'], keep=False)
num_duplicates_subset = duplicate_rows_subset.sum()
print(f"\nNumber of duplicate rows based on MainBranch, Employment, RemoteWork: {num_duplicates_subset}")

#Display the first 5 duplicate rows based on subset
print("First 5 duplicate rows based on subset:")
print(df[duplicate_rows_subset].head())

#Analyze which columns frequently contain identical values within these duplicate rows
dup_df = df[duplicate_rows_subset]
grouped = dup_df.groupby(['MainBranch', 'Employment', 'RemoteWork'])
identical_cols = grouped.agg(lambda x: x.nunique() == 1)
freq_identical = identical_cols.sum().sort_values(ascending=False)
print("\nFrequency of columns being identical within duplicate groups (based on MainBranch, Employment, RemoteWork):")
print(freq_identical)

#Distribution by MainBranch
plt.figure(figsize=(10, 6))
dup_df['MainBranch'].value_counts().plot(kind='bar')
plt.title('Distribution of Duplicate Rows by MainBranch')
plt.xlabel('MainBranch')
plt.ylabel('Number of Duplicate Rows')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('duplicates_by_mainbranch.png')
plt.show()

#Distribution by Employment
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

#Distribution by RemoteWork
plt.figure(figsize=(10, 6))
dup_df['RemoteWork'].value_counts().plot(kind='bar')
plt.title('Distribution of Duplicate Rows by RemoteWork')
plt.xlabel('RemoteWork')
plt.ylabel('Number of Duplicate Rows')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('duplicates_by_remotework.png')
plt.show()

#Distribution by Country
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

#Save the cleaned dataset to a new CSV file
df_cleaned.to_csv('survey_data_cleaned.csv', index=False)

#Identify remaining duplicate rows in the cleaned dataset
remaining_duplicates = df_cleaned.duplicated(subset=critical_columns).sum()
print(f"\nNumber of remaining duplicate rows in cleaned dataset based on critical columns: {remaining_duplicates}")

#Identify missing values in the cleaned dataset
missing_values = df_cleaned.isnull().sum()
print("\nMissing values in cleaned dataset:")
print(missing_values[missing_values > 0])

#Impute missing values in EdLevel with the most frequent value
mode_edlevel = df_cleaned['EdLevel'].mode()[0]
df_cleaned['EdLevel'].fillna(mode_edlevel, inplace=True)
print(f"\nImputed missing values in EdLevel with: {mode_edlevel}")

#Check missing values again after imputation
missing_values_after = df_cleaned.isnull().sum()
print("\nMissing values after imputation:")
print(missing_values_after[missing_values_after > 0])

#Check and handle missing values in ConvertedCompYearly
missing_comp = df_cleaned['ConvertedCompYearly'].isnull().sum()
print(f"\nMissing values in ConvertedCompYearly: {missing_comp}")
if missing_comp > 0:
    median_comp = df_cleaned['ConvertedCompYearly'].median()
    df_cleaned['ConvertedCompYearly'] = df_cleaned['ConvertedCompYearly'].fillna(median_comp)
    print(f"Imputed missing values in ConvertedCompYearly with median: {median_comp}")

#Compensation analysis using ConvertedCompYearly
print("\nCompensation Analysis (ConvertedCompYearly in USD):")
print(f"Mean annual compensation: {df_cleaned['ConvertedCompYearly'].mean():.2f}")
print(f"Median annual compensation: {df_cleaned['ConvertedCompYearly'].median():.2f}")
print(f"Min annual compensation: {df_cleaned['ConvertedCompYearly'].min():.2f}")
print(f"Max annual compensation: {df_cleaned['ConvertedCompYearly'].max():.2f}")
print(f"Number of non-null compensation values: {df_cleaned['ConvertedCompYearly'].notna().sum()}")

#Plot distribution of compensation
plt.figure(figsize=(10, 6))
df_cleaned['ConvertedCompYearly'].plot(kind='hist', bins=50, edgecolor='black')
plt.title('Distribution of Annual Compensation')
plt.xlabel('Annual Compensation (USD)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('compensation_distribution.png')
plt.show()






