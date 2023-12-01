---
layout: post
title: "[python] NumPy의 broadcasting 기능을 활용하여 배열의 shape을 조정하는 방법은 무엇인가요?"
description: " "
date: 2023-12-01
tags: [python]
comments: true
share: true
---

NumPy는 배열 간의 연산을 효율적으로 수행하기 위한 다양한 기능을 제공합니다. 그 중에서도 Broadcasting은 배열의 shape을 자동으로 조정하여 원소 간의 연산을 수행할 수 있게 해줍니다. Broadcasting을 사용하면 서로 다른 shape의 배열 간에도 연산을 쉽게 수행할 수 있습니다.

아래는 NumPy의 Broadcasting을 사용하여 배열의 shape을 조정하는 방법을 보여주는 예시 코드입니다.

```python
import numpy as np

# 1차원 배열과 스칼라 간의 연산
a = np.array([1, 2, 3])
b = 2
result = a * b
print(result)  # [2 4 6]

# 2차원 배열과 1차원 배열 간의 연산
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([1, 2, 3])
result = c + d
print(result)
# [[2 4 6]
#  [5 7 9]]

# 2차원 배열과 1차원 배열 간의 연산 (축 추가)
e = np.array([[1, 2, 3], [4, 5, 6]])
f = np.array([1, 2])
result = e + f[:, np.newaxis]
print(result)
# [[2 3 4]
#  [6 7 8]]
```

위의 코드에서는 Broadcasting을 사용하여 서로 다른 shape의 배열 간의 연산을 수행하고 있습니다. 첫 번째 예제에서는 1차원 배열과 스칼라 간의 곱셈을 수행하고 있으며, 두 번째 예제에서는 2차원 배열과 1차원 배열 간의 덧셈을 수행하고 있습니다. 마지막 예제에서는 2차원 배열과 1차원 배열 간의 덧셈을 수행하되, 1차원 배열의 shape에 새로운 축을 추가하여 연산을 수행하고 있습니다.

NumPy의 Broadcasting은 이처럼 배열의 shape을 조정하여 연산을 수행하는 강력한 기능입니다. 이를 잘 활용하면 복잡한 연산을 간단히 수행할 수 있으며, 코드의 가독성을 향상시킬 수 있습니다.

참고 자료:
- NumPy Broadcasting: https://numpy.org/doc/stable/user/basics.broadcasting.html