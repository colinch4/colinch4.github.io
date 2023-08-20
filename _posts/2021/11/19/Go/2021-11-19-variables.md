---
layout: post
title: "[Go] Variables"
description: " "
date: 2021-11-19
tags: [Go]
comments: true
share: true
---

## Variables
Go에서 변수를 선언할때는 <code>var</code> 를 사용한다.  
변수를 초기화할때는 <code>=</code> 혹은 <code>:=</code> 를 사용할 수 있다.

* <code>var</code> 키워드는 종종 global 변수를 선언시 사용된다.
* <code>:=</code> 연산자는 에러처리를 위해 많이 사용된다.
* 전역 변수는 <code>:=</code> 연산자를 통해 선언할 수 없다.

## Declaration
변수 선언시 <code>var</code> 를 사용하여 선언  
**Syntax :**  
  * 단일 변수 선언    
  <code>var \<variableName> \<dataType></code>
  ```go
  var age int
  var price float32
  ```
  * 복수 변수 선언 (같은 자료형)  
  <code>var \<variable1>, \<variable2> \<dataType></code>
  ```go
  var width, height int
  ```
  * 복수 변수 선언 (서로 다른 자료형)  
   소괄호<code>()</code>를 사용
   ```
   var ( 
      <variable1> <dataType>   
      <variable2> <dataType>
   )
   ```
   
  ```go
  var (
      age int
      name string
      height float32
  )
  ```

변수 선언시 초기값을 할당하지 않으면 **Zero Value** 가 할당된다.  
> Go가 Zero Value로 초기화 시키는 이유는 값이 garbage 값으로 할당되어 예상치 못한 결과가 발생하지 않도록 하기 위해서이다. 

| Data Types  | Zero Values |
| :---------: | :---------: |
| Integer     | 0           |
| Floating Point| 0.0       |
| Boolean     | false       |
| String      | ""          |
| Interface   | nil         |
| Slices      | nil         |
| Channels    | nil         |
| Maps        | nil         |
| Pointers    | nil         |
| Functions   | nil         |

## Assignment
1. **The Normal Assignment**  
  **Operator :** <code>=</code>  
  **Syntax :** 
  * 선언과 할당 동시에 하기  
  <code>var \<variableName> \<dataType> = \<value></code>  
  선언과 할당을 동시에 할 때 자료형(data type)은 생략 가능  
  Go는 할당되는 값을 보고 자료형을 대신 정해준다.  
  <code>var \<variableName> = \<value></code>  
  ```go
  var age int = 22
  var price float32 = 590.30
  var width = 10.10
  ```
  * 할당하기  
  <code>\<variableName> = \<value></code>
  ```go
  age = 22 
  ```
  * 복수 변수들의 선언과 할당    
  <code>var \<variable1>, \<variable2>, \<variable3> \<dataType> = \<value1>, \<value2>, \<value3>
</code>  

  ```go
  var SF, NY, LA = 415, 212, 213
  ```  
2. **The Short Assignment**  
  변수의 짧은 선언은 자료형과 <code>var</code> 키워드를 생략할 수 있다.   
  함수 안에서만 사용 가능하다.  
  > 즉, 함수 밖에서는 반드시 <code>var</code> 키워드를 통해 변수를 선언해야 한다.  

  **Operator :** <code>:=</code>  
  **Syntax :** 
  * 단일 변수 선언 및 할당  
  <code>\<variableName> := \<value></code>
  * 복수 변수 선언 및 할당  
  <code>\<variable1>, \<variable2> := \<value1>, \<value2></code>
  ```go
  tom := "Brown"
  tom, tim := "Brown", "Black"
  ```
