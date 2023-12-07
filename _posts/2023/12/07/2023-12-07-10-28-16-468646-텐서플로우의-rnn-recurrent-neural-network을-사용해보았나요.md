---
layout: post
title: "[python] 텐서플로우의 RNN (Recurrent Neural Network)을 사용해보았나요?"
description: " "
date: 2023-12-07
tags: [python]
comments: true
share: true
---

가장 기본적인 RNN 모델은 `tf.keras.layers.SimpleRNN` 클래스를 사용하여 생성할 수 있습니다. 이 클래스는 하나의 RNN 층을 나타내며, 시퀀스를 받아 순차적으로 처리한 후 결과를 반환합니다. 간단한 예시를 통해 사용법을 살펴보겠습니다.

```python
import tensorflow as tf

# 입력 데이터의 shape은 (batch_size, timesteps, input_dim)이어야 합니다.
inputs = tf.keras.Input(shape=(timesteps, input_dim))
# RNN 층 생성
rnn = tf.keras.layers.SimpleRNN(hidden_units, return_sequences=False)(inputs)
# 출력 레이어 생성
outputs = tf.keras.layers.Dense(output_dim, activation='softmax')(rnn)

# 모델 생성
model = tf.keras.Model(inputs=inputs, outputs=outputs)

# 모델 컴파일
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# 모델 학습
model.fit(x_train, y_train, epochs=num_epochs, batch_size=batch_size)
```

이 예시에서는 입력 데이터의 shape이 (batch_size, timesteps, input_dim) 형태이어야 합니다. `timesteps`는 시퀀스의 길이를 나타내며, `input_dim`은 시퀀스 데이터의 각 원소의 차원을 의미합니다. 예를 들어, 자연어 처리에서는 `timesteps`가 문장의 단어 개수에 해당하고, `input_dim`이 단어 임베딩 벡터의 차원입니다.

RNN 층 다음에는 출력 레이어를 추가하여 모델의 최종 출력을 만들어줍니다. 여기서 주의할점은 `return_sequences` 매개변수입니다. 이 값이 `False`로 설정되면 RNN 층은 마지막 시간 스텝의 출력만 반환하며, `True`로 설정되면 모든 시간 스텝의 출력을 반환합니다.

모델을 컴파일하고 학습시키기 위해 손실 함수와 최적화 알고리즘을 설정한 후 `model.fit()` 메서드를 호출하여 학습을 진행할 수 있습니다.

텐서플로우의 RNN API는 이 외에도 LSTM, GRU와 같은 다른 종류의 RNN 모델도 지원하고 있습니다. 더 복잡한 RNN 모델을 구성하고 싶다면 이러한 API를 활용해보세요.