---
layout: post
title: "[python] GRU(Gated Recurrent Unit)"
description: " "
date: 2023-12-12
tags: [python]
comments: true
share: true
---

순환 신경망(Recurrent Neural Network, RNN)은 시계열 데이터나 자연어와 같은 순차적인 데이터를 처리하기 위한 머신 러닝 모델입니다. GRU(Gated Recurrent Unit)는 RNN의 변종 중 하나로, **장기 의존 관계(Long-term dependencies)를 학습하는데 어려움을 해결하기 위해** 제안되었습니다.

## GRU의 개념

GRU는 LSTM(Long Short-Term Memory)과 유사하게 **단기 기억과 장기 기억을 포함**하고 있습니다. 하지만, LSTM과 달리 **게이트(gate)의 개수가 줄어 메모리 셀을 간소화**하였습니다.

GRU 셀은 리셋 게이트(Reset Gate)와 업데이트 게이트(Update Gate)를 사용하여, 현재 입력값과 이전 상태의 정보를 이용하여 새로운 상태를 생성합니다. 이를 통해 **장기 의존 관계를 고려하면서도 매개변수의 수를 줄여 계산 비용을 낮추는 효과**를 가져왔습니다.

## GRU의 구조

GRU는 총 3개의 게이트를 사용합니다:
- **삭감 게이트(Reset Gate)**: 이전 상태와 현재 입력을 결합하여 어떤 정보를 버릴 지 결정합니다.
- **업데이트 게이트(Update Gate)**: 이전 상태를 얼마나 유지할 지를 결정합니다.
- **현재 상태 계산을 위한 tanh 레이어** 

이러한 간결한 구조 덕분에 GRU는 LSTM보다 **더 적은 계산 비용**으로 장기적인 의존 관계를 학습할 수 있습니다.

## GRU의 장점

GRU는 다음과 같은 장점을 가집니다:
- **LSTM보다 적은 파라미터**: 그 결과, **더 적은 계산 비용**으로 더 빠르게 학습 가능
- **장기 의존 관계 학습능력**: 반복적인 패턴을 학습하는 데 용이

## 예시: Keras를 사용한 GRU 모델 구축

```python
from keras.models import Sequential
from keras.layers import GRU, Dense

model = Sequential()
model.add(GRU(256, input_shape=(T, D)))
model.add(Dense(1))

model.compile(loss='mse', optimizer='adam', metrics=['accuracy'])
```

GRU는 RNN의 변종 중 하나로, **장기 의존 관계를 고려하면서도 LSTM보다 간단한 구조로 빠르게 학습**할 수 있는 장점을 갖고 있습니다. 이에 따라, **자연어 처리나 시계열 데이터 분석**과 같은 분야에서 활발하게 활용되고 있습니다.

## 참고 자료
- [Understanding GRU Networks](https://towardsdatascience.com/understanding-gru-networks-2ef37df6c9be)
- [On the Properties of Neural Machine Translation: Encoder-Decoder Approaches](https://arxiv.org/pdf/1409.1259.pdf)
- [Empirical Evaluation of Gated Recurrent Neural Networks on Sequence Modeling](https://arxiv.org/pdf/1412.3555.pdf)