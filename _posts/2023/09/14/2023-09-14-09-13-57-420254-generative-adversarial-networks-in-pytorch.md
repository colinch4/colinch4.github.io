---
layout: post
title: "Generative adversarial networks in PyTorch"
description: " "
date: 2023-09-14
tags: [GANs, PyTorch]
comments: true
share: true
---

## What are GANs?

GANs consist of two main components: a **generator** and a **discriminator**. The generator network generates fake data samples, while the discriminator network distinguishes between real and fake samples.

The generator takes random noise as input and generates a sample that aims to resemble the real data. The discriminator, on the other hand, tries to classify the input sample as real or fake. The two networks play a **minimax game**, where the generator aims to improve its ability to fool the discriminator, and the discriminator aims to become better at distinguishing real from fake samples.

## Implementing GANs in PyTorch

To implement GANs in PyTorch, we'll first define the generator and discriminator networks using the `nn.Module` class. Let's consider a simple example where we generate handwritten digits.

```python
import torch
import torch.nn as nn

class Generator(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(Generator, self).__init__()

        self.model = nn.Sequential(
            nn.Linear(input_dim, 128),
            nn.LeakyReLU(0.2),
            nn.Linear(128, 256),
            nn.LeakyReLU(0.2),
            nn.Linear(256, output_dim),
            nn.Tanh()
        )

    def forward(self, x):
        return self.model(x)

class Discriminator(nn.Module):
    def __init__(self, input_dim):
        super(Discriminator, self).__init__()

        self.model = nn.Sequential(
            nn.Linear(input_dim, 256),
            nn.LeakyReLU(0.2),
            nn.Dropout(0.3),
            nn.Linear(256, 128),
            nn.LeakyReLU(0.2),
            nn.Dropout(0.3),
            nn.Linear(128, 1),
            nn.Sigmoid()
        )

    def forward(self, x):
        return self.model(x)
```

In the above code, we define the generator and discriminator networks using fully connected (linear) layers. We utilize the LeakyReLU activation function for better gradient flow and introduce dropout layers to prevent overfitting.

Once the generator and discriminator networks are defined, we can train the GAN model. During training, we alternate between training the generator and discriminator networks. The generator aims to minimize the discriminator's error on fake samples, while the discriminator aims to maximize its error on fake samples.

## Training the GAN

To train the GAN, we create instances of the generator and discriminator networks and define the loss functions and optimizers.

```python
generator = Generator(input_dim=100, output_dim=28*28)
discriminator = Discriminator(input_dim=28*28)

loss_fn = nn.BCELoss()
gen_optimizer = torch.optim.Adam(generator.parameters(), lr=0.0002)
dis_optimizer = torch.optim.Adam(discriminator.parameters(), lr=0.0002)
```

In the above code, we initialize the generator and discriminator networks, choose the binary cross-entropy loss as the loss function, and use the Adam optimizer for both networks.

Next, we feed random noise to the generator, pass the generated samples to the discriminator, and compute the loss for both networks. We update the parameters of each network accordingly.

```python
num_epochs = 100
batch_size = 64

for epoch in range(num_epochs):
    for i, real_data in enumerate(dataloader):
        real_data = real_data.view(-1, 28*28)

        # Train discriminator
        dis_optimizer.zero_grad()
        fake_data = generator(torch.randn(batch_size, 100))
        dis_real_output = discriminator(real_data)
        dis_fake_output = discriminator(fake_data.detach())

        dis_real_loss = loss_fn(dis_real_output, torch.ones_like(dis_real_output))
        dis_fake_loss = loss_fn(dis_fake_output, torch.zeros_like(dis_fake_output))
        dis_loss = dis_real_loss + dis_fake_loss
        dis_loss.backward()
        dis_optimizer.step()

        # Train generator
        gen_optimizer.zero_grad()
        fake_data = generator(torch.randn(batch_size, 100))
        dis_fake_output = discriminator(fake_data)

        gen_loss = loss_fn(dis_fake_output, torch.ones_like(dis_fake_output))
        gen_loss.backward()
        gen_optimizer.step()

    print(f"Epoch [{epoch+1}/{num_epochs}], Discriminator Loss: {dis_loss.item()}, Generator Loss: {gen_loss.item()}")
```

In the training loop, we alternate between training the discriminator and generator networks. We compute the losses for the real and fake samples and update the discriminator and generator networks accordingly. We print the losses for each epoch to monitor the progress of the training.

## Conclusion

In this blog post, we explored how to implement Generative Adversarial Networks (GANs) using PyTorch. GANs are a powerful tool for generating new data samples that resemble a given dataset. We defined the generator and discriminator networks, trained the GAN model, and discussed the training process.

With GANs, we can generate realistic data samples for various tasks such as image synthesis, text generation, and even music generation. GANs have revolutionized the field of generative modeling and continue to find applications in many domains.

#GANs #PyTorch