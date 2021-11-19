---
layout: post
title: "[Go] Constants"
description: " "
date: 2021-11-19
tags: [Go]
comments: true
share: true
---

# Constants
Go 에서 상수를 선언할 때는 <code>const</code> 키워드를 사용한다.  
상수 명명 규칙은 변수와 동일하다. 다른점이라면 상수는 선언과 초기화를 함께 해야 한다는 것이다.  

## Declaration & Initialization
상수 선언과 동시에 반드시 함께 해주어야 하는 값의 초기화.  
**Syntax**
  * 단일 상수 선언 및 초기화  
  <code>const \<constantName> = \<value></code>  
  자료형은 생략 가능하다.  
  <code>const \<constantName> \<dataType> = \<value></code> 
   
  ```go
  const jordan = "Amman"
  const peru string = "Lima"
  ```
  
  * 복수 상수 선언 및 초기화 (같은 자료형)  
  Comma(,) 로 구분  
  
  <code>const \<constant1>, \<costant2> = \<value1>, \<value2></code>  
  <code>const \<constant1>, \<costant2> \<dataType> = \<value1>, \<value2></code>  </code>
   
  ```go
  const barium, lanthanum = 56, 57
  const thorium, protactinium int = 90, 91
  ```
  * 복수 상수 선언 및 초기화 (다른 자료형)  
  ```go
  const (
      <constant1> = <value1>
      <constant2> = <value2>
      <constnat3> = <value3>
  )
  ```

## Enumeration
Go 에서 상수의 연속되는 값을 위해 <code>iota</code> 를 사용할 수 있다.
  * 그리스 알파벳에서 iota는 10 을 뜻한다. 
  * 수학에서 iota는 허수 단위 i 를 뜻한다.
  * iota는 0부터 시작한다.
  * iota는 상수의 연속된 값을 위해서만 쓰인다. 

많은 경우 상수는 연속되는 값을 가진다. 

대표적으로 요일의 표현이 있다.
  ```go
  // w/o iota
  const Sunday    = 0
  const Monday    = 1
  const Tuesday   = 2
  const Wednesday = 3
  const Thursday  = 4
  const Friday    = 5
  const Saturday  = 6
  
  // with iota
  const (
     Sunday = iota // 0
     Monday        // 1
     Tuesday       // 2
     Wednesday     // 3
     Thursday      // 4
     Friday        // 5
     Saturday      // 6
  )
  ```
Truthy value 와 Falsy value의 표현
  ```go
  const (
      zero, off, wrong = iota, iota, iota // 상수의 개수만큼 iota를 써주어야 한다.
      one, on, right
  )
  // output
   0 0 0 
   1 1 1
  ``` 
1 부터 시작하기 위해서는 아래와 같은 방법을 사용한다.
  ```go
  const (
     usa = iota + 1 // 1
     africa         // 2
     europe         // 3
  )
  ```
값 skip 하기
  * 원치 않는 값을 skip 하기 위해 unserscore <code>_</code> 를 사용할 수 있다.
  ```go
  const (
        Math = iota // 0
        English     // 1
        _
        _
        Physics     // 4
  )
  ```
