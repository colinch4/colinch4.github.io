---
layout: post
title: "[자바기초] ArrayList와 LinkedList"
description: " "
date: 2020-11-26
tags: [java]
comments: true
share: true
---


# ArrayList  

arraylist는 기존의 vector를 개선한 것으로, 구현원리와 기능이 동일하다.  

단, vector는 thread safe하지만 arraylist는 그렇지 않음.  

둘다 List 인터페이스를 구현하므로 저장순서가 유지되고 중복을 허용한다.  

배열기반이다.  
  

## 삭제하는 과정  

01234 가 저장되어 있다고 하자. 맨 앞 0이 삭제된다면  

1. 1234가 앞으로 한 칸씩 복사되어 삭제할 데이터 0을 덮어쓴다.   

01234 -> 12344  

2. 데이터가 모두 한칸씩 이동했으므로, 마지막 칸은 null로 채워준다.  

12344 -> 1234  

3. 데이터가 삭제되어 size가 줄었으므로, size 값을 감소시킨다.   

맨 마지막 데이터가 삭제된다면 데이터의 복제는 일어나지 않는다.  

## ArrayList 장점과 단점  

### 장점  
  
구조가 간단하고, 데이터를 읽는 데 걸리는 access time이 짧다.  

### 단점  

1. 크기를 변경할 수 없다. 크기를 변경해야하는 경우 새로운 배열을 생성 후 복사해야한다. 

2. 데이터의 중간에서 삽입 및 삭제에 시간이 걸림.

# LinkedList  

배열과 달리 링크드리스트는 불연속적으로 존재하는 데이터를 연결한다.  

단일 링크드리스트, 더블 링크드리스트, 더블리 써큘러 링크드 리스트가 있음  


# ArrayList vs LinkedList  

순차적으로 데이터를 추가/삭제 -> ArrayList  

비순차적으로 데이터를 추가/삭제 -> LinkedList 

접근 시간 -> ArrayList