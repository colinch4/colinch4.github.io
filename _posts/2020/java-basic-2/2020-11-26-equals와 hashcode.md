---
layout: post
title: "[자바기초] equals() 와 hashcode"
description: " "
date: 2020-11-26
tags: [java]
comments: true
share: true
---



# == , equals() 와 hashcode  

## ==  

== 연산자는 피연산자 타입이 기본형인 경우에는 값을 비교하고, 객체인 경우에는 주소가 같은지를 비교한다.  

```
//힙에 생성된 hello리터럴을 둘다 가리킴 
String str1 = "hello";
String str2 = "hello";

str1 == str2  // true

//각각의 메모리에 String 객체를 생성
String str3 = new String("hello");
String str4 = new String("hello");

String str5 = str4;

str3 == str4 // false 
str4 == str5 // true
```  

 
## equals  
  
  
Object 클래스의 메서드로, 클래스들은 equals를 적절히 오버라이딩 하여 사용할 수 있다.  

Object클래스의 equals는 기본적으로 객체 자신과 객체 obj가 같은 객체인지를 true, false로 반환한다. (== 와 같다.)  

그러나 String 클래스에서는 두 문자열의 내용이 같은지를 비교한다.   

hashcode와 같이 오버라이딩하여 개발자가 두 객체가 같지 않더라도 true를 리턴하게 만들 수 있다. (인스턴스의 멤버가 같은지 비교할 수 있다! String 처럼)  

이런 경우, hashcode를 오버라이딩 같이 오버라이딩 하지 않으면, 인스턴스 멤버가 같아도 hashcode의 결과가 다르게 나오게 되어 부작용이 생길 수 있다.

```
// 오버라이딩하여 사용하기

class Person{
	long id;

	public boolean equals(Object obj){ //Person객체의 id가 같은지 비교하는 함수로 오버라이드
		if(obj != null && obj instanceof Person){
			return id == ((Person)obj).id;
		}
		else{
			return false;
		}
	}
}
```
  
## hashCode  
  
  
Object 클래스의 메서드로, 클래스들은 hashCode를 적절히 오버라이딩 하여 사용할 수 있다.  

객체 자신의 해시코드(int)를 반환하는 함수  

다량의 데이터를 저장 & 검색하는 해싱기법에 key를 구분하는데 사용된다.  

equals()를 오버라이딩 했다면 hashCode() 역시 오버라이드 해야한다. equals의 결과가  true인 두 객체의 hashcode는 같아야하기 때문이다.
  
  
## identityHashcode
  
  Object 클래스의 hashcode 처럼 객체의 주소값으로 해시코드를 생성하여 모든 객체에 대해 항상 다른 해시코드 값을 반환한다.
  
  hashcode를 오버라이딩 했더라도, 두 객체가 인스턴스 멤버에 관계없이 서로 다른 객체라는 것을 알 수 있다.



  


