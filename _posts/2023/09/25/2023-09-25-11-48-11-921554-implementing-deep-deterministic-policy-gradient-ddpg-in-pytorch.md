---
layout: post
title: "Implementing deep deterministic policy gradient (DDPG) in PyTorch"
description: " "
date: 2023-09-25
tags: []
comments: true
share: true
---

## Introduction

In this blog post, we will walk through the implementation of the **Deep Deterministic Policy Gradient (DDPG)** algorithm in PyTorch. DDPG is an off-policy actor-critic algorithm that can be used for continuous control tasks.

## Background

DDPG is an extension of the **Deterministic Policy Gradient (DPG)** algorithm, which combines the benefits of policy-based and value-based methods. DPG is suitable for continuous action spaces, as it learns a deterministic policy instead of a probabilistic one.

The core idea behind DDPG is to use an **actor-critic** architecture, where the actor learns the optimal policy, and the critic learns to evaluate the action-value function. The actor is updated by maximizing the expected return, while the critic is updated by minimizing the **mean squared Bellman error**.

## Implementation

To implement DDPG in PyTorch, we need to define the following components:

### 1. Actor Network

The actor network takes the current state as input and outputs the corresponding action. It is trained to maximize the expected return. We can define the actor network as follows:

```
import torch
import torch.nn as nn
import torch.nn.functional as F

class Actor(nn.Module):
    def __init__(self, input_dim, output_dim, hidden_dim):
        super(Actor, self).__init__()
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, hidden_dim)
        self.fc3 = nn.Linear(hidden_dim, output_dim)
        
    def forward(self, state):
        x = F.relu(self.fc1(state))
        x = F.relu(self.fc2(x))
        x = torch.tanh(self.fc3(x))
        return x
```

### 2. Critic Network

The critic network takes the current state and action as input and outputs the corresponding action-value function. It is trained to minimize the mean squared Bellman error. We can define the critic network as follows:

```
class Critic(nn.Module):
    def __init__(self, input_dim, output_dim, hidden_dim):
        super(Critic, self).__init__()
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim + output_dim, hidden_dim)
        self.fc3 = nn.Linear(hidden_dim, 1)
        
    def forward(self, state, action):
        x = F.relu(self.fc1(state))
        x = torch.cat([x, action], dim=1)
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x
```

### 3. Replay Buffer

The replay buffer stores the experiences (state, action, reward, next state) for training the networks. It helps to break the sequential correlation in the data and improves training stability. We can define the replay buffer as follows:

```
class ReplayBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []
        self.position = 0
        
    def push(self, state, action, reward, next_state):
        if len(self.buffer) < self.capacity:
            self.buffer.append(None)
        self.buffer[self.position] = (state, action, reward, next_state)
        self.position = (self.position + 1) % self.capacity
        
    def sample(self, batch_size):
        batch = random.sample(self.buffer, batch_size)
        state, action, reward, next_state = zip(*batch)
        return torch.cat(state), torch.cat(action), torch.cat(reward), torch.cat(next_state)
```

### 4. DDPG Agent

The DDPG agent ties all the components together: it uses the actor network to select actions, the critic network to evaluate actions, and the replay buffer to store and sample experiences. We can define the DDPG agent as follows:

```
class DDPGAgent:
    def __init__(self, state_dim, action_dim, hidden_dim, buffer_capacity, batch_size, gamma, tau, learning_rate):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.actor = Actor(state_dim, action_dim, hidden_dim).to(self.device)
        self.critic = Critic(state_dim, action_dim, hidden_dim).to(self.device)
        self.target_actor = Actor(state_dim, action_dim, hidden_dim).to(self.device).eval()
        self.target_critic = Critic(state_dim, action_dim, hidden_dim).to(self.device).eval()
        self.target_actor.load_state_dict(self.actor.state_dict())
        self.target_critic.load_state_dict(self.critic.state_dict())
        self.replay_buffer = ReplayBuffer(buffer_capacity)
        self.batch_size = batch_size
        self.gamma = gamma
        self.tau = tau
        self.actor_optimizer = torch.optim.Adam(self.actor.parameters(), lr=learning_rate)
        self.critic_optimizer = torch.optim.Adam(self.critic.parameters(), lr=learning_rate)
        
    def select_action(self, state):
        state = torch.FloatTensor(state).unsqueeze(0).to(self.device)
        action = self.actor(state).cpu().data.numpy().flatten()
        return action
    
    def update_networks(self):
        state, action, reward, next_state = self.replay_buffer.sample(self.batch_size)
        target_actions = self.target_actor(next_state)
        target_values = self.target_critic(next_state, target_actions).detach()
        target_q_values = reward + self.gamma * target_values
        current_q_values = self.critic(state, action)
        critic_loss = F.mse_loss(current_q_values, target_q_values)
        self.critic_optimizer.zero_grad()
        critic_loss.backward()
        self.critic_optimizer.step()

        policy_loss = -self.critic(state, self.actor(state)).mean()
        self.actor_optimizer.zero_grad()
        policy_loss.backward()
        self.actor_optimizer.step()

        for target_param, param in zip(self.target_critic.parameters(), self.critic.parameters()):
            target_param.data.copy_(self.tau * param.data + (1 - self.tau) * target_param.data)
        for target_param, param in zip(self.target_actor.parameters(), self.actor.parameters()):
            target_param.data.copy_(self.tau * param.data + (1 - self.tau) * target_param.data)
```

## Conclusion

In this blog post, we have implemented the Deep Deterministic Policy Gradient (DDPG) algorithm in PyTorch. DDPG is a powerful algorithm for continuous control tasks and can be used to learn optimal policies in complex environments. By defining the actor network, critic network, replay buffer, and DDPG agent, we can build a robust DDPG implementation.