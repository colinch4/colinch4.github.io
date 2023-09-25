---
layout: post
title: "Implementing actor-critic algorithms in PyTorch"
description: " "
date: 2023-09-25
tags: [PyTorch]
comments: true
share: true
---

Actor-Critic algorithms are a popular class of reinforcement learning algorithms that combine the benefits of both value-based and policy-based methods. In this blog post, we will explore how to implement Actor-Critic algorithms using the PyTorch library.

## What are Actor-Critic Algorithms?

Actor-Critic algorithms are a type of policy gradient algorithms that consist of two main components: 

1. **Actor**: The actor is responsible for selecting actions based on the current policy.
2. **Critic**: The critic evaluates the quality of the selected actions and estimates the value of the current state.

The key idea behind Actor-Critic algorithms is that the actor learns from the critic's feedback to improve its policy iteratively. This allows the agent to explore the environment while also considering the learned value of each action.

## Setting up the Environment

Before we jump into implementing the algorithms, let's set up the environment. We assume that you have already installed PyTorch and other necessary libraries. Let's import the required libraries and set up our environment:

```
import gym
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F

env = gym.make('CartPole-v1')
state_dim = env.observation_space.shape[0]
action_dim = env.action_space.n
```

Here, we import the necessary libraries, create an instance of the CartPole environment from OpenAI Gym, and define the dimensions of the state and action spaces.

## Actor-Critic Network Architecture

To implement the actor-critic algorithm, we need to define the neural network architecture for both the actor and the critic. Let's create a simple neural network for our example:

```
class ActorCritic(nn.Module):
    def __init__(self):
        super(ActorCritic, self).__init__()
        self.fc1 = nn.Linear(state_dim, 64)
        self.fc2 = nn.Linear(64, action_dim)
        self.fc3 = nn.Linear(64, 1)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        policy = F.softmax(self.fc2(x), dim=-1)
        value = self.fc3(x)
        return policy, value

model = ActorCritic()
optimizer = optim.Adam(model.parameters(), lr=0.001)
```

In this example, we define a simple feedforward neural network with two fully connected layers for the actor and one fully connected layer for the critic. The actor outputs a softmax probability distribution over the actions, while the critic estimates the value of the current state.

## Training the Actor-Critic Model

Now that we have set up the environment and defined the network architecture, let's move on to training the actor-critic model. We will use the Advantage Actor-Critic (A2C) algorithm for this example:

```
def compute_returns(rewards, gamma):
    returns = []
    R = 0
    for r in reversed(rewards):
        R = r + gamma * R
        returns.insert(0, R)
    return returns

def train(num_episodes, gamma):
    for ep in range(num_episodes):
        state = env.reset()
        log_probs = []
        values = []
        rewards = []

        while True:
            state = torch.FloatTensor(state)
            policy, value = model(state)

            action = policy.sample()
            log_prob = policy.log_prob(action)

            next_state, reward, done, _ = env.step(action.item())

            log_probs.append(log_prob)
            values.append(value)
            rewards.append(reward)

            state = next_state

            if done:
                returns = compute_returns(rewards, gamma)

                actor_loss = 0
                critic_loss = 0

                for log_prob, value, R in zip(log_probs, values, returns):
                    advantage = R - value.item()
                    actor_loss += -log_prob * advantage
                    critic_loss += F.smooth_l1_loss(value, torch.tensor([R]))

                optimizer.zero_grad()
                (actor_loss + critic_loss).backward()
                optimizer.step()

                break
```

In this training loop, we sample actions from the actor's policy, compute log probabilities and values, and store the rewards. At the end of each episode, we calculate the returns and use them for updating both the actor and critic networks. We then perform the gradient update on the combined loss of the actor and critic and continue training.

## Conclusion

In this blog post, we have implemented Actor-Critic algorithms using the PyTorch library. By combining value-based and policy-based methods, actor-critic algorithms can achieve good performance on various reinforcement learning tasks. Feel free to experiment with different network architectures, hyperparameters, and environments to further improve the performance of your agent.

#RL #PyTorch