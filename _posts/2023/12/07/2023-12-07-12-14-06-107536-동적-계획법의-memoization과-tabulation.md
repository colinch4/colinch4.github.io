---
layout: post
title: "[python] 동적 계획법의 memoization과 tabulation"
description: " "
date: 2023-12-07
tags: [python]
comments: true
share: true
---

동적 계획법(Dynamic Programming)은 문제를 작은 하위 문제(subproblem)로 쪼개어 해결하는 알고리즘 기법입니다. 이때, 중복되는 계산을 효율적으로 처리하기 위해 메모이제이션(memoization)과 타뷸레이션(tabulation)이라는 두 가지 기법을 사용합니다.

## 메모이제이션 (Memoization)

메모이제이션은 중복되는 계산을 방지하기 위해 이전에 계산한 값을 저장하는 기법입니다. 이를 통해 동일한 인자로 호출되었을 때, 이전에 계산한 값을 바로 반환하여 중복된 계산을 피할 수 있습니다.

예를 들어, 피보나치 수열을 계산하는 함수를 메모이제이션을 사용하여 구현해보겠습니다.

```python
def fib(n, memo={}):
    if n <= 1:
        return n
    
    if n not in memo:
        memo[n] = fib(n-1) + fib(n-2)
    
    return memo[n]

print(fib(5))  # Output: 5
```

위 코드에서 `memo`는 기본값으로 빈 딕셔너리를 가지고 있습니다. 정수 `n`을 인자로 받아 피보나치 수열의 `n`번째 값을 반환하는 함수인 `fib`에서, 이전에 계산한 값들을 `memo`에 저장하도록 구현되어 있습니다. 이미 계산한 값이 `memo`에 존재할 경우, 이를 반환하고 없을 경우에만 계산하고 `memo`에 저장합니다.

## 타뷸레이션 (Tabulation)

타뷸레이션은 중복되는 계산을 피하기 위해 이미 계산한 결과를 테이블에 저장하는 기법입니다. 타뷸레이션은 메모이제이션과 달리, 작은 하위 문제부터 차례대로 계산하여 테이블에 저장하기 때문에 반복문을 사용하여 구현됩니다.

동일한 피보나치 예제에서 타뷸레이션을 사용하여 구현해보겠습니다.

```python
def fib(n):
    table = [0] * (n+1)
    table[1] = 1

    for i in range(2, n+1):
        table[i] = table[i-1] + table[i-2]
    
    return table[n]

print(fib(5))  # Output: 5
```

위 코드에서 `table`은 크기가 `n+1`인 리스트입니다. 첫 번째 원소를 0으로 초기화하고, 두 번째 원소를 1로 초기화합니다. 그리고 반복문을 통해 `table` 배열에 작은 하위 문제부터 차례대로 값을 계산하여 저장합니다. 마지막으로 `table[n]` 값을 반환합니다.

## 결론

동적 계획법은 중복되는 계산을 피하고 효율적인 알고리즘을 구현하는데 매우 유용한 기법입니다. 메모이제이션과 타뷸레이션은 동적 계획법의 핵심 기법으로, 중복 계산을 피하기 위해 이전 결과를 저장하거나 테이블에 저장하여 사용합니다. 상황에 맞게 적절한 방법을 선택하여 문제를 해결할 수 있습니다.

## 참고 자료

- [Dynamic Programming - GeeksforGeeks](https://www.geeksforgeeks.org/dynamic-programming/)
- [Memoization vs. Tabulation in Dynamic Programming - GeeksforGeeks](https://www.geeksforgeeks.org/tabulation-vs-memoization/)