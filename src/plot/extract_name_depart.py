import pandas as pd
import json

# Load the CSV file
file_path = '../outputs/final_2023extracted_data.csv'
data = pd.read_csv(file_path)

# Extracting names from the 'individuals' column, ignoring NaN values
all_names = []
for individuals in data['individuals'].dropna():
    # Parse the JSON-like string into a Python dictionary
    individuals_list = json.loads(individuals.replace("'", "\""))
    # Extract names from each individual's dictionary and add them to the all_names list
    for individual in individuals_list:
        all_names.append(individual['name'])

# Convert the list of names into a DataFrame for further analysis
names_df = pd.DataFrame(all_names, columns=['Name'])

# Count the frequency of each name
name_counts = names_df['Name'].value_counts().reset_index()
name_counts.columns = ['Name', 'Frequency']

# Save the frequency of names to a new CSV file
name_counts.to_csv('../outputs/name_frequencies.csv', index=False)

# Analysis of the "department" column
# Count the frequency of each department
department_counts = data['department'].value_counts().reset_index()
department_counts.columns = ['Department', 'Count']

# Save the frequency of departments to a new CSV file
department_counts.to_csv('../outputs/department_frequencies.csv', index=False)

print("The name frequencies and department frequencies have been saved to 'name_frequencies.csv' and 'department_frequencies.csv', respectively.")
