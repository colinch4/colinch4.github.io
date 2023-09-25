---
layout: post
title: "Implementing sentiment analysis models in PyTorch"
description: " "
date: 2023-09-25
tags: [sentimentanalysis, PyTorch]
comments: true
share: true
---

Sentiment analysis is a natural language processing task that involves determining the sentiment or opinion expressed in a given piece of text. PyTorch, a popular deep learning framework, offers a powerful and flexible platform for building sentiment analysis models. In this blog post, we will explore how to implement sentiment analysis models in PyTorch.

## Preparing the Data

To get started, we need a dataset for training and testing our sentiment analysis models. We can use the IMDb movie review dataset, which consists of movie reviews labeled as positive or negative.

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torchtext.datasets import IMDB
from torchtext.data import Field, LabelField, BucketIterator

# Define the fields for preprocessing
TEXT = Field(tokenize='spacy', lower=True)
LABEL = LabelField(dtype=torch.float)

# Load the IMDb dataset
train_data, test_data = IMDB.splits(TEXT, LABEL)

# Build the vocabulary
TEXT.build_vocab(train_data, max_size=25000, vectors='glove.6B.100d')
LABEL.build_vocab(train_data)

# Create iterators for batching the data
train_iterator, test_iterator = BucketIterator.splits(
    (train_data, test_data),
    batch_size=64,
    device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')
)
```

In the code snippet above, we define the `TEXT` and `LABEL` fields for preprocessing the text and labels, respectively. The IMDb dataset is loaded using the `IMDB.splits()` function from the `torchtext.datasets` module.

Next, we build the vocabulary by passing the training data to the `build_vocab()` method of each field. We set the `max_size` parameter to limit the vocabulary size and load pre-trained word embeddings using the `vectors` parameter.

Finally, we create iterators using `BucketIterator.splits()` to efficiently batch the data for training and testing. The `device` parameter ensures that the data is transferred to the GPU if available.

## Building the Model

Now that we have prepared the data, we can proceed to build our sentiment analysis model using PyTorch.

```python
class SentimentClassifier(nn.Module):
    def __init__(self, input_dim, embedding_dim, hidden_dim, output_dim, dropout):
        super().__init__()

        self.embedding = nn.Embedding(input_dim, embedding_dim)
        self.rnn = nn.LSTM(embedding_dim, hidden_dim, num_layers=2, bidirectional=True, dropout=dropout)
        self.fc = nn.Linear(hidden_dim * 2, output_dim)
        self.dropout = nn.Dropout(dropout)

    def forward(self, text):
        embedded = self.dropout(self.embedding(text))
        output, (hidden, cell) = self.rnn(embedded)
        hidden = self.dropout(torch.cat((hidden[-2, :, :], hidden[-1, :, :]), dim=1))
        return self.fc(hidden.squeeze(0))
```

The code snippet above shows the implementation of a simple sentiment classifier using a bidirectional LSTM (Long Short-Term Memory) model. The class `SentimentClassifier` extends `nn.Module` and defines the layers and operations required for the model.

The `__init__` method initializes the layers including the embedding layer, LSTM layer, and linear layer. The `forward` method defines the forward pass of the model, where the text is first embedded, passed through the LSTM layer, and the final hidden state is fed into the linear layer for classification.

## Training and Evaluation

With the model defined, we can now move on to training and evaluating our sentiment analysis model.

```python
def train(model, iterator, optimizer, criterion):
    model.train()
    
    epoch_loss = 0
    epoch_acc = 0
    
    for batch in iterator:
        optimizer.zero_grad()
        
        text, labels = batch.text, batch.label
        predictions = model(text).squeeze(1)
        
        loss = criterion(predictions, labels)
        acc = binary_accuracy(predictions, labels)
        
        loss.backward()
        optimizer.step()
        
        epoch_loss += loss.item()
        epoch_acc += acc.item()
    
    return epoch_loss / len(iterator), epoch_acc / len(iterator)


def evaluate(model, iterator, criterion):
    model.eval()
    
    epoch_loss = 0
    epoch_acc = 0
    
    with torch.no_grad():
        for batch in iterator:
            text, labels = batch.text, batch.label
            predictions = model(text).squeeze(1)
            
            loss = criterion(predictions, labels)
            acc = binary_accuracy(predictions, labels)
            
            epoch_loss += loss.item()
            epoch_acc += acc.item()
    
    return epoch_loss / len(iterator), epoch_acc / len(iterator)


# Helper function for computing binary accuracy
def binary_accuracy(preds, y):
    rounded_preds = torch.round(torch.sigmoid(preds))
    correct = (rounded_preds == y).float()
    acc = correct.sum() / len(correct)
    return acc
```

The above code defines the `train`, `evaluate`, and `binary_accuracy` functions. The `train` function performs a single training epoch, updating the model weights based on the loss computed using binary cross-entropy. The `evaluate` function calculates the loss and accuracy on the test set. The `binary_accuracy` function computes the accuracy of the predictions.

## Putting It All Together

To complete the sentiment analysis pipeline, we need to initialize the model, define the loss function and optimizer, and train and evaluate the model.

```python
# Initialize the model
INPUT_DIM = len(TEXT.vocab)
EMBEDDING_DIM = 100
HIDDEN_DIM = 256
OUTPUT_DIM = 1
DROPOUT = 0.5

model = SentimentClassifier(INPUT_DIM, EMBEDDING_DIM, HIDDEN_DIM, OUTPUT_DIM, DROPOUT)

# Define the loss function and optimizer
criterion = nn.BCEWithLogitsLoss()
optimizer = optim.Adam(model.parameters())

# Train and evaluate the model
N_EPOCHS = 5

for epoch in range(N_EPOCHS):
    train_loss, train_acc = train(model, train_iterator, optimizer, criterion)
    test_loss, test_acc = evaluate(model, test_iterator, criterion)
    
    print(f'Epoch: {epoch+1} | Train Loss: {train_loss:.3f} | Train Acc: {train_acc*100:.2f}%')
    print(f'Epoch: {epoch+1} | Test Loss: {test_loss:.3f} | Test Acc: {test_acc*100:.2f}%')
```

In the final code snippet, we initialize the model with the chosen hyperparameters, define the loss function and optimizer, and then train and evaluate the sentiment analysis model for a specified number of epochs. The train and test loss and accuracy are printed for each epoch.

# Conclusion

In this blog post, we have covered the implementation of sentiment analysis models in PyTorch. We started by preparing the data using the IMDb movie review dataset and then built a sentiment classifier model using a bidirectional LSTM. Finally, we trained and evaluated our model on the IMDb dataset. PyTorch's flexibility and simplicity make it an excellent choice for implementing and training sentiment analysis models. #sentimentanalysis #PyTorch