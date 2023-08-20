---
layout: post
title: "[Go] Functions"
description: " "
date: 2021-11-19
tags: [Go]
comments: true
share: true
---

## Functions

### Function의 특징

  * 자유로운 함수 선언의 위치 
    * Go는 함수 선언의 위치 제약이 없다.  
      * C/C++과 같은 언어는 함수 선언의 위치가 중요하다. C/C++의 언어에서는 main() 함수에서 특정 함수를 호출하기 위해서는 호출하려는 함수가 main()함수 이전에 선언 되어야 한다.
  * Mutiple Return Value
    * 여러개의 반환값을 리턴할 수 있다.
      * 다른 언어에서는 여러개의 반환값을 리턴하기 위해서는 referencem pointer type, class 혹은 struct의 인스턴스를 활용해야 한다.
      * 문법적으로 여러 return value를 리턴이 가능하기에 코드가 타언어에 비해 간결하다.



### Syntax
  * Function Declaration   
  <code>func \<functionName> () {...}</code>  
  ```go
  func hello() {
    fmt.Println("Baby Tiger is Here!")
  }

  func main() {
    hello()
  }
  ```
  함수가 정의된 시작 줄에서 여는 중괄호(<code>{</code>)를 써주어야 한다.  
  줄바꿈을 하여 <code>{</code> 를 써주게 되면 컴파일 에러가 발생한다.  

  * Parameters  
  <code>func \<funcName>(\<param1> \<Type>, \<param2> \<Type>) (returnValue's_Type)</code>  
  ```go
  func main{
    r := sum(1000, 90)
    fmt.Println(r) // 1090
  }

  func sum(a int, b int) int {
    return a + b
  }
  ```
  변수를 선언할 때 처럼 *매개변수*의 자료형과 *리턴값*의 자료형 또한 뒤에 붙여준다.  

  * Multiple return values  
  ```bash
  func <funcName>(<param1> <Type>, <param2> <Type>) (<returnVal1's_Type>, <returnVal2's_Type>){
        return <returnVal1>, <returnVal2>
  }
  ```  
  ```go
  func sumAndDiff(v1 int, v2 int) (int, int) { 
        return v1 + v2, v1 - v2
  } // (int, int)는 두 개의 integer 값이 리턴되는 것을 의미

  func main(){
        sum, diff := sumAndDiff(8, 4)
        fmt.Println(sum, diff) // 12 4
  }  
  ```  
   반환 값이 여러 개일 경우 <code>,</code> 로 구분해준다.  
   <code>()</code> 괄호 안에 리턴값 자료형을 <code>,</code> 로 구분하여 지정해준다.    
   리턴값은 함수에서 지정한 순서대로 리턴된다.  
   만약 리턴값이 여러개인데도 불구하고 리턴값을 받을 변수 하나만 적으면 첫 번째 리턴값만 저장된다.  
   Blank identifier을 통해 원하는 값만 리턴 가능하다.  
    
   ```go
   func sumAndDiff(v1 int, v2 int) (int, int) { 
         return v1 + v2, v1 - v2
   } 
   func main() {
         _, diff := sumAndDiff(8, 8) // sum은 제외하고 diff 값만 받고 싶을 때
         fmt.Println(diff) // 4
   }
   ``` 
   <code>_</code> 를 통해 특정 값을 생략
