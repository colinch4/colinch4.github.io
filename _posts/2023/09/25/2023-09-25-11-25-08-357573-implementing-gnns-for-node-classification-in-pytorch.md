---
layout: post
title: "Implementing GNNs for node classification in PyTorch"
description: " "
date: 2023-09-25
tags: []
comments: true
share: true
---

Graph Neural Networks (GNNs) have emerged as a powerful approach for node-level predictions in graph-structured data. GNNs have proven to be highly effective in tasks such as node classification, where the goal is to assign a label to each node in a given graph.

In this blog post, we will walk through the process of implementing a GNN for node classification using PyTorch, a popular deep learning framework. We will discuss the key components and steps involved in building a GNN model and provide example code for each step.

## Importing Required Libraries

Before we dive into the implementation, let's first import the necessary libraries:

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
```

## Defining the GNN Model

The first step in implementing a GNN for node classification is defining the GNN model architecture. A typical GNN consists of several graph convolutional layers, followed by non-linear activation functions. Each graph convolutional layer updates the node features by aggregating information from the node's neighbors.

Here's an example implementation of a simple GNN model using two graph convolutional layers:

```python
class GNNModel(nn.Module):
    def __init__(self, num_features, hidden_size, num_classes):
        super(GNNModel, self).__init__()
        self.conv1 = GraphConvolution(num_features, hidden_size)
        self.conv2 = GraphConvolution(hidden_size, num_classes)

    def forward(self, x, adj):
        x = F.relu(self.conv1(x, adj))
        x = self.conv2(x, adj)
        return x
```

## Implementing Graph Convolutional Layer

To implement the graph convolutional layer, we define a custom `GraphConvolution` class that performs the aggregation of node information. This class takes the input node features, the adjacency matrix, and applies a weight matrix to update the node features.

Here's an example implementation of the `GraphConvolution` class:

```python
class GraphConvolution(nn.Module):
    def __init__(self, input_size, output_size):
        super(GraphConvolution, self).__init__()
        self.weight = nn.Parameter(torch.FloatTensor(input_size, output_size))
        self.bias = nn.Parameter(torch.FloatTensor(output_size))

    def forward(self, x, adj):
        x = torch.matmul(adj, x)
        x = torch.matmul(x, self.weight) + self.bias
        return x
``` 

## Training and Evaluating the Model

Once the GNN model is defined, we can proceed with training and evaluating the model. This involves defining a loss function, optimizer, and training loop. In this example, we will use the cross-entropy loss and the Adam optimizer.

Here's an example code snippet to train and evaluate the GNN model:

```python
# Define loss function and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

# Training loop
for epoch in range(num_epochs):
    model.train()
    output = model(features, adjacency_matrix)
    loss = criterion(output[train_mask], labels[train_mask])

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

# Evaluation
model.eval()
with torch.no_grad():
    output = model(features, adjacency_matrix)
    predicted_labels = torch.argmax(output, dim=1)
    accuracy = (predicted_labels[val_mask] == labels[val_mask]).sum().item() / val_mask.sum().item()

print(f"Validation Accuracy: {accuracy}")
```

## Conclusion

In this blog post, we have implemented a Graph Neural Network (GNN) for node classification in PyTorch. We have discussed the key steps involved in building a GNN model, including defining the architecture, implementing the graph convolutional layer, and training the model.

By utilizing GNNs, we can effectively leverage the graph structure to improve node-level predictions in various domains such as social network analysis, recommendation systems, and drug discovery.

Keep in mind that this is just a basic implementation of GNNs for node classification, and there are more advanced techniques and variations to explore.