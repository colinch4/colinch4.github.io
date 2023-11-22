---
layout: post
title: "[알고리즘] Disjoint-Set(서로수 집합) 알고리즘"
description: " "
date: 2021-06-09
tags: [java]
comments: true
share: true
---

## Disjoint-Set(서로수 집합) 알고리즘

> - Union-Find 알고리즘 이라고도 불린다.
>
> * 여러개의 노드가 존재할 때, 두개의 노드를 선택해서 이 노드들이 서로 같은 그래프에 속하는 판별하는 알고리즘
>
> * 재귀 방법으르 통해 부모노드를 갱신



* 노드가 어느 그룹에 속해있는지 확인하는 것 : Find-Set

  <img src="./image/disjoint1.PNG" style="zoom:50%;" />

* 다른 그룹이었던 노드들을 하나의 그룹으로 합치는 것 : Union

  <img src="./image/disjoint2.PNG" style="zoom:50%;" />



### 부모 노드 초기화

```java
int n = 10;
int[] parents = new int[n + 1];

//부모노드 배열 초기화
for (int i = 1; i <= n; i++) {
	parents[i] = i;
	System.out.print(parents[i] + " ");
}

//< 연결 전 >
1 2 3 4 5 6 7 8 9 10 
```



### Find-set 과정

1. x의 부모 노드를 찾는 함수
2. x 와 parents[x]의 값이 다르면, x의 부모 노드는 x자신이 아닌 다른 노드이므로 재귀함수를 통해 부모노드를 찾아 parent 변수에 담고 리턴함
3. x의 값이 parents[x]와 같으면, x의 부모노드가 자기자신이라는 뜻이므로 리턴함

```java
// 설명 1번
public static int findSet(int[] parents, int x) {
		
		// 설명 3번
		if (parents[x] == x) {
			return x;
		}
		
		// 설명 2번
		int parent = findSet(parents, parents[x]);
		return parent;
}
```



### Union 과정

1. 노드 x와 노드 y를 합집합하는 연산
2. 각각의 노드에 대한 부모 노드를 찾음
3. 어느 한 집합의 부모 노드를 다른 집합의 부모노드로 변경

```java
// 설명 1번
public static void unionParent(int[] parents, int x, int y) {
		// 설명 2번
		x = findSet(parents, x);
		y = findSet(parents, y);
		
		// 설명 3번
		// 더 작은 값으로 부모 노드 설정
		if (x < y) {
			parents[y] = x;
		} else {
			parents[x] = y;
		}
}
```





### 문제

[백준 1717](https://www.acmicpc.net/problem/1717)

### 정리된 코드

[DisjointSet code](https://github.com/kyun9/PracticeAlgorithm/blob/master/src/Alone/Disjoint_Set.java)

