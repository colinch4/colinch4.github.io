---
layout: post
title: "[python] Computation Thinking"
description: " "
date: 2021-06-18
tags: [python]
comments: true
share: true
---

# Computation Thinking

## 1. 기초 수식

### 1.1 문제 풀이

- 문제 1 : T(n) = T(n-1) + 1

  - ```shell
    T(0) = 1
    
    T(n) = T(n-1) + 1
    	 = T(n-2) + 1 + 1
    	 = T(n-3) + 1 + 1 + 1
    	 = T(n-k) + k
    	 = 'T(0) + k'
    	  n = k 인 경우 T(0) 이 된다
    	  
    T(n) = 1 + n
    
    따라서 O(n) 시간복잡도가 된다.
    ```

- 문제 2 : T(n) = T(n-1) + n

  - ```shell
    n > 0, n = 0
    
    T(n) = T(n-1) + n
    	 = T(n-2) + (n-1) + n
    	 = T(n-k) + ( n-(k-1) ) + ... + n
    	 = 'T(0) + 1 + ... + n'
    
    T(n) = T(0) + n(n+1)/2
    ```

- 문제 3 : T(n) = T(n-1) + log n

  - ```shell
    n > 0, n = 0
    
    T(n) = T(n-1) + log n
    	 = T(n-2) + log(n-1) + log n
    	 = T(n-3) + log(n-2) + log(n-1) + log n
    	 = T(n-k) + log(n-(k-1)) + ... + log(n-1) + log n
    	 = T(0) + log(1) + log(2) + ... + log(n)
    	 <= T(0) + log n + log n + ... + log n
    	 'T(0) + log(n!) <= T(0) + nlog n'
         
    O(nlog n)
    ```

- 문제 4 : T(n) = T(n/2) + 1

  - ```shell
    n > 0, n = 0
    
    T(n) = T(n/2) + 1
    	 = T(n-1/2) + 1
    ```

-  문제 5 : T(n) = T(n/2) + n

  - ```shell
    T(0) = 1, T(1) = 1
    n/2^k = 1
    n = 2^k
    k = log n
    
    T(n) = T(n/2) + n ( n>1 )
    	 = T(n/4) + n/2 + n
    	 = T(n/8) + n/4 + n/2 + n
    	 = T(n/2^k) + n/2^k-1 + ... + n/2 + n
    	 = T(1) + n / 2^log n -1
    
    O(n)
    ```



## 2. 재귀

> - 재귀란 자기 자신을 호출하는 함수, 그럼 끝날 수가 있는가?
> - 함수는 입력이 있으며, 자기 자신의 입력과 동일한 입력으로 자기 자신을 호출하면 당연히 끝나지않음
> - 하지만, 다른 입력으로 호출하면 끝날 수 있음



### 2.1 피보나치 수열

> ```python
> def fibo(n):
>     if n <= 2:
>         return 1
>     return fibo(n-1) + fibo(n-2)
> ```



### 2.2 Merge Sort

> 크기 n인 배열을 입력으로 받아, 배열을 절반으로 두개로 나눈 후,
>
> 각 작은 배열을 재귀적으로 정렬하고,
>
> 그 결과를 Merge 한다.



### 2.3 소팅 성공 증명

```java
Stupid (A[0..n-1])
{
    if n=2 and A[0] > A[1]
        then swap A[0] and A[1]
    else
        m = ceiling(2n/3)
        Stupid(A[0..m-1])
        Stupid(A[n-m..n-1])
        Stupid(A[0..m-1])
}
```



## 3. 동적 프로그래밍 (DP)

> Dynamic Programming (동적계획법)이란?
>
> - 큰 문제를 작은문제로 나누어 푸는 문제를 일컫는 말
> - 문제의 최적해를 구하거나, 답의 개수를 세는 과정에 사용할 수 있는 알고리즘 설계기법
> - ex) 피보나치 수열
>
> 재귀 함수에서 동일한 입력의 함수 호출이 반복적으로 일어날 때 그 결과 값을 저장해 두고 불러 쓰는 것이다.
>
> (Memoization)
>
> 최초 입력에서 파생되는 모든 가능한 입력에 대한 답을 모두 젖아할 수 있는 메모리가 있어야 한다.
>
> 단순히 재귀에서 저장된 값을 찾아보는 것으로도 가능하지만, 결과 값을 순서를 정해서 계산할 수도 있다.    (동적계획법)





재귀, 메모이제이션, 동적계획법

3가지 방법중에

`동적계획법` 이 실행시간이 가장 빠르다.