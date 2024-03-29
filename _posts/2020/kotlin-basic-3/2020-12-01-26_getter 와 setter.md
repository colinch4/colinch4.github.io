---
layout: post
title: "[코틀린기초] 26. getter 와 setter"
description: " "
date: 2020-12-01
tags: [kotlin]
comments: true
share: true
---  
  
  코틀린에서는 프로퍼티만 선언해줘도 자동적으로 getter와 setter를 생성해준다.
  
  단, 불변형인 val은 getter만 생성해준다.
  
## getter, setter 지정하기
  
  프로퍼티 밑에 탭을 한칸 넣고 getter와 setter를 지정할 수 있다.
 
  **field** 를 사용하여 프로퍼티를 참조하는 변수로 사용한다. 안그러면 무한루프가 발생한다.
  
  ```
  class user(_id: Int, _name: String, _age:Int){
    val id: Int = _id
      get() = field   //여기에 id를 사용하게되면 계속 getter가 호출되어 무한루프가 발생!!!! 
      
    var name: String = _name
      get() = field
      set(value){     // value 말고 다른 거 써도 된다.
        field = value
      }
    
    var age: Int = _age
       get() = field
       set(value){
        field = value + 10    // 커스텀 세터
       }    
  }

  ```
  
  임시적인 보조 프로퍼티를 사용하여 구성할 수도 있다.
  
  ```
  class user(_id: Int, _name: String, _age:Int){
    val id: Int = _id
    private var tempName:String? = null //  임시 프로퍼티 
      
    var name: String = _name
      get(){
        if(tempName == null) tempName = "NONAME"
        return tempName ?: throw AssertionError(""Asserted by others)
      }
      set(value){
        println("The name was changed")
        field = value.toUpperCase() //  받은 인자를 대문자로 변경해 프로퍼티에 할당
      }
    
    var age: Int = _age
       get() = field
       set(value){
        field = value + 10    // 커스텀 세터
       }    
  }
  ```
  
## 프로퍼티 오버라이딩
  
  부모의 프로퍼티가 val 인 것을 자식이 var로 오버라이딩 가능
  
  그러나 반대의 경우는 불가능!! 
  
  ```
  open class First{
    open val x : Int = 0    //  오버라이딩 가능
      get(){
        println("First x")
        return field
      }
    val y : Int = 0   // open 키워드가 없어서 상속 불가
  }
  
  class Second : First(){
    override var x: Int = 0   // 프로퍼티 오버라이딩
      get(){
        println("Second x")   // getter가 오버라이딩되어 구현이 다르다
        return field + 3
      }
      
      set(value){
        field = value + 10
      }
  }
  
  fun main(){
    val second = Second()
    println(second.x)   //  오버라이딩된 x
    println(second.y)   //  부모로부터 상속받은 y
  }
  ```

  
