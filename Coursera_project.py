import pandas as pd
import json


url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%201/Accessing%20Data%20Using%20APIs/jobs.json"

df = pd.read_json(url)

# Write a function to get the number of jobs for the Python technology.
def get_number_of_jobs_T(technology):
    df_filtered = df[df['Key Skills'].str.contains(technology, case=False, na=False)]
    number_of_jobs = len(df_filtered)
    return technology,number_of_jobs

tech, count = get_number_of_jobs_T("Python")
print(f"Technology: {tech}, Number of jobs: {count}")

#Write a function to find number of jobs in US for a location of your choice.
def get_number_of_jobs_L(location):
    df_filtered = df[df['Location'].str.contains(location, case=False, na=False)]
    number_of_jobs = len(df_filtered)
    return location,number_of_jobs

location, count1 = get_number_of_jobs_L("New York")
print(f"Location: {location}, Number of jobs: {count1}")

tech_list = ["C#", "C","Python", "Java", "JavaScript", "C++", "SQL", "Spark", "Hadoop", "Tableau", "Power BI", "Scala", "Oracle", "SQL Server", "MySQLServer", "MongoDB", "PostgreSQL"]

final_results = []

for technology in tech_list:
    tech, count = get_number_of_jobs_T(technology)
    final_results.append({"Technology": tech, "Number of jobs": count})

df_final = pd.DataFrame(final_results)
print(df_final)

df_final.to_excel("job-postings.xlsx", index=False)

