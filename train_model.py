import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error
import joblib

# Load dataset
df = pd.read_csv(r'C:\Users\nagen\OneDrive\Desktop\archive\sales data-set.csv')

# Check columns
print(df.columns)

# Drop missing values only in required columns
df.dropna(subset=['Store', 'Dept', 'Date', 'Weekly_Sales', 'IsHoliday'], inplace=True)

# Convert categorical columns
df['Store'] = LabelEncoder().fit_transform(df['Store'])
df['Dept'] = LabelEncoder().fit_transform(df['Dept'])
df['Date'] = LabelEncoder().fit_transform(df['Date'])
df['IsHoliday'] = LabelEncoder().fit_transform(df['IsHoliday'])

# Features and target
X = df[['Store', 'Dept', 'Date', 'IsHoliday']]
y = df['Weekly_Sales']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model training
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'model.pkl')

# Evaluate
pred = model.predict(X_test)
mse = mean_squared_error(y_test, pred)
print("Model trained. MSE:", mse)