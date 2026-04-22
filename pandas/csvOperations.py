import pandas as pd

csvFile = 'salary.csv'

try:
    df = pd.read_csv(csvFile)
    print(df)
    df.to_csv("revisedSalary.csv", index=None)
except:
    print(f"{csvFile} not found")
