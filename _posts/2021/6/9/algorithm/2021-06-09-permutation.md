---
layout: post
title: "[알고리즘] Permutation(순열)"
description: " "
date: 2021-06-09
tags: [알고리즘]
comments: true
share: true
---

# Permutation(순열)

>순열이란 n 개의 값 중에서 r 개의 숫자를 모든 순서대로 뽑는 경우를 말함
>
>ex) [1,2,3]일 때 크기가 3인 배열에서 2개를 뽑았을 때 [1, 2] [1, 3] [2, 1] [2, 3] [3, 1] [3, 2] 6가지의 경우가 나온다.



### Swap을 이용한 순열

*  swap 함수를 만들어서 배열들의 값을 직접 바꾸는 방법
* 배열의 첫 값부터 순서대로 하나씩 바꾸며 모든 값을 한번씩 swap
* depth를 기중 인덱스로 하여 depth보다 작은 값들을 그대로 고정하고 depth 보다 인덱스가 큰 값들만 가지고 다시 swap을 진행함

![](./image/permutation1.PNG)



```java
// 순서 없이 n 개중에서 r 개를 뽑는 경우
// 사용 예시: permutation(arr, 0, n, 4);
static void permutation(int[] arr, int depth, int n, int r) {
    if(depth == r) {
        print(arr, r);
        return;
    }
 
    for(int i=depth; i<n; i++) {
        swap(arr, depth, i);
        permutation(arr, depth + 1, n, r);
        swap(arr, depth, i);
    }
}
 
static void swap(int[] arr, int depth, int i) {
    int temp = arr[depth];
    arr[depth] = arr[i];
    arr[i] = temp;
}

 // 배열 출력
    static void print(int[] arr, int r) {
        for(int i=0; i<r; i++)
            System.out.print(arr[i] + " ");
        System.out.println();
    }

//결과
1 2 3
1 3 2
2 1 3
2 3 1
3 2 1
3 1 2
```



### visited 배열을 이용한 순열

* arr = r 개를 뽑기 위한 n 개의 값

  output = 뽑힌 r 개의 값

  visited =중복해서 뽑지 않기 위해 체크하는 값

* DFS를 돌면서 모든 인덱스를 방문하여 output에 값을 넣음

* 이미 들어간 값은 visited 값을 true로 바꾸어 중복하여 넣지 않음

* depth 값은 output 에 들어간 숫자의 길이라고 생각하면 됨

* depth 의 값이 r 만큼 되면 output 에 들어 있는 값을 출력하면 됨



![](./image/permutation2.PNG)



```java
// 순서를 지키면서 n 개중에서 r 개를 뽑는 경우
// 사용 예시: perm(arr, output, visited, 0, n, 3);
static void perm(int[] arr, int[] output, boolean[] visited, int depth, int n, int r) {
    if(depth == r) {
        print(output, r);
        return;
    }
 
    for(int i=0; i<n; i++) {
        	/*************************************** 

			여기서 visited 배열을 사용하지 않으면 중복 순열이 가능하다
					
			 *******************************************/
        if(visited[i] != true) {
            visited[i] = true;
            output[depth] = arr[i];
            perm(arr, output, visited, depth + 1, n, r);       
            output[depth] = 0; // 이 줄은 없어도 됨
            visited[i] = false;;
        }
    }
}

//결과
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
```





### 문제

[백준 10974](https://www.acmicpc.net/problem/10974)



### 정리된 코드

[Permutation_Last](https://github.com/kyun9/PracticeAlgorithm/blob/master/src/Alone/Permutation_Last.java)