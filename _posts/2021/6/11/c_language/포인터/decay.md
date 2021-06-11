---
layout: post
title: "[포인터] Decay란"
description: " "
date: 2021-06-11
tags: [c]
comments: true
share: true
---

## Decay란?

* Decay: **C에서 배열의 이름은 배열의 첫번째 원소의 시작 주소**로 해석된다. 즉 배열이 포인터로 변환된 것인데 이를 **Decay(퇴화)** 라고 표현한다.

### Decay 예외
  #### 1\) sizeof 연산 : 배열의 이름에 sizeof 연산을 할 때는 decay가 되지 않는다. 따라서 포인터의 크기가 아닌 **배열의 크기를 반환한다.** 
  #### 2\) & 연산 : 배열의 이름에 &연산을 할 때는 decay가 되지 않는다. 따라서 첫번째 원소의 더블 포인터가 아닌 **배열의 주소를 나타낸다.**

<br>

##  Decay 알아야 돼요? 꼭 써야 되나요?
=> C에서 함수로 배열을 보낼때 주로 배열의 이름을 매개값으로 보낸다. 즉 배열이 decay 되어 포인터(첫번째 원소의 시작 주소)로서 보내는 것인데 이런 식으로 매개값을 보내면 함수를 작성할 때 함수의 파라미터에 배열의 길이를 일일히 명시하지 않아도 되서 좋고, 또 배열의 길이에 제한이 없고(단,타입 크기 범위 안에서) 낭비가 없다.( ex : addTen(int (*arr)[3]) -> addTen(int *arr)). **단, 포인터로서 보내면 배열의 길이를 모르기 때문에 배열의 길이를 나타내는 값도 필수적으로 같이 보내야 한다.** 그리고 다른 모든 사람이 배열의 이름을 매개값으로 보내기 때문에 decay를 알아야 한다. 

```c
void addTen(int (*arr)[3]) 
// 에서 
void addTen(int *arr, int len)
// 로
```

<br>

## C 언어에서 타입을 보는 방법

* **이름을 뺀 나머지가 타입이다.**

1\) int i -> int : i 의 타입은 int 형이다.
<br><br>2\) int arr[3] -> int[3] : arr의 타입은 int 형의 3개 짜리 배열이다.
<br><br>3\) int arr2[3][4] -> int[3][4] : arr2의 타입은 int 형의 3개 짜리 배열이다. **하나의 원소가 int[4]인!**


### => Decay의 원리로 위의 arr2를 int 형의 12개짜리 배열이라 하면 안된다. arr2는 세개짜리 배열이고 하나의 원소가 int[4], 즉 길이가 4인 원소라 해야 한다. 왜냐면, arr2, 즉 배열의 이름이 **decay 되면서 가리키는 원소가 한칸짜리가 아닌 int[4]이기 때문이다.** 그러므로 sizeof(arr2)는 48인데 **이를 sizeof(int)\*12 로 해석하지 말고 sizeof(int[4])\*3 로 해석해야 한다.** 



decay.c
```c
#include <stdio.h>

void addTen(int *arr){

  int i;
  for(i =0; i<3; i++){
    arr[i] += 10;
  }

  printf("addTen()에서: sizeof(arr): %ld\n", sizeof(arr));

}


int main(){
  
  int i; 
  int arr[3] = { 1, 2, 3 };

  printf("main()에서: sizeof(arr): %ld\n", sizeof(arr));

  addTen(arr); // 배열의 이름을 매개값으로. 즉 포인터로서 보냄.

  for(i = 0; i < 3; ++i){
    printf("%d\n", arr[i]);
  }  

  return 0;
}

// 실행 결과 
// main()에서: sizeof(arr): 12
// addTen()에서: sizeof(arr): 8
// 11
// 12
// 13
```

=> main에서 sizeof(arr)을 하니 값이 12임을 알수 있지만(배열의 이름이더라도 sizeof()연산은 decay 되지 않는다.), addTen 함수에 arr를 매개값으로 보내고 addTen에서 sizeof(arr)을 하니 값이 8임을 알수 있다. **이는 배열의 이름을 매개값으로 보낼 때 decay 되어 포인터(첫번째 원소의 시작 주소)로서 보내짐을 알 수 있다.** 또 포인터이어도 배열로서 사용할 수 있음을 알 수 있다. 따라서 for문을 통해 배열의 모든 원소에 +10씩 적용되었다. 
<br><br>=> 이 코드에는 문제점이 있다. addTen()는 매개값으로 받는 배열을 인덱스 0부터 2까지만 +10을 할 수 밖에 없다. 매개값으로 배열의 이름을 보내면 포인터(첫번째 원소의 시작주소)로서 보낸 것이므로 배열의 길이를 알수 없다. **따라서 배열의 이름을 매개값으로 보낼 때는 반드시 배열의 길이를 나타내는 값도 매개값으로 보내야 한다.** 

<br>

## 제약: 배열은 배열의 첫번째 원소의 시작 주소로 전달하기 때문에, 함수에서 배열의 크기를 알 수 없다. 


## => 배열을 전달하는 함수를 설계할 때, 배열의 길이를 추가적으로 전달해야 한다. 

<br>수정한 addTen()
```c
void addTen(int *arr, int len){
  int i;
  for(i = 0; i < len; i++){
    arr[i] += 10;  
  }

  printf("addTen()에서: sizeof(arr): %ld\n", sizeof(arr));
}
```
