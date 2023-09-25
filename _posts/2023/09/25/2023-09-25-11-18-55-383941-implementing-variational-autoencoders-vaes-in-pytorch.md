---
layout: post
title: "Implementing variational autoencoders (VAEs) in PyTorch"
description: " "
date: 2023-09-25
tags: [variationalautoencoders, deeplearning]
comments: true
share: true
---

In this blog post, we will learn how to implement Variational Autoencoders (VAEs) using PyTorch. VAEs are generative models that learn to approximate the true data distribution and can generate new samples similar to the input data.

## What are Variational Autoencoders?

Variational Autoencoders (VAEs) are a class of deep generative models and an extension of traditional autoencoders. They are capable of learning the underlying statistical distribution of the input data and generating new samples from this distribution.

Unlike traditional autoencoders, VAEs learn a latent vector representation for each input data point, which allows for sampling from this learned distribution. The model consists of an encoder that maps the input data to a latent space, and a decoder that reconstructs the input data from the latent space samples.

## Implementing VAE in PyTorch

Let's dive into the implementation of VAEs using PyTorch. We will cover the major components of the model: the encoder, the decoder, and the loss function.

### Importing the Required Libraries

First, let's import the necessary libraries for building the VAE.

```python
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
```

### The Encoder

The encoder takes the input data and maps it to the latent space by passing it through a series of neural network layers.

```python
class Encoder(nn.Module):
    def __init__(self, input_dim, hidden_dim, latent_dim):
        super(Encoder, self).__init__()
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.fc_mean = nn.Linear(hidden_dim, latent_dim)
        self.fc_logvar = nn.Linear(hidden_dim, latent_dim)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        mean = self.fc_mean(x)
        logvar = self.fc_logvar(x)
        return mean, logvar
```

### The Decoder

The decoder takes a latent vector from the encoder and reconstructs the input data.

```python
class Decoder(nn.Module):
    def __init__(self, latent_dim, hidden_dim, output_dim):
        super(Decoder, self).__init__()
        self.fc1 = nn.Linear(latent_dim, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = torch.sigmoid(self.fc2(x))
        return x
```

### The Variational Autoencoder

The VAE combines the encoder and decoder to form the complete model. It also includes a sample function to obtain a latent vector from the learned distribution.

```python
class VAE(nn.Module):
    def __init__(self, input_dim, hidden_dim, latent_dim):
        super(VAE, self).__init__()
        self.encoder = Encoder(input_dim, hidden_dim, latent_dim)
        self.decoder = Decoder(latent_dim, hidden_dim, input_dim)

    def sample_latent_vector(self, mean, logvar):
        epsilon = torch.randn_like(logvar)
        return mean + torch.exp(logvar / 2) * epsilon

    def forward(self, x):
        mean, logvar = self.encoder(x)
        z = self.sample_latent_vector(mean, logvar)
        reconstruction = self.decoder(z)
        return reconstruction, mean, logvar
```

### The Loss Function

The loss function for VAE consists of two parts: the reconstruction loss and the Kullback-Leibler (KL) divergence loss. The reconstruction loss measures the difference between the input data and the reconstructed output, while the KL divergence loss ensures the learned distribution is close to a unit Gaussian.

```python
def vae_loss(reconstruction, input_data, mean, logvar):
    reconstruction_loss = F.binary_cross_entropy(reconstruction, input_data, reduction='sum')
    kl_divergence_loss = -0.5 * torch.sum(1 + logvar - mean.pow(2) - logvar.exp())
    return reconstruction_loss + kl_divergence_loss
```

### Training the VAE

Now, let's train the VAE using the MNIST dataset as an example.

```python
# Load the MNIST dataset
train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=batch_size, shuffle=True)

# Initialize the VAE model
vae = VAE(input_dim, hidden_dim, latent_dim)
optimizer = optim.Adam(vae.parameters(), lr=learning_rate)

# Training loop
for epoch in range(num_epochs):
    for batch_idx, input_data in enumerate(train_loader):
        optimizer.zero_grad()
        reconstruction, mean, logvar = vae(input_data)
        loss = vae_loss(reconstruction, input_data, mean, logvar)
        loss.backward()
        optimizer.step()

        if batch_idx % log_interval == 0:
            print(f"Epoch {epoch+1}/{num_epochs}, Batch {batch_idx}/{len(train_loader)}, Loss: {loss.item():.4f}")

# Save the trained model
torch.save(vae.state_dict(), 'vae_model.pt')
```

## Conclusion

In this blog post, we have implemented a Variational Autoencoder (VAE) using PyTorch. VAEs are powerful generative models that can learn the underlying distribution of input data and generate new samples. By combining an encoder and decoder, we have trained the VAE using the MNIST dataset as an example.

By understanding VAEs and their implementation in PyTorch, you can further explore more complex variations and apply them to various domains.

#variationalautoencoders #deeplearning