import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def train_linear_regression_model():
    # Load the data
    data = pd.read_csv('Sleep_health_and_lifestyle_dataset.csv')
    print(data.info())
    data = data.drop(columns=['Person ID', 'Quality of Sleep', 'Sleep Disorder', 'Stress Level'])
    data[['Systolic', 'Diastolic']] = data['Blood Pressure'].str.split('/', expand=True)
    print(data['Gender'].unique())
    # Label encoding for categorical columns
    Le = LabelEncoder()
    data['BMI Category'] = Le.fit_transform(data['BMI Category'])
    data['Occupation'] = Le.fit_transform(data['Occupation'])
    data['Gender'] = Le.fit_transform(data['Gender'])
    print(data['Gender'].unique())
    # Prepare the features and target
    x = data[['Gender', 'Age', 'Physical Activity Level', 'BMI Category', 'Systolic', 'Diastolic',
              'Heart Rate', 'Daily Steps']].values
    y = data['Sleep Duration'].values

    # Split the data
    x_train, _, y_train, _ = train_test_split(x, y, test_size=0.2)

    # Train the linear regression model
    model = LinearRegression()
    model.fit(x_train, y_train)

    return model

if __name__ == "__main__":
    trained_model = train_linear_regression_model()
