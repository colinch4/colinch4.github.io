---
layout: post
title: "PyTorch for document classification"
description: " "
date: 2023-09-14
tags: [PyTorch, DocumentClassification]
comments: true
share: true
---

Document classification is a common task in natural language processing (NLP) where the goal is to assign a label or category to a given document based on its content. PyTorch, a popular deep learning framework, provides powerful tools and libraries that can be leveraged for document classification tasks. In this blog post, we will explore how to use PyTorch for document classification.

## Data Preprocessing

The first step in any NLP task is data preprocessing. This typically involves cleaning the text data, tokenizing it, and converting it into a numerical representation that can be fed into a deep learning model. In PyTorch, the `torchtext` library provides convenient functions for handling text data preprocessing. With `torchtext`, you can easily load, preprocess, and split your dataset into training, validation, and testing sets.

```python
import torchtext
from torchtext.datasets import AG_NEWS
from torchtext.data.utils import get_tokenizer

tokenizer = get_tokenizer("basic_english")

train_dataset, test_dataset = AG_NEWS(root="data")

# Define the fields for input text and labels
TEXT = torchtext.data.Field(tokenize=tokenizer, lower=True, batch_first=True, fix_length=256)
LABEL = torchtext.data.LabelField(dtype=torch.float)

train_data, test_data = torchtext.datasets.TabularDataset.splits(
    path="data",
    train="train.csv",
    test="test.csv",
    format="csv",
    fields=[("label", LABEL), ("text", TEXT)]
)

# Build the vocabulary
TEXT.build_vocab(train_dataset, min_freq=5, vectors="glove.6B.100d")
LABEL.build_vocab(train_dataset)
```

Here, we use the `AG_NEWS` dataset from `torchtext.datasets` as an example. We also define the tokenizer function using `get_tokenizer` from `torchtext.data.utils`. We then create `Text` and `Label` fields to preprocess the input text and labels respectively. After loading the train and test datasets, we build the vocabulary using the `build_vocab` function, specifying the minimum frequency and the pre-trained word embeddings to use.

## Model Architecture

For document classification, a common approach is to use a recurrent neural network (RNN) or a convolutional neural network (CNN) to capture sequence or local context information from the text. In PyTorch, you can easily define and train your custom model using the `torch.nn` module.

```python
import torch.nn as nn

class DocumentClassifier(nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_dim, output_dim, num_layers):
        super(DocumentClassifier, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.rnn = nn.GRU(embedding_dim, hidden_dim, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_dim, output_dim)
        
    def forward(self, text):
        embedded = self.embedding(text)
        _, hidden = self.rnn(embedded)
        return self.fc(hidden[-1])
```

In this example, we create a simple RNN-based document classifier using the `GRU` module from `torch.nn`. The input text is first embedded using an `Embedding` layer, passed through the RNN layer, and then the final hidden state is fed into a linear layer for classification.

## Training and Evaluation

Once we have the data preprocessing and model architecture in place, we can train and evaluate our document classifier using PyTorch's training loop.

```python
import torch.optim as optim

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = DocumentClassifier(len(TEXT.vocab), embedding_dim=100, hidden_dim=256, output_dim=4, num_layers=2).to(device)
optimizer = optim.Adam(model.parameters(), lr=0.001)
criterion = nn.CrossEntropyLoss()

train_iterator, test_iterator = torchtext.data.BucketIterator.splits(
    (train_dataset, test_dataset),
    batch_size=64,
    device=device
)

def train(model, iterator, optimizer, criterion):
    model.train()
    for batch in iterator:
        optimizer.zero_grad()
        text = batch.text.to(device)
        labels = batch.label.to(device)
        predictions = model(text).squeeze(1)
        loss = criterion(predictions, labels.long())
        loss.backward()
        optimizer.step()

def evaluate(model, iterator, criterion):
    model.eval()
    epoch_loss = 0
    with torch.no_grad():
        for batch in iterator:
            text = batch.text.to(device)
            labels = batch.label.to(device)
            predictions = model(text).squeeze(1)
            loss = criterion(predictions, labels.long())
            epoch_loss += loss.item()
    return epoch_loss / len(iterator)

for epoch in range(num_epochs):
    train(model, train_iterator, optimizer, criterion)
    val_loss = evaluate(model, val_iterator, criterion)
    print(f"Epoch: {epoch+1}/{num_epochs} | Val Loss: {val_loss}")
```

In the training loop, we iterate over the training data batches, calculate the forward pass, compute the loss using the criterion (cross-entropy loss), perform backpropagation, and update the model parameters using Adam optimizer. We also evaluate the model on the validation set after each epoch. Finally, we print the validation loss.

## Conclusion

In this blog post, we explored how to use PyTorch for document classification. We covered data preprocessing, model architecture, training, and evaluation steps. PyTorch's flexibility and powerful libraries make it an excellent choice for building deep learning models for document classification and other NLP tasks. With the example code provided, you can get started with document classification using PyTorch and adapt it according to your specific requirements. 

#PyTorch #DocumentClassification