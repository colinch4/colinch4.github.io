---
layout: post
title: "[programmers][알고리즘][level2] 행렬의 곱셈"
description: "행렬의 곱셈은, 곱하려는 두 행렬의 어떤 행과 열을 기준으로, 좌측의 행렬은 해당되는 행, 우측의 행렬은 해당되는 열을 순서대로 곱한 값을 더한 값이 들어갑니다. 행렬을 곱하기 위해선 좌측 행렬의 열의 개수와 우측 행렬의 행의 개수가 같아야 합니다. 곱할 수 있는 두 행렬 A,B가 주어질 때, 행렬을 곱한 값을 출력하는 productMatrix 함수를 완성해 보세요."
date: 2018-05-16
tags: [programmers, 알고리즘]
comments: true
share: true
---

행렬의 곱셈은, 곱하려는 두 행렬의 어떤 행과 열을 기준으로, 좌측의 행렬은 해당되는 행, 우측의 행렬은 해당되는 열을 순서대로 곱한 값을 더한 값이 들어갑니다. 행렬을 곱하기 위해선 좌측 행렬의 열의 개수와 우측 행렬의 행의 개수가 같아야 합니다. 곱할 수 있는 두 행렬 A,B가 주어질 때, 행렬을 곱한 값을 출력하는 productMatrix 함수를 완성해 보세요.

```c++
#include<iostream>
#include<string>
using namespace std;

string getName(int day)
{
    switch(day)
    {
        case 3: return "SUN"; 
        case 4: return "MON";
        case 5: return "TUE"; 
        case 6: return "WED";
        case 0: return "THU";
        case 1: return "FRI";
        case 2: return "SAT";
    }
    return "";
}

string getDayName(int a,int b)
{
    if ( (a>12) || (b>31) ) return ""; 

    string answer= "";
    int day = 0; 
    int month[12] = {31,29,31,30,31,30,31,31,30,31,30,31};
    for ( int i = 0; i < a-1; ++i ) day += month[i];
    day += b; 

    answer = getName(day%7); 

    return answer;
}
int main()
{
    int a=5,b=24;

    //아래는 테스트 출력을 위한 코드입니다.
    cout<<getDayName(a,b);
}
```

나웅태 님의 풀이
```c++
#include<iostream>
#include<string>
using namespace std;

string getDayName(int a,int b)
{
  int month[12] = {0,31,29,31,30,31,30,31,31,30,31,30};
  string date[7] = {"SUN","MON","TUE","WED","THU","FRI","SAT"};

  for(int i = 0; i < a; i++)
  {
    b += month[i];
  }  

    string answer= date[(b+4)%7];  

    return answer;
}
int main()
{
    int a=5,b=24;

    //아래는 테스트 출력을 위한 코드입니다. 
  cout<<getDayName(a,b);
}

```
