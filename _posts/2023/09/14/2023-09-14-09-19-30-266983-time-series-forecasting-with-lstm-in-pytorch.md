---
layout: post
title: "Time series forecasting with LSTM in PyTorch"
description: " "
date: 2023-09-14
tags: [LSTM, TimeSeriesForecasting]
comments: true
share: true
---

In this tutorial, we will explore how to perform time series forecasting using Long Short-Term Memory (LSTM) networks in PyTorch. LSTM is a type of recurrent neural network (RNN) that has shown great effectiveness in capturing and modeling sequences with temporal dependencies.

## Data Preparation

Before we start building our LSTM model, we need to prepare and preprocess our time series data. Typically, time series data comes in a sequential format, where each data point is associated with a specific time index. We will split our data into training and testing sets, and normalize the input data to ensure efficient training.

```python
import numpy as np
import torch

# Load and preprocess the time series data
data = np.loadtxt("time_series_data.csv", delimiter=",")

# Split the data into training and testing sets
train_size = int(len(data) * 0.8)
train_data, test_data = data[:train_size], data[train_size:]

# Normalize the data
mean = np.mean(train_data)
std = np.std(train_data)
train_data = (train_data - mean) / std
test_data = (test_data - mean) / std

# Convert the data to PyTorch tensors
train_data = torch.FloatTensor(train_data).unsqueeze(dim=1)
test_data = torch.FloatTensor(test_data).unsqueeze(dim=1)
```

## LSTM Model

Next, we will define our LSTM model architecture using the `nn.LSTM` module provided by PyTorch. The input to our LSTM network will be the previous `seq_len` time steps, and the output will be the prediction for the next time step.

```python
import torch.nn as nn

class LSTMModel(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, output_size):
        super(LSTMModel, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)
        
    def forward(self, x):
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(x.device)
        c0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(x.device)
        
        out, _ = self.lstm(x, (h0, c0))
        out = self.fc(out[:, -1, :])
        
        return out
```

## Training the Model

Now that our model is defined, we can train it using the training data. We will use the Mean Squared Error (MSE) loss and the Adam optimizer for training.

```python
# Define hyperparameters
input_size = 1
hidden_size = 64
num_layers = 2
output_size = 1
epochs = 100
learning_rate = 0.001

# Create the model instance
model = LSTMModel(input_size, hidden_size, num_layers, output_size)

# Define the loss function and optimizer
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

# Training loop
for epoch in range(1, epochs+1):
    model.train()
    
    # Forward pass
    outputs = model(train_data)
    loss = criterion(outputs, train_data)
    
    # Backward pass and optimization
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
    # Print the loss for every 10 epochs
    if epoch % 10 == 0:
        print(f"Epoch: {epoch}, Loss: {loss.item():.4f}")
```

## Evaluation and Prediction

After training our model, we can evaluate its performance by predicting the future values using the test data.

```python
model.eval()

# Make predictions on the test data
with torch.no_grad():
    predicted_values = model(test_data)

# Denormalize the predicted values
predicted_values = predicted_values * std + mean

# Plot the predicted values against the actual values
import matplotlib.pyplot as plt

plt.plot(test_data.squeeze().numpy(), label="Actual")
plt.plot(predicted_values.squeeze().numpy(), label="Predicted")
plt.xlabel("Time")
plt.ylabel("Value")
plt.legend()
plt.show()
```

## Conclusion

In this tutorial, we learned how to perform time series forecasting using LSTM networks in PyTorch. LSTM models are powerful tools for capturing and predicting patterns in sequential data. By preprocessing the data, defining the model architecture, and training it using appropriate optimization techniques, we can make accurate predictions on time series data. Use LSTM to unlock the potential of time series forecasting and make informed decisions based on sequential data.

**#LSTM** **#TimeSeriesForecasting**