import joblib 
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv('housing.csv').iloc[:, :-1].dropna()
print(df.head())
print('Read data successfully')
x = df.drop(columns='median_house_value')
y = df.median_house_value.copy()
print('Split data successfully')

model = LinearRegression().fit(x,y)
print('Trained model successfully')

joblib.dump(model, 'model.joblib')
print(' Saved model successfully ')