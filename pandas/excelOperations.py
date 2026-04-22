import pandas as pd

excelFile = 'salaryData.xlsx'
sheetName = 'Sheet2'

try:
    df = pd.read_excel(excelFile, sheet_name=sheetName)
    print(df)
except:
    print(f"{excelFile} not found or the sheet_name={sheetName} not found")
