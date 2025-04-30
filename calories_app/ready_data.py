import pandas as pd
from decimal import Decimal
data = pd.read_csv("nutrition.csv")
print(data['carbs'])
data['carbs'] = data['carbs'].apply(lambda d: float(d.split("g")[0]))
data['fats'] = data['fats'].apply(lambda d: float(d.split("g")[0]))
data['protein'] = data['protein'].apply(lambda d: float(d.split("g")[0]))
data.to_csv("new_data.csv")