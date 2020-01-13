---
layout: post
title: "[programmers][hash] 완주하지 못한 선수"
description: "수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.
마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요."
date: 2020-01-14
tags: [programmers, 알고리즘, hash]
comments: true
share: true
---

### 문제 설명
수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

### 제한사항
마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
completion의 길이는 participant의 길이보다 1 작습니다.
참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
참가자 중에는 동명이인이 있을 수 있습니다.

### 입출력 예
| participant | completion | return |
| - | - | - |
| [leo, kiki, eden] | [eden, kiki] | leo |
| [marina, josipa, nikola, vinko, filipa] | [josipa, filipa, marina, nikola] | vinko |
| [mislav, stanko, mislav, ana] | [stanko, ana, mislav] |mislav |

|제목|내용|설명|
|:---|---:|:---:|
|왼쪽정렬|오른쪽정렬|중앙정렬|
|왼쪽정렬|오른쪽정렬|중앙정렬|
|왼쪽정렬|오른쪽정렬|중앙정렬|

#### 입출력 예 설명
예제 #1
leo는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.

예제 #2
vinko는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.

예제 #3
mislav는 참여자 명단에는 두 명이 있지만, 완주자 명단에는 한 명밖에 없기 때문에 한명은 완주하지 못했습니다.


#### 내 풀이 
```c++
#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    map<string, int> p_count; 
    
    for ( string _participant : participant ) {
        if ( p_count.find(_participant) == p_count.end() ) {
            p_count[_participant] = 1; 
        } else {
             p_count[_participant] = p_count.find(_participant)->second+1; 
        }        
    }
    
    for ( string _completion : completion ) {
        p_count[_completion] = p_count.find(_completion)->second-1; 
    }
    
    for ( auto it = p_count.begin(); it != p_count.end(); it++ ) {
        if ( it->second != 0 ) answer = it->first; 
    }
    
    return answer;
}
```

#### 윤은지 님의 풀이
```c++
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    sort(participant.begin(), participant.end());
    sort(completion.begin(), completion.end());
    for(int i=0;i<completion.size();i++)
    {
        if(participant[i] != completion[i])
            return participant[i];
    }
    return participant[participant.size() - 1];
    //return answer;
}

```
