---
layout: post
title: "[알고리즘] Combination(조합)"
description: " "
date: 2021-06-09
tags: [알고리즘]
comments: true
share: true
---

## Combination(조합)

> 조합이란 n 개의 숫자 중에서 r 개의 수를 순서 없이 뽑는 경우를 말함
>
> ex) [1,2,3]일 때 크기가 3인 배열에서 2개를 뽑았을 때 [1, 2] [1, 3] [2, 3] 3가지의 경우가 나온다.
>
> [2, 1] [3, 1] [3, 2]는 중복이라서 제거됨



## visited 이용한 조합

### 1. 백트래킹 이용하여 구현

* start 변수 기준
* start 인덱스를 기준으로 start 보다 작으면 뽑을 후보에서 제외, start보다 크면 뽑을 후보가 됨
* visited[i]는 true가 되면 뽑음, 안 뽑으면 false
* 다음 for 문에서는 무조건 i + 1로 시작



```java
// 백트래킹 사용
// 사용 예시 : combination(arr, visited, 0, n, r)
static void combination(int[] arr, boolean[] visited, int start, int n, int r) {
    if(r == 0) {
        print(arr, visited, n);
        return;
    } else {
        for(int i=start; i<n; i++) {
            visited[i] = true;
            combination(arr, visited, i + 1, n, r - 1);
            visited[i] = false;
        }
    }
}

 static void print(int[] arr, boolean[] visited, int n) {
        for(int i=0; i<n; i++) {
            if(visited[i] == true)
                System.out.print(arr[i] + " ");
        }
        System.out.println();
    }

//결과
1 2 3
1 2 4
1 3 4
2 3 4
```



### 2. 재귀 이용하여 구현

* depth 변수를 사용함
* depth 변수는 현재 인덱스라고 생각하면 됨
* 현재 인덱스를 뽑는다면 visited[depth] = true, 뽑지 않는다면 visited[depth] = false
* depth == n 되면 모든 인덱스를 다 보았으므로 재귀 종료



```java
// 재귀 사용
// 사용 예시 : comb(arr, visited, 0, n, r)
static void comb(int[] arr, boolean[] visited, int depth, int n, int r) {
    if(r == 0) {
        print(arr, visited, n);
        return;
    }
    if(depth == n) {
        return;
    } else {
        visited[depth] = true;
        comb(arr, visited, depth + 1, n, r - 1);
 
        visited[depth] = false;
        comb(arr, visited, depth + 1, n, r);
    }
}

//결과
1 2 3
1 2 4
1 3 4
2 3 4
```



## 리스트에 담은 조합

### 중복 없는 조합

* visited 배열을 이용해 true가 아닌 리스트에 추가 / 제거를 이용한 조합
* index 변수를 이용하여 arr배열의 위치에 값을 리스트에 추가(index 증가)

```java
// 리스트에 담은 조합 함수
	public static void combination(ArrayList<Integer> arrList, int n, int r, int index) {
		if (r == 0) {
			for (int i = 0; i < arrList.size(); i++) {
				System.out.print(arrList.get(i) + " ");
			}
			System.out.println();
			return;
		}
		if (index == n)
			return;
		arrList.add(arr[index]);
		combination(arrList, n, r - 1, index + 1); // 뽑았음-> r-1
		arrList.remove(arrList.size() - 1); // 위에서 뽑은거 롤백
		combination(arrList, n, r, index + 1); // 안뽑았으니 r
	}

//결과
1 2 3 
1 2 4 
1 3 4 
2 3 4 
```



### 중복 있는 조합

* index 변수를 이용하여 arr배열의 위치에 값을 리스트에 추가(처음 index 증가하지 않음)

```java
public static void combination_repetition(ArrayList<Integer> arrList, int n, int r, int index) {
		if (r == 0) {
			for (int i = 0; i < arrList.size(); i++) {
				System.out.print(arrList.get(i) + " ");
			}
			System.out.println();
			return;
		}

		if (index == n)
			return;
		arrList.add(arr[index]);
		combination_repetition(arrList, n, r - 1, index); // 뽑았음-> r-1 중복을 허용하니까 index는 고정
		arrList.remove(arrList.size() - 1); // 위에서 뽑은거 롤백
		combination_repetition(arrList, n, r, index + 1); // 안뽑았으니 r, index+1
	}

//결과
1 1 1 
1 1 2 
1 1 3 
1 1 4 
1 2 2 
1 2 3 
1 2 4 
1 3 3 
1 3 4 
1 4 4 
2 2 2 
2 2 3 
2 2 4 
2 3 3 
2 3 4 
2 4 4 
3 3 3 
3 3 4 
3 4 4 
4 4 4 
```







### 문제

[백준 2309](https://www.acmicpc.net/problem/2309)



### 정리된 코드

[Combination Last](https://github.com/kyun9/PracticeAlgorithm/blob/master/src/Alone/Combination_Last.java)

