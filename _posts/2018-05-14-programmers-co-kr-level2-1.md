---
layout: post
title: "[programmers][알고리즘][level2]소수 찾기"
description: "소수 찾기"
date: 2018-05-14
tags: [programmers, 알고리즘]
comments: true
share: true
---

numberOfPrime 메소드는 정수 n을 매개변수로 입력받습니다.

1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하도록 numberOfPrime 메소드를 만들어 보세요.

소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
(1은 소수가 아닙니다.)

10을 입력받았다면, 1부터 10 사이의 소수는 [2,3,5,7] 4개가 존재하므로 4를 반환
5를 입력받았다면, 1부터 5 사이의 소수는 [2,3,5] 3개가 존재하므로 3를 반환

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
```c++
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

