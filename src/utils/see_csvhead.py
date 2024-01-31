import pandas as pd 

# csv_path = "outputs/final_output.csv"
csv_path = "../outputs/output_2023.csv"
# csv_path = "/Users/shiym/Documents/PEFT/web_scraper_project/src/outputs/final_output.csv"
df = pd.read_csv(csv_path, encoding='utf-8')
print(df.head())

print("shape about rows and columns:",df.shape)

print(df.info())




