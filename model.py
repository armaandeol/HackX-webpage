import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler



# Example dataset with 'latitude', 'longitude', 'rainfall'
data = pd.read_csv('rainfall_data.csv')  # This should contain latitude, longitude, and rainfall data

# Preview the dataset
print(data.head())


# Define features (latitude, longitude) and target (rainfall)
X = data[['latitude', 'longitude']].values
y = data['rainfall'].values

# Normalize the input features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Define the model
model = models.Sequential()

# Add input layer with two input nodes (latitude and longitude)
model.add(layers.InputLayer(input_shape=(2,)))

# Add a couple of hidden layers
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(32, activation='relu'))

# Output layer for rainfall prediction (single output)
model.add(layers.Dense(1, activation='linear'))

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])

# Train the model
history = model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2)
# Evaluate on test data
test_loss, test_mae = model.evaluate(X_test, y_test)
print(f"Test Mean Absolute Error: {test_mae}")
# Example: Predict rainfall for a given latitude and longitude
latitude = 40.7128   # Example latitude (New York)
longitude = -74.0060  # Example longitude (New York)

# Normalize the input
input_data = scaler.transform([[latitude, longitude]])

# Make a prediction
predicted_rainfall = model.predict(input_data)
print(f"Predicted Rainfall: {predicted_rainfall[0][0]}")