---
layout: post
title: "programmers-level1-행렬의 덧셈"
description: "행렬의 덧셈"
date: 2018-05-14
tags: [programmers]
comments: true
share: true
---
 
행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다. 2개의 행렬을 입력받는 sumMatrix 함수를 완성하여 행렬 덧셈의 결과를 반환해 주세요.

예를 들어 2x2 행렬인 A = ((1, 2), (2, 3)), B = ((3, 4), (5, 6)) 가 주어지면, 같은 2x2 행렬인 ((4, 6), (7, 9))를 반환하면 됩니다.(어떠한 행렬에도 대응하는 함수를 완성해주세요.)

```c++
#include<iostream>
#include<vector>

using namespace std;

vector<vector<int> > sumMatrix(vector<vector<int> >A, vector<vector<int> >B)
{
	vector<vector<int> > answer;
    auto a_it = A.begin(); 
    auto b_it = B.begin(); 
    while( a_it != A.end() ) 
    {
        vector<int> _answer; 
        auto _a_it = (*a_it).begin(); 
        auto _b_it = (*b_it).begin(); 
        while( _a_it != (*a_it).end() ) 
        {
            _answer.push_back((*_a_it) + (*_b_it)); 
            ++_a_it;
            ++_b_it;
        }
        answer.push_back(_answer);
        ++a_it; 
        ++b_it; 
    }
	return answer;
}
int main()
{
	vector<vector<int> > a{{1,2},{2,3}}, b{{3,4},{5,6}};
	vector<vector<int> > answer = sumMatrix(a,b);

	for(int i=0;i<answer.size();i++)
	{
		for(int j=0;j<answer[0].size();j++)
		{
			cout<<answer[i][j]<<" ";
		}
		cout<<"\n";
	}
}
```

김경주 님의 풀이

```c++
#include<iostream>
#include<vector>
using namespace std;

vector<vector<int> > sumMatrix(vector<vector<int> >A, vector<vector<int> >B)
{
    vector<vector<int> > answer = A;

  for(int i=0; i<A.size(); i++){
    for(int j=0; j<A[0].size(); j++){
      answer[i][j] = A[i][j] + B[i][j];
    }
  }

    return answer;
}
int main()
{
    vector<vector<int> > a{{1,2},{2,3}}, b{{3,4},{5,6}};
    vector<vector<int> > answer = sumMatrix(a,b);

    for(int i=0;i<answer.size();i++)
    {
        for(int j=0;j<answer[0].size();j++)
        {
            cout<<answer[i][j]<<" ";
        }
        cout<<"\n";
    }
}
```
