---
layout: post
title: "[programmers][알고리즘][level1] 피보나치 수"
description: "피보나치 수"
date: 2018-05-14
tags: [programmers, 알고리즘]
comments: true
share: true
---

피보나치 수는 F(0) = 0, F(1) = 1일 때, 2 이상의 n에 대하여 F(n) = F(n-1) + F(n-2) 가 적용되는 점화식입니다. 2 이상의 n이 입력되었을 때, fibonacci 함수를 제작하여 n번째 피보나치 수를 반환해 주세요. 예를 들어 n = 3이라면 2를 반환해주면 됩니다.


```c++
#include<iostream>
using namespace std;

int sumDivisor(int n)
{
    if ( n <= 0 ) return 0; 
    int sum = 0; 
    for ( int i = 1; i <= n; i++ ) 
    {
        int result = n % i; 
        if ( result == 0 ) sum += i;  
    }
	return sum;
}

int main()
{
	int testCase = 10;
	int testAnswer = sumDivisor(testCase);

	cout<<testAnswer;
}
```
