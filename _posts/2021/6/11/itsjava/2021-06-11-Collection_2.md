---
layout: post
title: "[이것이자바다] chapter 15. 컬렉션 - Set 컬렉션"
description: " "
date: 2021-06-11
tags: [이것이자바다]
comments: true
share: true
---

## chapter 15
## Set 컬렉션 

* Set 컬렉션은 저장 순서가 유지되지 않는다.(List는 유지 된다.)또한 객체를 중복해서 저장할 수 없고, 하나의 null만 저장할 수 있다.

* Set 컬렉션은 수학의 집합(set)에 비유될 수 있다. 집합은 순서와 상관없고 중복이 허용되지 않기 때문이다. 

* 인덱스(index)로 관리하지 않기 때문에 인덱스를 매개값으로 갖는 메소드가 없다. 

* Set 컬렉션에는 Hashset, LinkedHashSet, TreeSet 등이 있다. 
 
| 기능     | 메소드              | 설명                                         |
|----------|---------------------|----------------------------------------------|
| 객체 추가| boolean add(E e )  | 주어진 객체를 저장, 객체가 성공적으로 저장되면 true를 리턴하고 중복 객체면 false를 리턴|
| 객체 검색| boolean contains(Object o) | 주어진 객체가 저장되어 있는지 여부 |
|  | boolean isEmpty()  | 컬렉션이 비어 있는지 조사 |
| | Iterator\<E> iterator() | 저장된 객체를 한번씩 가져오는 반복자 리턴 |
| | int size()  | 저장되어 있는 전체 객체 수 리턴 |
| 객체 삭제 | void clear() | 저장된 모든 객체를 삭제 |
|  | boolean remove(Object o) | 주어진 객체를 삭제 |
=> 메소드의 매개 변수 타입과 리턴 타입에 E라는 타입 파라미터가 있는데, 이것은 Set 인터페이스가 **제네릭 타입**이기 때문이다. <br>

* Set 컬렉션은 **인덱스로 객체를 검색해서 가져오는 메소드가 없다.** 대신, 전체 객체를 대상으로 한번씩 반복해서 가져오는 **반복자(Iterator)** 를 제공한다. 반복자는 Iterator 인터페이스를 구현한 객체를 말하는데, iterator() 메소드를 호출하면 얻을 수 있다. 

```java
Set<String> set = ...;
Iterator<String> iterator = set.iterator(); // Set 컬렉션 변수 set의 iterator()메소드를 통해 Iterator 인터페이스를 구현한 객체 생성.
```

Iterator 인터페이스에 선언된 메소드들 <br>

| 리턴 타입 | 메소드 명 | 설명                                                         |
|-----------|-----------|--------------------------------------------------------------|
| boolean   | hasNext() | 가져올 객체가 있으면 true를 리턴하고 없으면 false를 리턴한다.|
| E  | next() | 컬렉션에서 하나의 객체를 가져온다. |
| void | remove() | Set 컬렉션에서 객체를 제거한다. |

=> <br>
1. 먼저 hasNext()메소드를 통해 가져올 객체가 있는지 확인한다.(있으면 true, 없으면 false를 반환함)
2. next()메소드를 통해 객체를 하나씩 가져온다.
3. Iterator의 next() 메소드로 가져온 객체를 제거하고 싶다면 remove() 메소드를 호출한다. 


```java
Set<String> set = new Hashset<>();
Iterator<String> iterator = set.iterator();

while(iterator.hasNext()){
  //String 객체를 하나씩 가져옴
  String str = iterator.next();
  
}
// hasNext() 메소드는 가져올 객체가 있는지 확인한다. 있으면 true, 없으면 false를 반환한다. 
// next() 메소드는  하나의 객체를 가져온다. 

```
향샹된 for문<br>

```java
Set<String> set = new Hashset<>();
for(String str: set){
  Syetem.out.println(str);
}
//Iterator 인터페이스 객체 없이 향상된 for문을 이용해 전체 객체를 대상으로 반복할 수 있다. 
```

remove() 메소드로 Iterator의 next() 메소드로 가져온 객체를 제거가능하다. <br>
```java
while(iterator.hasNext()){
  String str = iterator.next();
  if(str.equals("홍길동")
    iterator.next(); // 단 이 코드는 str이 "홍길동"일때의 loop가 끝나고 다음 loop가 돌때에 적용되므로 다음 루프부터 "홍길동"이란 객체가 set에서 삭제가 되는 것이다.

}
```

### HashSet 

* HashSet은 Set 인터페이스의 구현 클래스로, HashSet을 생성하기 위해서는 다음과 같이 기본 생성자를 호출하면 된다. 타입 파라미터 E에는 컬렉션에 저장할 객체 타입을 지정하면 된다. 아래는 String을 대입하였다. 

```java
Set<E> set = new HashSet<E>();
Set<String> set = new HashSet<String>();
```

* HashSet의 저장될 객체는 hashCode()와 equals() 메소드를 재정의해서 동등 객체가 될 조건을 정해야한다. 그렇지 않으면 서로 논리적으로 동등한 객체임에도 불구하고 중복 저장될 수 있다. 
* 예를 들어, 문자열을 HashSet에 저장할 경우, 같은 문자열을 갖는 String 객체는 동등한 객체로 간주되고 다른 문자열을 갖는 String 객체는 다른 객체로 간주되는데, 그 이유는 String 클래스가 Object클래스의 hashCode()와 equal()메소드를 재정의해서 같은 문자열일 경우 hashCode()의 리턴값(int)이 같게, equals()의 리턴값이 true가 나오도록 했기 때문이다. 

HashSet의 String객체 추가,검색,제거 <br>
```java
public class HashSetExample {
    public static void main(String[] args) {
        Set<String> set = new HashSet<>();

        set.add("java");
        set.add("kotlin");
        set.add("C");
        set.add("java"); //String 클래스는 Object의 hashCode(), equals()를 재정의해서
        // 같은 문자열일 경우 hashCode()의 리턴값(int)이 같게, equals()의 리턴값이 true가 나오도록 했기 때문에
        // Set의 특성대로 중복 없이 추가,삭제,검색을 할 수 있다.

        Iterator<String> iterator = set.iterator();
        int size  = set.size();
        System.out.println("총 객체 수: " + size);


        while(iterator.hasNext()) {
            String str = iterator.next();
            System.out.println(str);
        }
        System.out.println();
        set.remove("kotlin");


        size = set.size();
        System.out.println("총 개수: " +size);
        for(String str: set)
            System.out.println(str);

        set.clear();
        if(set.isEmpty()){
            System.out.println("set에 들어있는 객체가 없습니다. 비어 있음");
        }
    }
}
```


**hashCOde(), equals() 메소드 재정의해서 hashSet의 객체로 써먹기**<br>
```java

class Member {

    String name;
    int age;

    Member(String name, int age){
        this.name = name;
        this.age = age;
    }

    @Override
    public int hashCode(){
        return name.hashCode()+age;
        //String(name)이 재정의한 hashCode()를 사용하자!
    }


    @Override
    public boolean equals(Object obj) {
        if(obj instanceof Member){
            Member member = (Member)obj;
            return member.name.equals(name) && (member.age == age);
        }
        else
            return false;
    }

 
}
```

실행해보기<br>
```java
import java.util.HashSet;
import java.util.Set;

public class HashSetExmaple2 {
    public static void main(String[] args) {
        Set<Member> set = new HashSet<>();
        set.add(new Member("kim", 27));
        set.add(new Member("kim", 27));

        for(Member member: set){
            System.out.print("name: " +member.name);
            System.out.println(" age: " + member.age);
        }
    }
}

//실행 결과
//name: kim age: 27
```

=> Object 클래스의 hashCode() , equals() 메소드를 재정의하지 않으면 Set 컬렉션에 논리적으로 동등한 객체임에도 불구하고 중복 저장될 수 밖에 없다. 왜냐하면 Object 클래스의 hashCode(), equals() 모두 **객체의 주소를 참조하여 비교하기 때문에** 주소만 다르면 논리적으로도 다르다고 판단하여 동등 비교를 할 수 없기 때문이다. <br>


