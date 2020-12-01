---
layout: post
title: "[kotlin] by를 이용한 delegate 패턴"
description: " "
date: 2020-11-29
tags: [kotlin]
comments: true
share: true
---


## 델리게이션

델리게이션(Delegation)은 패턴으로 위임자(Delegator)가 실행되면 이곳에서 적절한 업무 처리가 되어야 하는데 이 처리를 위임자에서 직접 처리하지 않고 위임대행자(delegatee)에게 맡긴다는 개념이다. Composition을 이용하는 전형적인 패턴이다.

예를 들어 위임자가 처리해야 하는 업무가 데이터 저장이라고 할 때, 데이터가 하나의 방법으로만 저장되는 것이 아니라 파일, 데이터베이스, 네트워크 등에 저장할 수도 있다고 가정하면 각각의 데이터 저장 로직을 구현한 대행자를 만들고, 그 대행자가 데이터를 저장하도록 처리할 수 있다.
```kotlin
    interface Updater {
        fun update(str: String)
    }
    
    class FileUpdater: Updater {
        override fun update(str: String) {
            println("i am file delegatee : $str")
        }
    }
    
    class DbUpdater: Updater {
        override fun update(str: String) {
            println("i am db delegatee : $str")
        }
    }
    
    class RemoteUpdater: Updater {
        override fun update(str: String) {
            println("i am file delegatee : $str")
        }
    }
    
    class UpdateDelegator(obj: Updater) : Updater by obj
    
    class UpdateDelegator2(private val obj: Updater) {
        fun update(str: String){
            obj.update(str)
        }
    }
    
    fun main(args: Array<String>) {
        val dbUpdater = DbUpdater()
        UpdateDelegator(dbUpdater).update("dbdb")
    }
```
위와 같이 Delegator와 Delegatee를 만들어 줄 수 있는데 주목할 부분은 UpdateDelegator이다. by 키워드를 이용하면 인터페이스(Updater)의 함수가 by 오른쪽에 작성한 객체(obj)의 함수를 호출하도록 작성해 자동으로 UpdateDelegator에 추가되게 한다. 결국, 일일이 위임자를 작성할 필요가 없다는 것이다.

위임자 클래스에서 대행자를 호출하는 구문이 by에 의해 자동으로 작성된다는 개념인데, 이를 위해서는 약간의 규칙에 맞게 인터페이스, 클래스들을 준비해 주어야 한다. 위임자와 대행자가 같은 인터페이스를 구현하고 있어야 만이 by를 이용하여 위임 패턴을 구현할 수 있다.

### 어댑터 패턴과의 차이?

구조적으로는 매우 동일하다. 그러나 목적에 차이가 있다. 어댑터 패턴은 다른 여러가지를 같은 API로 사용하려는게 주목적이다. 반면, 위임 패턴은 원래 본인이 수행해야 하는 일정 정도의 업무를 다른 곳에 위임하기 위한 것이 주목적이다.

### 장점
많은 boilerplate code들을 생략할 수 있다.

### 델리게이션 프로퍼티

코틀린은 by를 이용해 클래스 위임을 대행하는 것과 같은 개념으로 프로퍼티의 위임도 제공한다. 만약 프로퍼티의 get(), set() 함수에 들어가는 로직이 여러 프로퍼티에 중복된다면, 매번 프로퍼티에 get(), set() 함수로 구현하지 말고 중복되는 로직을 구현하는 클래스를 만들어서 처리를 위임하자는 개념이다.
```kotlin
    class Test {
    	var sum: Int = 0
    		get() = field
    		set(value) {
    			field = 0
    			for(i in 1..value){
    				field += i
    			}
    		}
    }
    
    fun main(args: Array<String>) {
    	val obj: Test = Test()
    	obj.sum = 10
    	println(obj.sum)
    	obj.sum = 5
    	println(obj.sum)
    }
    
    // 55
    // 10
```
해당 로직을 가지는 프로퍼티가 프로그램 전반에 여러 개 나온다면, 매번 같은 로직을 프로퍼티 마다 get(), set() 함수로 추가해야 한다. 이럴 때 위임 프로퍼티를 이용하면 수고를 덜 수 있다.
```kotlin
    import kotlin.reflect.KProperty
    
    class MySumDelegate {
    	var result: Int = 0
    
    	operator fun getValue(thisRef: Any?, property: KProperty<*>): Int {
    		println("getValue call... ref : $thisRef, property : '${property.name}'")
    		return result
    	}
    
    	operator fun setValue(thisRef: Any?, property: KProperty<*>, value: Int) {
    		result = 0
    		println("setValue call... value : $value, '${property.name}'")
    		for(i in 1..value){
    			result += i
    		}
    	}
    }
    
    class Test {
    	var sum: Int by MySumDelegate()
    }
    
    fun main(args: Array<String>) {
    	val obj: Test = Test()
    	obj.sum = 10
    	println(obj.sum)
    	obj.sum = 5
    	println(obj.sum)
    }
```
프로퍼티를 대행할 클래스를 만드는 규칙이 있는데 getValue()와 setValue() 함수를 포함해야 한다. 프로퍼티를 이용할 때 이 함수들이 자동 호출되며 프로퍼티의 get(), set() 함수와 매핑된다.

getValue(), setValue() 함수는 operator 키워드를 추가해야 하며 두 번째 매개변수를 이용해 적용된 프로퍼티의 이름을 얻고, setValue() 함수는 세 번째 매개변수를 이용해 프로퍼티에 대입된 값을 얻는다.
