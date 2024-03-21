# Let's first load and inspect the head of the CSV file to understand its structure and format.
import pandas as pd

# Load the CSV file
file_path = '../outputs/final_2023extracted_data.csv'
data = pd.read_csv(file_path)

# Display the head of the dataset to understand its format
# data.head()

import json
from pandas.io.json import json_normalize

# Extracting names from the 'individuals' column, ignoring NaN values
# Initialize an empty list to hold all names
all_names = []

# Iterate over the 'individuals' column
for individuals in data['individuals'].dropna():
    # Parse the JSON-like string into a Python dictionary
    individuals_list = json.loads(individuals.replace("'", "\""))
    # Extract names from each individual's dictionary and add them to the all_names list
    for individual in individuals_list:
        all_names.append(individual['name'])

# Convert the list of names into a DataFrame for further analysis
names_df = pd.DataFrame(all_names, columns=['Name'])

# Display the first few names to ensure correct extraction
# names_df.head(), len(all_names)


import matplotlib.pyplot as plt

# Count the frequency of each name
name_counts = names_df['Name'].value_counts().head(10)


# # Analysis of the "department" column
# # Count the frequency of each department
department_counts = data['department'].value_counts()

# Display the frequency of departments
department_counts.head(), len(department_counts)


# Attempting an alternative approach for better handling of Chinese characters by specifying a font that is more likely to support Chinese characters.
# plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # Specify a font that supports Chinese characters

plt.rcParams['font.sans-serif'] = ['Baoli SC'] # 步骤一（替换sans-serif字体）
plt.rcParams['axes.unicode_minus'] = False

# Re-create the bar plot for the top 10 most frequent names with the new font setting
plt.figure(figsize=(10, 6))
name_counts.plot(kind='bar')
plt.title('Top 10 Most Frequent Names')
plt.xlabel('Name')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot with the new font setting, hoping for correct display of Chinese characters
plt.show()

# Create a plot for the "department" column
# Selecting the top 10 most frequent departments for clarity
top_departments = department_counts.head(10)

plt.figure(figsize=(10, 6))
top_departments.plot(kind='bar')
plt.title('Top 10 Most Frequent Departments')
plt.xlabel('Department')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot
plt.show()
