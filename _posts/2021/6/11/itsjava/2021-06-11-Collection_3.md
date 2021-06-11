---
layout: post
title: "[이것이자바다] chapter 15. 컬렉션 - Map 컬렉션"
description: " "
date: 2021-06-11
tags: [이것이자바다]
comments: true
share: true
---


## chapter15
## Map 컬렉션 

* Map 컬렉션은 키(key)와 값(value)으로 구성된 Entry 객체를 저장하는 구조를 가지고 있다. 여기서 키와 값은 모두 객체인데, 즉 기본타입(Primitive type)은 키와 값이 될 수 없다. 
* 키는 중복 저장될 수 없지만(같은 주소면 불가능 ), 값은 중복 저장될 수 있다(같은 주소여도 가능). 

* 만약 기존에 저장된 키와 동일한 키로 값을 저장하면 기존의 값은 없어지고 새로운 값으로 대치된다. ( put() 메소드 사용) 
* Map 컬렉션에는 HashMap ,Hashtable ,LinkedHashMap, Properties, TreeMap 등이 있다.

아래 표는 Map 컬렉션에서 공통적으로 사용 가능한 Map 인터페이스의 메소드들이다. **키로 객체들을 관리하기 때문에 키를 매개값으로 갖는 메소드가 많다.**

| 기능      | 메소드             | 설명                                                                  |
|-----------|--------------------|-----------------------------------------------------------------------|
|객체 추가  | V put(K key,V value)|주어진 키로 값을 저장. 새로운 키일 경우 null을 리턴하고 동일한 키가 있을 경우 값을 대체하고 이전의 값을 리턴 |
| 객체 검색 | boolean containsKey(Object key)| 주어진 키가 있는지 여부 | 
| | boolean containsValue(Object Value) | 주어진 값이 있는지 여부 |
| | **Set\<Map.Entry\<K,V>> entrySet()** | **키와 값의 쌍으로 구성된 모든 Map.Entry 객체를 Set에 담아서 리턴** | 
| | V get(Object key) | 주어진 키가 있는 값을 리턴 |
| | boolean isEmpty() | 컬렉션이 비어 있는지 여부  |
| | Set\<K> keySet()  | 모든 키를 Set 객체에 담아서 리턴 | 
| | int size()   | 저장된 키의 총 수를 리턴 | 
| | Collection\<V> values() | 저장된 모든 값을 Collection에 담아서 리턴(값이 중복될 경우도 있기에 Collection(List,Set)에 담는다. |
| 객체 삭제 | void clear() | 모든 Map.Entry(키와 값)를 삭제 |
|  | V remove(Object key) | 주어진 키와 일치하는 Map.Entry를 삭제하고 값을 리턴 | 

=> Map 컬렉션도 List,Set 컬렉션처럼 제네릭 타입이다. 위의 표의 K와 V는 타입 파라미터이다. <br>

```java
Map<String,Integer> map = ~;
map.put("홍길동",30);
int age = map.get("홍길동"); //주어진 키("홍길동")가 있는 값을 리턴
map.remove("홍길동"); //주어진 키로 Entry<Key,Value> 객체 삭제
```

keySet() 메소드를 이용해서 전체 객체 출력하기(for문 사용)<br>
```java

public class KeySetExample {
    public static void main(String[] args) {
        Map<String,Integer> map = new HashMap<>();
        map.put("kimdo", 27);
        map.put("Park", 28);

        Set<String> keySet = map.keySet();
        for(String name: keySet){
            System.out.print("name: "+ name);
            System.out.println(" age: " + map.get(name));
        }
    }
}
```

entrySet() 메소드로 모든 Map.Entry를 Set 컬렉션으로 얻은 다음, 반복자를 통해 Map.Entry를 하나씩 얻고 getKey()와  getValue() 메소드를 이용해 키와 값 얻기<br>
```java
public class EntrySetExample {
    public static void main(String[] args) {
        Map<String,Integer> map = new HashMap<>();
        map.put("kim",27);
        map.put("gyu", 26);

        Set<Map.Entry<String,Integer>> entrySet = map.entrySet();

        Iterator<Map.Entry<String,Integer>> entryiterator = entrySet.iterator();

        while(entryiterator.hasNext()){
            Map.Entry<String,Integer> entry = entryiterator.next();
            System.out.print("name: "+entry.getKey());
            System.out.println(" age: "+ entry.getValue());
        }
        /*
 for (Map.Entry<String, Integer> entry : entrySet) {
            System.out.print("name: " + entry.getKey());
            System.out.println(" age: " + entry.getValue());
        }
        */

    }
}
```
* Map 컬렉션은 반복자를 직접적으로 사용할 수 없다. 따라서 keySet(), entrySet() 메소드를 이용하여 Set으로 반복자를 사용하자.

### HashMap

=> HashMap은 Map 인터페이스를 구현한 대표적인 Map 컬렉션이다. **HashMap의 키로 사용할 객체는 Object 클래스의 hashCode()와 equals() 메소드를 각각 재정의해야 한다** 동등 객체 , 즉 논리적으로 동등하려면 키가 hashCode()의 리턴값이 같아야 하고, equals() 메소드가 true를 리턴해ㅑ 한다. <br>

* 주로 키 타입은 String 클래스를 많이 사용한다.(String은 문자열이 같은 경우 동등 객체가 될 수 있도록 hashCode()와 equals()메소드가 재정의되어 있다.)

```java
Map<K,V> map = new HashMap<K,V>();
//키 타입, 값 타입

Map<String, Integer> map = new HashMap<>();
```

hashMap 예제 <br>
```java
public class HashMapExample1 {
    public static void main(String[] args) {
       //Map 컬렉션 생성
        Map<String,Integer> map = new HashMap<>();

        map.put("최호권", 27);
        map.put("함형규", 26);
        map.put("김현준", 27);
        System.out.println("총 객체 수: " + map.size());

        //객체 찾기
        System.out.println("\t최호권 나이: " + map.get("최호권"));

        //객체를 하나씩 출력
        Set<Map.Entry<String,Integer>> entrySet = map.entrySet();
        for(Map.Entry<String,Integer> entry: entrySet){
            System.out.print("이름: "+entry.getKey());
            System.out.println(" 나이: "+entry.getValue());
        }
        System.out.println();

        map.remove("김현준");
        System.out.println("총 객체 수: " + map.size());

        entrySet = map.entrySet();
        for(Map.Entry<String,Integer> entry: entrySet){
            System.out.print("이름: "+entry.getKey());
            System.out.println(" 나이: "+entry.getValue());
        }
        System.out.println();

        //객체 전체 삭제
        map.clear();
        System.out.println("총 Entry 수: " +map.size());
    }
}
```

hashCode(), equals() 재정의하여 HashMap의 키가 될 자격이 있는 객체 만들기 <br>
```java

public class HashMapExample2 {
    public static void main(String[] args) {
        Map<Student,Integer> map = new HashMap<>();
        map.put(new Student(1,"Kimdo"), 99);
        map.put(new Student(2, "other"), 50);
        map.put(new Student(2,"other"), 50);

        //Map은 향상된  for문을 사용할 수 없으므로 entrySet을 이용하자.
        Set<Map.Entry<Student,Integer>> entrySet = map.entrySet();

        for(Map.Entry<Student,Integer> entry : entrySet) {
            System.out.print("학번: "+ entry.getKey().sno);
            System.out.print(" 이름: "+entry.getKey().name);
            System.out.println(" 코딩 점수: " + entry.getValue());
        }
        int size = map.size();
        if(size == 2) {
            System.out.println("객체 수가 " + size + "이므로 HashMap의 키가 중복없이 잘 작동함을 알 수 있다.");
        }
    }
}
```
### Hashtable

* Hashtable은 HashMap과 동일한 내부 구조를 가지고 있다. Hashtable도 키로 사용할 객체는 hashCode()와 equals() 메소드를 재정의해서 동등 객체가 될 조건을 정해야 한다. 
* HashMap과의 차이점은 Hashtable은 **동기화된(synchronized) 메소드로 구성되어 있기 때문에 멀티 스레드가 동시에 이 메소드를 실행할 수는 없고, 하나의 스레드가 실행을 완료해야만 다른 스레드를 실행할 수 있다.** 이것을 스레드가 안전(thread safe)하다고 말한다.

```java
Map<K,V> map = new Hashtable<K,V>();

//객체 String,Integer 넣음
Map<String,Integer> map = new Hashtable<>();
```

아이디와 비밀번호 검사하기 <br>
```java
public class HahTableExample {
    public static void main(String[] args) {
        Map<String,String> map = new Hashtable<>();

        //id & password
        map.put("spring","12");
        map.put("summer", "123");
        map.put("fall", "1234");
        map.put("winter", "12345");

        Scanner scanner = new Scanner(System.in);

        while(true){
            System.out.println("아이디와 비밀번호를 입력해주세요(q: 나가기)");
            System.out.print("아이디: ");
            String id = scanner.nextLine();
            if(id.equals("q"))
                break;

            System.out.print("비밀번호: ");
            String password = scanner.nextLine();

            if(map.containsKey(id)){
                if(map.get(id).equals(password)){
                    System.out.println("로그인 되었습니다.");
                    break;
                }else {
                    System.out.println("비밀번호가 일치하지 않습니다.");
                }
            }else{
                System.out.println("아이디가 존재하지 않습니다.");
            }
        }
    }
}
```


### Properties

* Properties는 Hashtable의 하위 클래스이기 때문에 Hashtable의 모든 특성을 그래로 가지고 있다.
* 차이점은 Hashtable은 키와 값을 다양한 타입으로 저장이 가능한데 비해 **Properties는 키와 값을 String 타입으로 제한한 컬렉션**이다. 
* Properties는 애플리케이션의 옵션 정보, 데이터베이스 연결 정보 그리고 국제화(다국어) 정보가 저장된 프로퍼티(~.properties)파일을 읽을 때 주로 사용한다. 

=> 나중에 해보자<br>
