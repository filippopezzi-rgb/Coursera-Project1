import pandas as pd

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/VYPrOu0Vs3I0hKLLjiPGrA/survey-data-with-duplicate.csv"
df = pd.read_csv(url)
#df = df.drop_duplicates()

#Display the first 5 rows of the dataset
print(df.head())

#Display the number of rows in the dataset
print("Number of rows:", df.shape[0])

#Display the number of columns in the dataset
print("Number of columns:", df.shape[1])

#Display the data types of each column
print("Data types of each column:\n", df.dtypes)

#Convert the 'Age' column to numeric, forcing errors to NaN
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')

# Remove rows where 'Age' is NaN
df = df.dropna(subset=['Age'])

#Display the average age of participants
average_age = df['Age'].mean()
print("Average age of participants:", average_age)

#Display the unique values in the 'Country' column
unique_countries = df['Country'].unique()
print("Unique countries in the dataset:", unique_countries)



