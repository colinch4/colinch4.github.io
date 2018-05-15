---
layout: post
title: "[programmers][알고리즘][level2] 최소값 만들기"
description: "최소값 만들기"
date: 2018-05-15
tags: [programmers, 알고리즘]
comments: true
share: true
---

자연수로 이루어진 길이가 같은 수열 A,B가 있습니다. 최솟값 만들기는 A, B에서 각각 한 개의 숫자를 뽑아 두 수를 곱한 값을 누적하여 더합니다. 이러한 과정을 수열의 길이만큼 반복하여 최종적으로 누적된 값이 최소가 되도록 만드는 것이 목표입니다.

예를 들어 A = [1, 2] , B = [3, 4] 라면

A에서 1, B에서 4를 뽑아 곱하여 더합니다.
A에서 2, B에서 3을 뽑아 곱하여 더합니다.
수열의 길이만큼 반복하여 최솟값 10을 얻을 수 있으며, 이 10이 최솟값이 됩니다.
수열 A,B가 주어질 때, 최솟값을 반환해주는 getMinSum 함수를 완성하세요.

```c++
#include<iostream>
using namespace std;

int numOfPrime(int n)
{
	int answer = 0;
    for ( int i = 2; i <= n; ++i )
    {
        int count = 0; 
        for ( int j = 2; j <= i; ++j ) 
        {
            if ( (i%j) == 0 ) ++count;
        }
        if ( count == 1 ) ++answer;
    }
	return answer;
}

int main()
{
	int testCase = 10;
	int testAnswer = numOfPrime(testCase);

	cout<<testAnswer;
}
```

정문교 님의 풀이
```
#include<iostream>
#include <vector>

using namespace std;

int numOfPrime(int n)
{
    if (n == 1) { return 0; }

    int answer = 0;
    vector<bool> vecIsPrime(n - 1, true);

    for (int i = 2; i <= n; ++i) {
        if (vecIsPrime[i - 2] == false) { continue; }

        for (int j = i * 2; j <= n; j += i) {
            vecIsPrime[j - 2] = false;
        }
    }

    for (int i = 0; i < vecIsPrime.size(); ++i) {
        if (vecIsPrime[i] == true) { ++answer; }
    }

    return answer;
}

int main()
{
    int testCase = 10;
    int testAnswer = numOfPrime(testCase);

    cout<<testAnswer;
}
```

