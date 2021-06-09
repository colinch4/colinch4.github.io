---
layout: post
title: "[알고리즘] 이진 탐색(Binary Search)"
description: " "
date: 2021-06-09
tags: [알고리즘]
comments: true
share: true
---

# 이진 탐색(Binary Search)

> 정렬된 리스트에서 특정한 값을 찾는 알고리즘



* 처음 중간의 값을 임의의 값으로 선택하여, 그 값을 찾고자 하는 값과 크고 작음을 비교하는 방식으로 채택하고 있음
* 처음  선택한 중앙값이 만약 찾는 값보다 크면 그 값은 새로운 최고값이 되며, 작으면 그 값은 새로운 최하값이 됨
* 검색이 반복될 때마다 목표값을 찾을 확률은 두배가 됨
* 이진 검색은 분할 정복 알고리즘(divide and conquer) 의 한 예임



```java
//이분 탐색 메서드
	private static int binarySearch(int[] A, int n) {
		int first = 0;
		int last = A.length - 1;
		int mid = 0;

		while (first <= last) {
			mid = (first + last) / 2;

			if (n == A[mid])
				return 1;
			else {
				if (n < A[mid])
					last = mid - 1;
				else
					first = mid + 1;
			}
		}
		return 0;
	}
```





### 문제

[백준 1920](https://www.acmicpc.net/problem/1920)



### 정리된 코드

[B_1920](https://github.com/kyun9/PracticeAlgorithm/blob/master/src/B_Study/B_1920.java)