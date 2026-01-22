import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/Programming_Languages.html"
data  = requests.get(url).text 
soup = BeautifulSoup(data, 'html.parser')

# Scrape the language names and salaries from the table
table = soup.find('table')
rows = table.find_all('tr')
languages = []
salaries = []
for row in rows[1:]:  # Skip header row
    cols = row.find_all('td')
    if cols:
        languages.append(cols[1].text.strip())
        salaries.append(cols[3].text.strip())

print("Programming Languages and Average Annual Salaries:")
for lang, sal in zip(languages, salaries):
    print(f"{lang}: {sal}")

# Save to CSV
df = pd.DataFrame({'Language': languages, 'Average Annual Salary': salaries})
df.to_csv('popular-languages.csv', index=False)
print("Data saved to popular-languages.csv")

