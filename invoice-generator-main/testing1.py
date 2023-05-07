import pandas as pd





df = pd.read_csv('Performance_data.csv')
ID = input("enter the ID: ")
test = df[df["ZP_ID"]== ID]

test.to_csv('test_data.csv', index=False)

#testing1 beje subclass te invoice.py