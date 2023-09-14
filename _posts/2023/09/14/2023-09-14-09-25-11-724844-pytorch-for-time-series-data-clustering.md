---
layout: post
title: "PyTorch for time series data clustering"
description: " "
date: 2023-09-14
tags: [MachineLearning]
comments: true
share: true
---

Clustering is a common machine learning technique used for grouping similar data points together based on their inherent patterns or characteristics. When it comes to time series data, clustering becomes a bit more challenging due to the temporal nature of the data. However, with the power of PyTorch, we can leverage its tensor operations and neural network capabilities to perform time series data clustering effectively.

In this blog post, we will explore how to use PyTorch for time series data clustering by implementing a simple example.

## Prerequisites

Before we dive into the code, make sure you have PyTorch and its dependencies installed. You can install PyTorch using pip or conda, depending on your preference.

```python
pip install torch
```

## Generating Synthetic Time Series Data

To illustrate the clustering process, let's start by generating synthetic time series data. We will generate three clusters, each containing 100 time series sequences. Each sequence will have a random length and consist of random values.

```python
import torch
from torch.utils.data import Dataset

class TimeSeriesDataset(Dataset):
    def __init__(self, num_clusters, num_sequences):
        self.num_clusters = num_clusters
        self.num_sequences = num_sequences
        self.data = []

        for _ in range(num_clusters):
            cluster_data = []
            
            for _ in range(num_sequences):
                seq_length = torch.randint(low=10, high=20, size=(1,))
                sequence = torch.randn(seq_length)
                cluster_data.append(sequence)
            
            self.data.append(cluster_data)

    def __len__(self):
        return self.num_clusters * self.num_sequences

    def __getitem__(self, idx):
        cluster_idx = idx // self.num_sequences
        seq_idx = idx % self.num_sequences
        sequence = self.data[cluster_idx][seq_idx]

        return sequence, cluster_idx
```

## Neural Network Model

Next, we need to define a neural network model that will learn to cluster the time series data. For simplicity, we'll use a simple feed-forward neural network with one hidden layer. The network takes each time series sequence as input and outputs a cluster assignment.

```python
import torch.nn as nn
import torch.nn.functional as F

class TimeSeriesClusteringModel(nn.Module):
    def __init__(self, input_size, hidden_size, num_clusters):
        super(TimeSeriesClusteringModel, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, num_clusters)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x
```

## Training the Model

Now let's train the model using the time series data. We'll use the KMeans clustering algorithm as a reference to evaluate the performance of our PyTorch-based model.

```python
import torch.optim as optim
from sklearn.cluster import KMeans

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
input_size = 20
hidden_size = 64
num_clusters = 3

# Create the dataset
dataset = TimeSeriesDataset(num_clusters, num_sequences=100)
dataloader = torch.utils.data.DataLoader(dataset, batch_size=8, shuffle=True)

# Create the model
model = TimeSeriesClusteringModel(input_size, hidden_size, num_clusters)
model.to(device)

# Define the optimizer and loss function
optimizer = optim.Adam(model.parameters(), lr=0.001)
criterion = nn.CrossEntropyLoss()

# Training loop
for epoch in range(10):
    for sequences, targets in dataloader:
        sequences = sequences.to(device)
        targets = targets.to(device)

        # Zero the gradients
        optimizer.zero_grad()

        # Forward pass
        outputs = model(sequences)

        # Compute the loss
        loss = criterion(outputs, targets)

        # Backward pass and optimization
        loss.backward()
        optimizer.step()

# Evaluate the model
with torch.no_grad():
    model.eval()

    # Generate predictions
    predictions = model(dataset.data.view(-1, input_size).to(device))

    # Cluster assignments using KMeans
    kmeans = KMeans(n_clusters=num_clusters)
    kmeans.fit(dataset.data.view(-1, input_size))

    # Calculate accuracy
    pytorch_accuracy = torch.sum(predictions.argmax(dim=1) == torch.from_numpy(kmeans.labels_).to(device)) / len(predictions)
```

## Conclusion

In this blog post, we demonstrated how to use PyTorch for time series data clustering. By leveraging PyTorch's tensor operations and neural network capabilities, we can build a model that learns to group similar time series sequences together. Although the example provided is simple, it serves as a starting point for more advanced time series clustering tasks.

#AI #MachineLearning