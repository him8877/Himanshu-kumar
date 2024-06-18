import pandas as pd

data = [
    {
        "id": 88,
        "name": "Himanshu",
        "age": 25,
        "dept": "MCA"
    },
    {
        "id": 89,
        "name": "Rohit",
        "age": 22,
        "dept": "Btech"
    },
    {
        "id": 2023,
        "name": "Himanshu",
        "age": 30,
        "dept": "MCA"
    }
]

df = pd.DataFrame(data)

print(df)
