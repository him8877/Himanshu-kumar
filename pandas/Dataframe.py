import pandas as pd

# Creating a DataFrame from a dictionary
data = {
    'ID': ['254', '586', '664', '875'],
    'Name': ['Himanshu', 'Ankit', 'Rohit', 'Varun'],
    'Age': [25, 28, 22, 32],
    'City': ['greater Noida', 'Bihar', 'Dwarka', 'Digital India']
}
df = pd.DataFrame(data)
print(df)
