---
layout: post
title: "[python] RNN(Recurrent Neural Network)"
description: " "
date: 2023-12-12
tags: [python]
comments: true
share: true
---

RNN(Recurrent Neural Network)는 신경망의 한 종류로, 순차적인 데이터를 처리하기에 적합한 구조를 갖고 있습니다. 특히 시계열 데이터와 자연어 처리에 많이 사용됩니다. RNN은 각 단계마다의 입력과 이전 단계의 출력을 함께 고려해 계산을 수행하며, 이를 통해 순차적인 정보를 학습하고 기억할 수 있습니다. 이러한 특성으로 RNN은 문장 생성, 번역, 감情 분석 등 다양한 응용에 사용됩니다.

## RNN의 구조

RNN은 입력, 은닉 상태(hidden state), 출력으로 구성되어 있습니다. 입력은 각 단계에서의 입력 데이터를 나타내고, 은닉 상태는 해당 단계까지의 정보를 담고 있는 벡터를 의미합니다. 그리고 출력은 각 단계에서의 출력값을 나타냅니다.

```python
import torch
import torch.nn as nn

# 입력 크기, 은닉 상태 크기, 출력 크기 정의
input_size = 10
hidden_size = 20
output_size = 5

# RNN 모델 정의
rnn = nn.RNN(input_size, hidden_size, output_size)
```

## RNN의 장단점

RNN은 시계열 데이터의 패턴을 학습하기에 적합하며, 입력과 출력의 길이에 제약이 없어 다양한 형태의 데이터를 처리할 수 있습니다. 하지만 RNN은 긴 시퀀스의 정보를 기억하기 어렵다는 단점이 있습니다. 이를 해결하기 위해 LSTM(Long Short-Term Memory)과 GRU(Gated Recurrent Unit) 같은 RNN의 변종이 개발되었습니다.

## 결론

RNN은 순차적인 정보를 처리하는데 유용한 신경망 구조입니다. 시계열 데이터나 자연어 처리와 같은 영역에서 널리 사용되며, LSTM과 GRU와 같은 변종 모델을 통해 기존의 단점을 극복하고 더 나은 성능을 발휘하고 있습니다.

## 참고 자료
- [Understanding LSTM Networks](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)
- [Gated Recurrent Unit (GRU)](https://towardsdatascience.com/understanding-gru-networks-2ef37df6c9be)