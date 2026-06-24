import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
data = {
    'Hours': [1, 2, 3, 4, 5],
    'Marks': [20, 30, 40, 50, 60]
}

df = pd.DataFrame(data)
X = df[['Hours']]
y = df['Marks']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model = LinearRegression()
model.fit(X_train, y_train)
predicted_marks = model.predict([[6]])
print(predicted_marks)