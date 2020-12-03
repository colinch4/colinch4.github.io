---
layout: post
title: "[안드로이드] Fragment Manager 란"
description: " "
date: 2020-11-25
tags: [Android]
comments: true
share: true
---


# 프래그먼트 매니저  

액티비티와 프래그먼트의 중간에서 서로를 이어주는 역할을 하는 것이 프래그먼트 매니저  
  
  
## 프래그먼트 매니저가 하는 일  
  
#### 1. 프래그먼트 트랜잭션  

프래그먼트를 추가, 삭체, 교체 등의 작업을 수행할 수 있게 해주며, 행해진 트랜잭션의 상태를 
프래그먼트 백스택에 저장할 수 있도록 줌.  

#### 2. 액티비티와의 통신  

단일 프래그먼트에 대해 세부적인 작업 또한 가능하다. 프래그먼트 내의 구성요소들 하나하나에 접근 할 수 있도록 해줌.  

액티비티에서 특정 이벤트가 발생했을 때, 프래그먼트에서 적절한 동작을 할 수 있도록 합니다.  

## 프래그먼트 트랜잭션  

프래그먼트 추가, 삭제 및 교체 뿐만아니라 프래그먼트 백스택 관리, 프래그먼트 전환 애니매이션 설정 등 많은 일을 수행함.  

### 1. 프래그먼트 트랜잭션 설정  

```
// 프래그먼트 매니저 선언 
FragmentManager fragmentManaget = getSupportFragmentManager();

// 프래그먼트 트랜잭션 시작
FragmentTransaction fragmentTransaction = fragmentManager.beginTransaction();

// 트랜잭션, 백스택, 애니매이션 등을 설정

// 프래그먼트 트랜잭션 마무리
fragmentTransaction.commit();

```

### 2. 트랜잭션을 이용한 프래그먼트 삽입, 교체, 제거  

```
// 프래그먼트 추가
fragmentTransaction.add(R.id.fragment_container, new 프래그먼트이름);

// 프래그먼트 교체
fragmentTransaction.replace(R.id.fragment_container, new 프래그먼트이름);

// 프래그먼트 제거
fragmentTransaction.remove(프래그먼트);

```
  

### 3. 프래그먼트 백스택  

백스택을 이용하면 프래그먼트를 back key를 이용하여 이전 상태로 돌아갈 수 있다.

addToBackStack() 메소드만 호출하면 된다.

```
//백스택에 저장
fragmentTransaction.addToBackStack(null);

//트랜잭션 마무리
fragmentTransaction.commit();
```

## 액티비티와의 통신  

### 액티비티에서 프래그먼트 자원에 접근  

프래그먼트 매니저에 속한 findFragmentById() 또는 findFragmentByTag()로 원하는 프래그먼트를 참조할 수 있다.  

이때 id로 찾는 경우는 레이아웃이 있는 경우, tag로 찾는 경우는 레이아웃이 없는 경우에 사용한다.  
  
  
### 프래그먼트에서 액티비티 자원에 접근  
  

interface를 사용하여 액티비티에 데이터를 보낼 수 있다.    

액티비티는 리스너 interface를 구현하여 콜백 메소드를 오버라이딩하고, 프래그먼트는 생성될 때 onAttach에서 액티비티로부터 context를 받아 리스너로 사용할 수 있다.  

이때 프래그먼트가 액티비티에서 제거되는 onDetach에서 listener 변수를 null로 해주도록 하자.  



  






