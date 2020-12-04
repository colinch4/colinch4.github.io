---
layout: post
title: "[Tensorflow] Tensorflow 기본 프로그래밍"
description: " "
date: 2020-12-04
tags: [Tensorflow]
comments: true
share: true
---

# Tensorflow 기본 프로그래밍

>**TF2.x**의 기본 구현 방법에 대해서 알아본다.

* 버전 확인

```python
import tensorflow as tf
print(tf.__version__)
# 2.1.0
```



* random 값 & 출력 : `Session`없이 출력 가능하다.

```python
random = tf.random.normal([1], dtype=tf.float32)
print(random)
# tf.Tensor([-1.5870395], shape=(1,), dtype=float32)
print(random.numpy())
# [-1.5870395]
```



* constant

```python
a = tf.constant(10, dtype=tf.float32)
b = tf.constant(20, dtype=tf.float32)

c = a+b
print(c)
# tf.Tensor(30.0, shape=(), dtype=float32)
print(c.numpy())
# 30.0
```



* convert_to_tensor : tensor로 전환하지 않아도 연산이 되지만 `convert_to_tensorf`를 이용해 변형해주는 편이 낫다.

```python
a = tf.constant(10, dtype=tf.float32) 
d = 30
print((a+d).numpy())        # 40
tensor_d = tf.convert_to_tensorf(d)
print((a+tensor_d).numpy()) # 40
```



* Variable : 더이상 `tf.global_variabls_initializer()`를 실행하지 않아도 된다.

```python
w = tf.Variable(tf.random.normal([1]), name='weight')
print(w.numpy())
# [0.966355]
```



* Lazy execution이었던 placeholder는 삭제 되었다.



