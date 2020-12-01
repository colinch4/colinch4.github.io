---
layout: post
title: "[kotlin] SAM & typealias"
description: " "
date: 2020-11-29
tags: [kotlin]
comments: true
share: true
---


### SAM 전환

SAM(Single Abstract Method)는 자바 API를 코틀린에서 활용할 때 람다 표현식을 이용해 쉽게 이용할 수 있게 제공해주는 기법이다. 안드로이드 프로그래밍이나 서버 측 웹 애플리케이션을 코틀린으로 작성할 때 코틀린 코드에서 자바 API를 자주 활용해야 하는데, 이 때 SAM은 유용하게 활용되는 기법이다.

SAM은 단어 뜻 그대로 하나의 추상 함수를 가지는 인터페이스 활용을 목적으로 한다. 인터페이스와 그 인터페이스를 등록하는 setter 함수가 자바에 작성되어 있다면, 코틀린에서 setter 함수를 이용하여 인터페이스를 구현한 객체를 등록할 때 람다 함수를 이용하여 쉽게 등록하는 방법을 제공한다.
```kotlin
    public interface JavaInterface1 {
    	void callback();
    }
    
    public class SAMTest{
    	JavaInterface1 callback;
    	public void setInterface(JavaInterface1 callback){
    		this.callback = callback;
    	}
    }
    
    // 이용하는 부분
    SAMTest obj = SAMTest();
    obj.setInterface(new JavaInterface1() {
    	@Override
    	public void callback() {
    		System.out.println("hello java");
    	}
    });
    
    // 아래의 함수는 사실 람다로 줄일 수 있다.
    obj.setInterface((JavaInterface1) () -> System.out.println("hello java"))
```
코틀린에서 위의 자바 인터페이스를 사용하면 SAM을 이용하여 다음과 같이 사용할 수 있다.
```kotlin
    fun main(args: Array<String>){
    	val obj = SAMTest()
    
    	obj.setInterface(object: JavaInterface1{
    		override fun callback() {
    			println("hello kotlin")
    		}
    	})
    	obj.callback.callback()
    }
    
    // SAM 적용
    
    fun main(args: Array<String>){
    	val obj = SAMTest()
    
    	obj.setInterface { println("hello sam") }
    }
```
코드가 굉장히 간결해진다. 인터페이스의 추상 함수 내부 코드 구현만 람다 식으로 표현해 주면 된다. 마치 고차함수를 인수로 받는 함수를 사용하는 것 같은 모양새가 된다.

### typealias

타입 에일리어스란 타입의 이름을 변경하는 방법을 이야기한다. 여기서 타입은 클래스명 혹은 인터페이스명을 가리킨다. 프로퍼티의 타입으로 지정할 수 있는 것에 대한 이름 변경을 제공한다는 의미이다.
```kotlin
    typealias MyInt = Int
    typealias MList<T> = MutableList<T>
    typealias MC = MyClass
    typealias MI = MyInterface
    typealias MyType = (Int) -> Boolean
    val myFun: MyType = { it > 10 }
    
    class MyClass: MY
    
    // inner class에 대한 타입을 재정의하는 데도 사용가능
    class Super {
    	inner class Sub
    
    	fund getSubInstance(): MySub {
    		return Sub()
    	}
    }
    
    typealias MySub = Super.Sub
```