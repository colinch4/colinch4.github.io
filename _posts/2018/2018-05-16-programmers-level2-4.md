---
layout: post
title: "2016년"
description: "2016년 1월 1일은 금요일입니다. 2016년 A월 B일은 무슨 요일일까요? 두 수 A,B를 입력받아 A월 B일이 무슨 요일인지 출력하는 getDayName 함수를 완성하세요. 요일의 이름은 일요일부터 토요일까지 각각 SUN,MON,TUE,WED,THU,FRI,SAT 를 출력해주면 됩니다. 예를 들어 A=5, B=24가 입력된다면 5월 24일은 화요일이므로 TUE를 반환하면 됩니다."
date: 2018-05-16
tags: [programmers]
comments: true
share: true
---

2016년 1월 1일은 금요일입니다. 2016년 A월 B일은 무슨 요일일까요? 두 수 A,B를 입력받아 A월 B일이 무슨 요일인지 출력하는 getDayName 함수를 완성하세요. 요일의 이름은 일요일부터 토요일까지 각각

> SUN,MON,TUE,WED,THU,FRI,SAT

를 출력해주면 됩니다. 예를 들어 A=5, B=24가 입력된다면 5월 24일은 화요일이므로 TUE를 반환하면 됩니다.

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
