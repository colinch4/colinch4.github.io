---
layout: post
title: "[자바기초] HashSet, TreeSet"
description: " "
date: 2020-11-26
tags: [java]
comments: true
share: true
---

# HashSet  

데이터의 순서와 중복이 없는 Set . 내부적으로 해싱을 이용하여 구현됨.

데이터 저장 전에 기존에 같은 객체가 있는지 확인한다.  있다면 저장하지 않음  

저장할 객체의 equals와 hashCode를 호출하여 같은 객체가 있는지 확인한다.  고로 오버라이딩 해놔야한다. 


# LinkedHashSet  

데이터의 순서가 있는 Set. 

  
# TreeSet  
  
범위 검색과 정렬에 유리한 이진 트리로 구현됨 (레드-블랙 트리)

부모보다 작은 값을 왼쪽, 큰 값은 오른 쪽에 저장한다.  

HashSet보다 데이터 추가, 삭제에 시간이 더 걸린다.  

데이터의 저장 과정은 이진 트리에서 데이터를 추가하는 과정과 동일.  

headSet : 지정된 객체보다 작은 값의 객체들을 반환  
  
subSet: 범위 검색의 결과를 반환합니다.  
  
tailSet: 지정된 객체보다 큰 값의 객체들을 반환합니다.  

TreeSet은 문자열 검색, 자동완성 등과 같은 곳에 활용할 수 있다.  

+ 중위 순회시에 오름차순으로 정렬할 수 있다.

# HashSet vs TreeSet  

구현 방식은 각각  해싱과 이진트리이다.  

해싱이 이진트리보다 빨라 HashSet이 속도면에서 더 빠르다. 

그러나 TreeSet은 이진트리의 사용으로 정렬기능이 있다. 
 