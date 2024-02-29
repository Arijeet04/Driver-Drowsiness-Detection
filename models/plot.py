import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('Sleep_health_and_lifestyle_dataset.csv')
print(data.info())
data[['Systolic' , 'Diastolic']]=data['Blood Pressure'].str.split('/',expand=True)
