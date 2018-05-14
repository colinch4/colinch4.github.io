---
layout: post
title: "programmers-level1-최대공약수와 최소공배수"
description: "최대공약수와 최소공배수"
date: 2018-05-14
tags: [programmers, 알고리즘]
comments: true
share: true
---

두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환해주는 gcdlcm 함수를 완성해 보세요. 배열의 맨 앞에 최대공약수, 그 다음 최소공배수를 넣어 반환하면 됩니다. 예를 들어 gcdlcm(3,12) 가 입력되면, [3, 12]를 반환해주면 됩니다.

```c++
#include<vector>
#include<iostream>
using namespace std;
vector<int> gcdlcm(int a,int b)
{
	vector<int> answer;
    int big = 0; 
    int small = 0; 
    if ( a > b )
    {
        big = a; 
        small = b;
    }
    else
    {
        big = b; 
        small = a; 
    }
    
    for ( int i = small; i > 0; --i )
    {
        if ( ((big % i) == 0) && ((small % i) == 0) )
        {
            answer.push_back(i);
            break;
        }
             
    }
    
    for ( int i = 1; i <= small; ++i )
    {
        int bigi = big*i; 
        if ( (bigi % small) == 0 ) 
        {
            answer.push_back(bigi); 
            break;
        }
    }
    
	return answer;
}

int main()
{
	int a=3, b=12;
	vector<int> testAnswer = gcdlcm(a,b);

	cout<<testAnswer[0]<<" "<<testAnswer[1];
}
```

김준민 님의 풀이 
```c++
#include<vector>
#include<iostream>
using namespace std;


int Euclidean(int a, int b)
{
    return b ? Euclidean(b, a%b) : a;
}

vector<int> gcdlcm(int a,int b)
{
    vector<int> answer;
    // 유클리드 호제법
  answer.push_back(Euclidean(a,b));

  answer.push_back(a*b / answer[0]);

    return answer;
}

int main()
{
    int a=3, b=12;
    vector<int> testAnswer = gcdlcm(a,b);

    cout<<testAnswer[0]<<" "<<testAnswer[1];
}
```

