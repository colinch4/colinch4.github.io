---
layout: post
title: "Implementing VAEs in PyTorch"
description: " "
date: 2023-09-14
tags: [deeplearning]
comments: true
share: true
---

Variational Autoencoders (VAEs) are powerful deep learning models used for generative tasks. In this blog post, we will walk through the implementation of VAEs using PyTorch, a popular deep learning framework.

To get started, let's install the necessary dependencies:

```
pip install torch torchvision
```

Now, let's import the required libraries:

```python
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
```

Next, we define the encoder and decoder architectures. The encoder network takes an input image and maps it to a lower-dimensional latent space. The decoder network then reconstructs the original image from the latent space. Here's an example implementation:

```python
class Encoder(nn.Module):
    def __init__(self):
        super(Encoder, self).__init__()
        self.conv1 = nn.Conv2d(1, 16, kernel_size=3, stride=2, padding=1)
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, stride=2, padding=1)
        self.fc1 = nn.Linear(32 * 7 * 7, 256)
        self.fc_mu = nn.Linear(256, latent_dim)
        self.fc_logvar = nn.Linear(256, latent_dim)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.relu(self.conv1(x))
        x = self.relu(self.conv2(x))
        x = x.view(x.size(0), -1)
        x = self.relu(self.fc1(x))
        z_mu = self.fc_mu(x)
        z_logvar = self.fc_logvar(x)
        return z_mu, z_logvar


class Decoder(nn.Module):
    def __init__(self):
        super(Decoder, self).__init__()
        self.fc1 = nn.Linear(latent_dim, 256)
        self.fc2 = nn.Linear(256, 32 * 7 * 7)
        self.conv1 = nn.ConvTranspose2d(32, 16, kernel_size=4, stride=2, padding=1)
        self.conv2 = nn.ConvTranspose2d(16, 1, kernel_size=4, stride=2, padding=1)
        self.relu = nn.ReLU()
        self.sigmoid = nn.Sigmoid()

    def forward(self, z):
        x = self.relu(self.fc1(z))
        x = self.relu(self.fc2(x))
        x = x.view(x.size(0), 32, 7, 7)
        x = self.relu(self.conv1(x))
        x = self.sigmoid(self.conv2(x))
        return x
```

Now, let's define the VAE model that combines the encoder and decoder networks:

```python
class VAE(nn.Module):
    def __init__(self):
        super(VAE, self).__init__()
        self.encoder = Encoder()
        self.decoder = Decoder()

    def reparameterize(self, mu, logvar):
        std = torch.exp(0.5 * logvar)
        eps = torch.randn_like(std)
        z = mu + eps * std
        return z

    def forward(self, x):
        z_mu, z_logvar = self.encoder(x)
        z = self.reparameterize(z_mu, z_logvar)
        x_recon = self.decoder(z)
        return x_recon, z_mu, z_logvar
```

We can now define the loss function and training loop:

```python
reconstruction_loss = nn.BCELoss(reduction='sum')

def loss_function(x_recon, x, z_mu, z_logvar):
    BCE = reconstruction_loss(x_recon, x)
    KLD = -0.5 * torch.sum(1 + z_logvar - z_mu.pow(2) - z_logvar.exp())
    return BCE + KLD

vae = VAE()
optimizer = optim.Adam(vae.parameters(), lr=learning_rate)

def train():
    vae.train()
    train_loss = 0
    for batch_idx, (x, _) in enumerate(train_loader):
        optimizer.zero_grad()
        x_recon, z_mu, z_logvar = vae(x)
        loss = loss_function(x_recon, x, z_mu, z_logvar)
        loss.backward()
        train_loss += loss.item()
        optimizer.step()
    return train_loss / len(train_loader.dataset)

for epoch in range(num_epochs):
    train_loss = train()
    print(f"Epoch {epoch+1}/{num_epochs}, Loss: {train_loss:.4f}")
```

In this blog post, we learned how to implement VAEs in PyTorch. VAEs are powerful models for generative tasks, and with the help of PyTorch, we can easily create and train VAE models. By leveraging the encoder-decoder architecture and the reparameterization trick, VAEs can learn to generate new data samples from a latent space representation.

#deeplearning #python