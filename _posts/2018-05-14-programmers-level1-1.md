---
layout: post
title: "[programmers][알고리즘][level1] 약수의 합"
description: "약수의 합"
date: 2018-05-14
tags: [programmers, 알고리즘]
comments: true
share: true
---

어떤 수를 입력받아 그 수의 약수를 모두 더한 수 sumDivisor 함수를 완성해 보세요. 예를 들어 12가 입력된다면 12의 약수는 [1, 2, 3, 4, 6, 12]가 되고, 총 합은 28이 되므로 28을 반환해 주면 됩니다.

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

curookie 님의 풀이
```c++
#include<iostream>
#include<cmath>
using namespace std;

int sumDivisor(int n)
{
  int sum = 0;
  for(int i=1; i<=sqrt(n); i++) if(n%i==0) { sum += i; if(n!=i*i) sum += n/i; }
    return sum;
}

int main()
{
    int testCase = 12;
    int testAnswer = sumDivisor(testCase);

    cout<<testAnswer;
}
```

