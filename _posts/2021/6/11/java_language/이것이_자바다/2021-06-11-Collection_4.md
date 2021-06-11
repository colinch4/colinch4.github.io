---
layout: post
title: "[이것이자바다] chapter 15. 컬렉션 - 검색 기능을 강화시킨 컬렉션 TreeSet, TreeMap"
description: " "
date: 2021-06-11
tags: [이것이자바다]
comments: true
share: true
---


## chapter 15
## 검색 기능을 강화시킨 컬렉션 TreeSet, TreeMap

* 컬렉션 프레임워크는 검색 기능을 강화시킨 TreeSet과 TreeMap을 제공하고 있다. TreeSet은 Set컬렉션이고, TreeMap은 Map컬렉션이다. 
* 이 컬렉션들은 **이진 트리(binary tree)를 이용해서 계층적 구조(Tree 구조)를 가지면서 객체를 생성**한다. 


### 이진 트리 구조 
=> 이진 트리(binary tree)는 여러 개의 노드(node)가 트리 형태로 연결된 구조로, **루트 노트(root node)**라고 불리는 하나의 노드에서부터 시작해서 각 노드에 **최대 2개의 노드**를 연결할 수 있는 구조를 가지고 있다. <br>
=> 위아래로 연결된 두 노드를 부모-자식관계에 있다고 하며 위의 노드를 **부모 노드**, 아래의 노드를 **자식 노드**라 한다. 하나의 부모 노드는 최대 2 개의 자식 노드와 연결될 수 있다.<br>
=> 이진 트리는 부모 노드의 값보다 작은 노드는 왼쪽에 위치시키고, 부모 노드의 값보다 큰 노드는 오른쪽에 위치시킨다.<br>
(숫자가 아닌 문자를 저장할 경우에는 문자의 유니코드 값으로 비교한다.)<br>

Tree traversal(트리 순회) <br>

v: 노드 방문 ,L: 왼쪽 부분트리 운행, R: 오른쪽 부분트리 운행
1. Pre-Order(전 순회)
: vLR

2. In-Order(중 순회)
: LvR 

3. Post-Order(후 순회)
: LRv

### TreeSet 
* TreeSet은 **이진 트리(binary tree)**를 기반으로 한 Set 컬렉션이다. **하나의 노드는 노드값인 value와 왼쪽과 오른쪽 자식 노드를 참조하기 위한 두 개의 변수로 구성된다.** 
* TreeSet에 객체를 저장하면 자동으로 정렬되는데 부모값과 비교해서 낮은 것은 왼쪽 자식 노드에, 높은 것은 오른쪽 자식 노드에 저장된다. 

TreeSet<br>
```java
TreeSet<E> treeSet = new TreeSet<E>();
TreeSet<String> treeSet = new TreeSet<>();
```

=> Set 인터페이스 타입 변수에 대입해도 되지만 TreeSet 클래스 타입으로 대입한 이유는 **객체를 찾거나 범위 검색과 관련된 메소드를 사용하기 위해서이다.**<br>

TreeSet이 가지고 있는 메소드<br>
 
| 리턴 타입 | 메소드        | 설명                                      |
|-----------|---------------|-------------------------------------------|
| E | first() | 제일 낮은 객체를 리턴  | 
| E | last() | 제일 높은 객체를 리턴 | 
| E | lower(E e) | 주어진 객체보다 바로 아래 객체를 리턴 | 
| E | higher(E e) | 주어진 객체보다 바로 위 객체를 리턴 | 
| E | floor(E e) | 주어진 객체와 동등한 객체가 있으면 리턴, 만약 없다면 주어진 객체의 바로 아래의 객체를 리턴 |
| E | ceiling(E e) | 주어진 객체와 동등한 객체가 있으면 리턴, 만약 없다면 주어진 객체의 바로 위의 객체를 리턴 |
| E | pollFirst() | 제일 낮은 객체를 꺼내오고 컬렉션에서 제거함 | 
| E | pollLast() | 제일 높은 객체를 꺼내오고 컬렉션에서 제거함 | 

TreeSetExample<br>
```java
public class TreeSetExample{
    public static void main(String[] args) {
        TreeSet<Integer> scores = new TreeSet<>();
        scores.add(87);
        scores.add(98);
        scores.add(75);
        scores.add(95);
        scores.add(80);

        Integer score =null;

        //가장 낮은 값의 객체 리턴
        score = scores.first();
        System.out.println("가장 낮은 점수: "+ score);

        //가장 높은 값의 객체 리턴
        score = scores.last();
        System.out.println("가장 높은 점수: "+ score);

        score = scores.lower(95);
        System.out.println("95점 아래 점수: "+ score);

        score = scores.higher(95);
        System.out.println("95점 위 점수: "+ score);

        score = scores.floor(95);
        System.out.println("95점이거나 아래인 점수: "+ score);

        score = scores.ceiling(85);
        System.out.println("85점이거나 위인 점수: " +score);

        System.out.println();
        System.out.println("====================================");
        while(!scores.isEmpty()){
            int sc = scores.pollFirst(); //가장 낮은 값 꺼내고 삭제. 오름차순
            System.out.println("꺼낸 값: " + sc);
            System.out.println("남은 객체수: "+ scores.size());
        }
    }
}
```

다음 표는 TreeSet이 가지고 있는 정렬과 관련된 메소드들이다. <br>

|리턴 타입 | 메소드                 | 설명                                        |
|----------|------------------------|---------------------------------------------|
| Iterator\<E> | descendingIterator() | 내림차순으로 정렬된 Iterator를 리턴 | 
| NavigableSet\<E> | descendingSet() | 내림차순으로 정렬된 NavigableSet을 반환 | 

* descendingIterator() 메소드는 내림차순으로 정렬된 Iterator를 리턴한다.
* descendingSet() 메소드는 내림차순으로 정렬된 NavigableSet 객체를 리턴하는데 NavigableSet은 TreeSet과 마찬가지로 first(),last(),lower(),higher(), floor(), ceiling() 메소드를 제공하고, 정렬 순서를 바꾸는 descendingSet()메소드도 제공한다. 오름차순으로 정렬하고 싶다면 다음과 같이 descendingSet() 메소드를 두 번 호출하면 된다. 

```java
NavigableSet<E> descendingSet = treeSet.descendingSet();
NavigableSet<E> ascendingSet = descendingSet.descendingSet(); // 두번 호출
```

```java
public class TreeSetExample2 {
    public static void main(String[] args) {
        TreeSet<Integer> scores = new TreeSet<>();
        scores.add(50);
        scores.add(60);
        scores.add(70);
        scores.add(80);
        scores.add(90);

        Iterator<Integer> iterator = scores.descendingIterator();
        while(iterator.hasNext()){
           Integer score = iterator.next();
            System.out.println(score +" ");
        }

        System.out.println();

        NavigableSet<Integer> descendingSet = scores.descendingSet();
        for(Integer score: descendingSet)
            System.out.println(score +" ");


        System.out.println();
        NavigableSet<Integer> ascendingSet = descendingSet.descendingSet();
        for(Integer score: ascendingSet){
            System.out.println(score +" ");
        }
    }
}
```

* 다음은 TreeSet이 가지고 있는 범위 검색과 관련된 메소드들이다.

| 리턴 타입        | 메소드                   | 설명                                                                              |
|------------------|--------------------------|-----------------------------------------------------------------------------------|
| NavigableSet\<E> | headSet(E toElement, boolean inclusive)| 주어진 객체보다 낮은 객체들을 NavigableSet으로 리턴. 주어진 객체 포함 여부는 두번째 매개값에 따라 달라짐. |
| NavigableSet\<E> | tailSet(E fromElement, boolean inclusive) |주어진 객체보다 높은 객체들을 NavigableSet으로 리턴. 주어진 객체 포함 여부는 두번째 매개값에 따라 달라진다. | 
| NavigableSet\<E> | subSet(E fromElement, boolean fromInclusive, E toElement, boolean toInclusive) | 시작과 끝으로 주어진 객체 사이의 객체들을 NavigableSet으로 리턴. 시작과 끝 객체 포함여부는 두번째, 네 번째 매개값에 따라 달라진다. |

영어 단어를 정렬하고, 범위 검색해보기<br>
```java
public class TreeSetExample3 {
    public static void main(String[] args) {
        TreeSet<String> treeSet = new TreeSet<>();
        treeSet.add("apple");
        treeSet.add("forever");
        treeSet.add("description");
        treeSet.add("ever");
        treeSet.add("zoo");
        treeSet.add("base");
        treeSet.add("guess");
        treeSet.add("cherry");
        treeSet.add("chic");

        System.out.println("[c~f 사이의 단어 검색]");
        NavigableSet<String> rangeSet = treeSet.subSet
                ("c",true,"f",true);

        for(String word: rangeSet){
            System.out.println(word);
        }
    }
}
```

### TreeMap
* TreeMap도 TreeSet처럼 이진 트리를 기반으로 한 Map 컬렉션이다. TreeSet과의 차이점은 **키와 값이 저장된 Map.Entry를 저장한다는 점**이다.
* TreeMap에 객체를 저장하면 자동으로 정렬되는데, **기본적으로 부모 키값과 비교하여 키 값이 낮은 것은 왼쪽 자식 노드에, 키 값이 높은 것은 오른쪽 자식 노드에 Map.Entry 객체를 저장한다.**

```java
TreeMap<K,V> treeMap = new TreeMap<K,V>();
TreeMap<String, Integer> treeMap = new TreeMap<>();
```
=> Map 인터페이스 타입 변수에 대입해도 되지만 TreeMap 클래스 타입으로 대입한 이유는 특정 객체를 찾거나 범위 검색과 관련된 메소드를 사용하기 위해서이다.<br>

TreeMap이 가지고 있는 검색 관련 메소드<br>

| 리턴 타입 | 메소드        | 설명                                      |
|-----------|---------------|-------------------------------------------|
| Map.Entry\<K,V> | firstEntry() | 제일 낮은 Map.Entry를 리턴  | 
| Map.Entry\<K,V>  | lastEntry() | 제일 높은 Map.Entry를 리턴 | 
| Map.Entry\<K,V>  | lowerEntry(K key) | 주어진 키보다 바로 아래 Map.Entry를 리턴 | 
| Map.Entry\<K,V>  | higherEntry(K key) | 주어진 키보다 바로 위 Map.Entry를 리턴 | 
| Map.Entry\<K,V>  | floorEntry(K key) | 주어진 키와 동등한 키가 있으면 해당 Map.Entry를 리턴, 만약 없다면 주어진 키의 바로 아래의 키의 Map.Entry를 리턴 |
| Map.Entry\<K,V>  | ceilingEntry(K key) | 주어진 키와 동등한 키가 있으면 Map.Entry를 리턴, 만약 없다면 주어진 키의 바로 위의 키의 Map.Entry를 리턴 |
| Map.Entry\<K,V>  | pollFirstEntry() | 제일 낮은 Map.Entry를 꺼내오고 컬렉션에서 제거함 | 
| Map.Entry\<K,V>  | pollLastEntry() | 제일 높은 Map.Entry를 꺼내오고 컬렉션에서 제거함 | 

```java
import java.util.Map;
import java.util.TreeMap;

public class TreeMapExample1 {
    public static void main(String[] args) {
        TreeMap<Integer,String> scores = new TreeMap<>();
        scores.put(87,"홍길동");
        scores.put(98,"이동수");
        scores.put(75,"박길순");
        scores.put(95,"신용권");
        scores.put(80,"김자바");

        Map.Entry<Integer,String> entry = null;

        entry = scores.firstEntry(); //가장 낮은 키의 entry.
        System.out.println("가장 낮은 점수: " + entry.getKey() +" -" + entry.getValue());

        entry = scores.lastEntry(); //가장 큰 키의 entry
        System.out.println("가장 큰 점수: " + entry.getKey() +" -"+ entry.getValue());

        entry = scores.lowerEntry(95);
        System.out.println("95점 아래 점수: " +entry.getKey() +" -" + entry.getValue());

        entry = scores.higherEntry(95);
        System.out.println("95점 위 점수: " + entry.getKey() +" -"+entry.getValue());

        entry = scores.floorEntry(95);
        System.out.println("95점이거나 아래인 점수: "+ entry.getKey() +" -" +entry.getValue());

        entry = scores.ceilingEntry(85);
        System.out.println("85점이거나 바로 위의 점수: " +entry.getKey()+ " -" +entry.getValue());

        System.out.println();
        while(!scores.isEmpty()){
           entry = scores.pollFirstEntry(); // 오름차순
           System.out.println("받은 점수: "+entry.getKey()+ " 사람: "+entry.getValue());
            System.out.println("남은 객체 수: " + scores.size());
        }
    }
}
```

|리턴 타입 | 메소드                 | 설명                                        |
|----------|------------------------|---------------------------------------------|
| NavigableSet\<K> | descendingKeySet() | 내림차순으로 정렬된 키의 NavigableSet을 리턴 | 
| NavigableMap\<K,V> | descendingMap() | 내림차순으로 정렬된 Map.Entry의 NavigableMap을 반환 | 

```java
NavigableMap<K,V> descendingMap = treeMap.descendingMap();//내림차순
NavigableMap<K,V> ascendingMap = descendingMap.descendingMap(); //오름차순
```

객체 정렬하기<br>
```java
package CollectionFramework.Tree;

import java.util.*;

public class TreeMapExample2 {
    public static void main(String[] args) {
        TreeMap<Integer,String> scores = new TreeMap<>();
        scores.put(87,"홍길동");
        scores.put(93,"이동수");
        scores.put(75,"박길순");
        scores.put(95,"신용권");
        scores.put(80,"김자바");

        Set<Map.Entry<Integer,String>> entrySet2 = scores.entrySet();
        for(Map.Entry<Integer,String> entry: entrySet2){
            System.out.println(entry.getKey() +"-" + entry.getValue());
        }
        System.out.println();


        NavigableSet<Integer> descendingKeySet = scores.descendingKeySet();
        System.out.println("[내림차순]");
        for(Integer score: descendingKeySet){
            System.out.print("받은 점수: " + score);
            System.out.println(" 사람: " + scores.get(score));
        }
        System.out.println();
        System.out.println("[내림차순]");
        //오름차순
        //Map은 for문을 돌릴 수 없으므로 Set을 활용하자.
        NavigableMap<Integer,String> descendingMap = scores.descendingMap();
        Set<Map.Entry<Integer,String>> entrySet = descendingMap.entrySet();
        for(Map.Entry<Integer,String> entry :entrySet){
            System.out.println(entry.getKey() +"-"+ entry.getValue());
        }

        //내림차순
        System.out.println();
        System.out.println("[오름차순]");
        descendingMap = descendingMap.descendingMap();
        entrySet = descendingMap.entrySet();
        for(Map.Entry<Integer,String> entry :entrySet){
            System.out.println(entry.getKey() +"-"+ entry.getValue());
        }

    }
}

```

| 리턴 타입        | 메소드                   | 설명                                                                              |
|------------------|--------------------------|-----------------------------------------------------------------------------------|
| NavigableMap\<K,V> | headMap(K toKey, boolean inclusive)| 주어진 키보다 낮은 키의 Map.Entry들을 NavigableMap으로 리턴. 주어진 키의 Map.Entry의 포함 여부는 두번째 매개값에 따라 달라짐. |
| NavigableMap\<K,V> | tailMap(K fromKey, boolean inclusive) |주어진 키보다 높은 키들의 NavigableMap으로 리턴. 주어진 키의 Map.Entry의 포함 여부는 두번째 매개값에 따라 달라진다. | 
| NavigableMap\<K,V> | subMap(K fromKey, boolean fromInclusive, K toKey, boolean toInclusive) | 시작과 끝으로 주어진 키 사이의 키들의 Map.Entry을 NavigableMap으로 리턴. 시작과 끝 키의 Map.Entry 포함여부는 두번째, 네 번째 매개값에 따라 달라진다. |

키로 정렬하고 범위 검색하기 <br>
```java
public class TreeMapExample3 {
    public static void main(String[] args) {
        TreeMap<String,Integer> treeMap = new TreeMap<>();
        treeMap.put("apple",10);
        treeMap.put("forever",60);
        treeMap.put("description",40);
        treeMap.put("ever",50);
        treeMap.put("zoo",10);
        treeMap.put("base",20);
        treeMap.put("guess",70);
        treeMap.put("cherry",30);
        treeMap.put("chic",25);

        System.out.println("[c~f 사이의 단어 검색]");
        NavigableMap<String,Integer> navigableMap = treeMap.subMap
                ("c",true,"f",true);
        Set<Map.Entry<String,Integer>> entrySet = navigableMap.entrySet();

        for(Map.Entry<String,Integer> entry: entrySet){
            System.out.print("word: " + entry.getKey());
            System.out.println(" number: " + entry.getValue());
        }
    }
}
```

### Comparable 과 Comparator

* TreeSet 객체와 TreeMap의 키는 저장과 동시에 **자동 오름차순**으로 정렬되는데, **숫자(Integer,Double)타입일 경우에는 값**으로 정렬하고, 문자열(String)일 경우에는 유니코드로 정렬한다. 

* TreeSet과 TreeMap은 정렬을 위해 java.lang.Comparable을 구현한 객체를 요구하는데, Integer, Double, String은 모두 Comparable 인터페이스를 구현하고 있다. **사용자 정의 클래스도 Comparable을 구현한다면 자동 정렬이 가능하다.** Comparable에는 compareTo()메소드가 정의되어 있기 때문에 **사용자 정의 클래스에서는 이 메소드를 오버라이딩(재정의)하여** 다음과 같이 리턴 값을 만들어야 한다. 

| 리턴 타입 | 메소드        | 설명                                                   |
|-----------|---------------|--------------------------------------------------------|
| int       | compareTo(T o) | 주어진 객체와 같으면 0을 리턴 <br> 주어진 객체보다 적으면 음수를 리턴 <br> 주어진 객체보다 크면 양수를 리턴|

=> **오름차순, 내림차순 다 가능하다.**


> 사용자 정의, compareTo() 메소드 오버라이딩 예제 

Comparable을 구현한 클래스<br>
```java
public class Person implements Comparable<Person> {

    String name;
    int age;
    
    Person(String name, int age){
        this.name = name;
        this.age = age;
    }
    
    @Override
    //나이로 비교하는 것으로 설정
    public int compareTo(Person o) {
        if(age<o.age) return -1;
        else if(age == o.age) return  0;
        else
            return 1;
    }
}
```
사용자 정의 객체를 나이 순으로 정렬하기 <br>

```java
public class ComparableExample {
    public static void main(String[] args) {
        TreeSet<Person> treeSet = new TreeSet<>();

        treeSet.add(new Person("KIM", 27));
        treeSet.add(new Person("GYU",26));
        treeSet.add(new Person("LEE",24));

        System.out.println("[나이 오름차순]");
        for(Person person: treeSet){
            System.out.println(person.name +"-" + person.age);
        }
    }
}
```

*  TreeSet의 객체와 TreeMap의 키가 Comparable을 구현하고 있지 않을 경우에는 저장하는 순간 **ClassCastException**이 발생하므로 주의하자.
ClassCastException<br>
```java
Exception in thread "main" java.lang.ClassCastException: class CollectionFramework.Compare.Person cannot be cast to class java.lang.Comparable (CollectionFramework.Compare.Person is in unnamed module of loader 'app'; java.lang.Comparable is in module java.base of loader 'bootstrap')
	at java.base/java.util.TreeMap.compare(TreeMap.java:1291)
	at java.base/java.util.TreeMap.put(TreeMap.java: 536)
	at java.base/java.util.TreeSet.add(TreeSet.java: 255)
	at CollectionFramework.Compare.ComparableExample.main(ComparableExample.java:9)
```

=>  그렇다면 비구현 객체를 정렬하는 방법은 없을까? 있다. **TreeSet 또는 TreeMap 생성자의 매개값으로 정렬자(Comparator)를 제공하면 Comparable 비구현 객체도 정렬시킬 수 있다.**<br>

Comparable 비구현 객체에 정렬자(Comparator) 정렬하기 <br>

```java
TreeSet<E> treeSet = new TreeSet<E>(new AscendingComparator() ); //오름차순 정렬자
TreeSet<E> treeSet = new TreeSet<E>(new DescendingComparator() );//내림차순 정렬자
```
=> 정렬자는 Comparator 인터페이스를 구현한 객체를 말하는데, Comparator 인터페이스에는 다음과 같이 메소드가 정의되어 있다. <br>

| 리턴타입  | 메소드          | 설명                                            |
|-----------|-----------------|-------------------------------------------------|
| int       | compare(T o1, T o2) | o1과 o2가 동등하다면 0을 리턴  | 
|   | | o1이 o2보다 앞에 오게 하려면 음수를 리턴 |
| | | o1이 o2보다 뒤에 오게 하려면 양수를 리턴 | 


Comparator을 통해 비구현 객체를 정렬하였고, 또 오름차순이 아닌 내림차순으로 정렬하였다.(오름차순,내림차순 둘다 가능하다!)<br>
```java
public class ComparatorExample {
    public static void main(String[] args) {
        //fruit의 가격을 기준으로(getPrice) Comparator 작성.
        Comparator<Fruit> comparator = (o1,o2)->{
            //큰것이 앞에 오도록
            if(o1.getPrice()>o2.getPrice())
                return -1;
            //작은 것이 뒤에 가도록
            else if(o1.getPrice()<o2.getPrice())
                return 1;
            else
                return 0;
        };

        TreeSet<Fruit> treeSet = new TreeSet<>(comparator); //내림차순 정렬
        treeSet.add(new Fruit("포도",3000));
        treeSet.add(new Fruit("수박",10000));
        treeSet.add(new Fruit("딸기", 6000));

        Iterator<Fruit> iterator = treeSet.iterator();
        while(iterator.hasNext()){
            Fruit fruit = iterator.next();
            System.out.print("과일 이름: " + fruit.getName());
            System.out.println(" 가격: "+ fruit.getPrice());
        }
    }
}
/*실행결과 
과일 이름: 수박 가격: 10000
과일 이름: 딸기 가격: 6000
과일 이름: 포도 가격: 3000
*/
```
