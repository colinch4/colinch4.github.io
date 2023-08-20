---
layout: post
title: "[자바기초] HashMap, LinkedHashMap, TreeMap"
description: " "
date: 2020-11-26
tags: [java]
comments: true
share: true
---

## HashMap  

데이터를 키와 값의 페어로 저장  

동기화 지원이 안됨. 동기화를 위해서는 Hashtable을 사용  

해싱 기법으로 데이터를 저장. 데이터가 많아도 검색이 빠르다.


## 사용 법 

```
HashMap map = new HashMap();
map.put("myId","1234");
```


## LinkedHashMap  

순서가 유지되는 HashMap

내부에 더블 링크드리스트로 데이터 입력 순서를 보존할 수 있다.
  

## TreeMap  

TreeSet처럼 이진트리로 구현되어 데이터를 정렬해서 저장함. (Key로 정렬) 

덕분에 저장 시간이 좀 길다. 

TreeSet이 TreeMap으로 구현되어 있다  

다수의 데이터에서 개별적인 검색은 HashMap이 더 빠르다. 

Map이 필요한 경우에는 주로 HashMap을 사용하고, 정렬이나 범위 검색이 필요한 경우에는 TreeMap을 사용한다.