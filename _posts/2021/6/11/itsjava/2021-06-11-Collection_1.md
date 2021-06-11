---
layout: post
title: "[이것이자바다] chapter 15. 컬렉션 - List 컬렉션"
description: " "
date: 2021-06-11
tags: [이것이자바다]
comments: true
share: true
---

## List 컬렉션 

* List 컬렉션은 객체를 일렬로 늘어놓는 구조를 가지고 있다.
* 객체를 인덱스로 관리하기 때문에 객체를 저장하면 자동 인덱스가 부여되고 **인덱스로 객체를 검색, 삭제할 수 있는 기능**을 제공한다.
* List 컬렉션은 객체 자체를 저장하는 것이 아니라 다음 그림과 같이 객체를 **참조**한다. 동일한 객체를 중복 저장할 수 있는데, 이 경우 동일한 번지가 참조된다. 
(null 도 저장이 가능한데, 이 경우 해당 인덱스는 객체를 참조하지 않는다.)<br>

| 기능     | 메소드               | 설명                                       |
|----------|----------------------|--------------------------------------------|
|객체 추가 | boolean add(E e)     | 주어진 객체를 **맨 끝**에 추가                 |
|          | void add(int index, E element) | 주어진 인덱스에 객체를 추가      |
|     |  E set(int index, E element ) | 주어진 인덱스에 저장된 객체를 주어진 객체로 바꿈 | 
| 객체 검색 | boolean contains(Object o) | 주어진 객체가 **저장되어 있는지 여부**   |
|  | E get(int index)  | 주어진 인덱스에 저장된 객체를 리턴 |
|  | boolean isEmpty() | 컬렉션이 비어 있는지 조사 |
|  | int size()        | 저장되어 있는 전체 객체 수를 리턴 | 
| 객체 삭제 | void clear() | **저장된 모든 객체를 삭제** | 
|  | E remove(int index) | 주어진 인덱스에 저장된 객체를 삭제 | 
| | boolean remove(Object o) |주어진 객체를 리스트에서 삭제(메소드 한번 호출에 객체 한 개 제거할 수 있음) |

=> List 인터페이스는 제네릭 타입이기 때문에, 구체적인 타입은 구현 객체를 생성할 때 결정된다. <br>

* 만약 전체 객체를 대상으로 하나씩 반복해서 저장된 객체를 얻고 싶다면 다음과 같이 for문을 사용할 수 있다. 

```java
 List<String> list = ...;
 for(int i=0; i<list.size(); i++){
   String str = list.get(i);
 }
//위와 같이 List의 size() 메소드를 이용하여 for문을 만들도록 하자.


for(String str : list){

}
// 인덱스가 필요 없다면 위와 같이 향상된 for문을 사용해도 좋다.

```

### ArrayList
* ArrayList에 객체를 추가하면 객체가 인덱스로 관리된다. 
* ArrayList가 일반 배열과 큰 차이점을 가지고 있는 것은 배열은 생성할 때 크기가 고정되고 사용중에 크기를 변경할 수 없지만, **ArrayList는 저장 용량(capacity)을 초과한 객체들이 들어오면 자동적으로 저장 용량(capacity)이 늘어난다는 점이다.**
* 하지만 이러한 ArrayList도 단점이 존재한다. 중간 인덱스에 객체를 추가할때는 원래 객체부터 뒤로 1씩 밀려나고, 중간 인덱스에 객체를 삭제하는 경우에는 뒤의 인덱스의 객체들이 앞으로 1씩 당겨지는 특징이 있다. 따라서 삽입이나 제거의 경우에 ArrayList는 시간적으로 낭비가 크므로 조히하는 경우에만 ArrayList를 사용하고,  삽입, 삭제가 잦은 경우는 LinkedList를 사용하도록 하자.

저장 공간을 초과해도 ArrayList는 동작한다. <br>
```java
import java.util.ArrayList;
import java.util.List;

public class ArrayListExample {

    public static void main(String[] args) {
        
        // ArrayList는 배열의 크기를 초과해도 오류가 나지 않는다. 
        // 자동적으로 저장 용량(capacity)가 늘어나기 때문이다.
        List<String> list = new ArrayList<>(5);
        for(int i=0; i<10;i++)
            list.add(String.valueOf(i));
        for(String str: list)
            System.out.print(str+ " ");
        System.out.println();
    }
}
```

Array\_List 사용 예 <br> 
```java
import java.util.ArrayList;
import java.util.List;

public class ArrayListExample2 {
    public static void main(String[] args) {
        List<String> list = new ArrayList<String>();

        list.add("java"); // String 객체를 저장.
        list.add("JDBC");
        list.add("Servlet/JSP");
        list.add(2, "database");
        list.add("iBATIS");
        list.add("iBATIS");

        int size = list.size(); // 저장된 총 객체 수 얻기
        System.out.println("총 객체수: " +size);
        System.out.println();

        String skill = list.get(2); //2번 인덱스의 객체 얻기
        System.out.println("2: " + skill);
        System.out.println();

        for(int i=0; i<list.size(); i++){
            String str = list.get(i);
            System.out.println(i +": " + str);
        }
        System.out.println();

        list.remove(2); // 2번 인덱스 database 삭제됨.
        for(String str: list){
            System.out.println(str);
        }
        list.remove(2);

        System.out.println();
        for(String str: list){
            System.out.println(str);
        }

        System.out.println();
        list.remove("iBATIS");
        for(String str: list){
            System.out.println(str);
        }
    }
}
```
* 고정된 객체들로 구성된 List를 생성해야 할 때도 있다. 이런 경우에는 Arrays.asList(T ... a) 메소드를 사용하는 것이 간편하다.

```java
List<T> list = Arrays.asList(T... a);
//Arrays.asList(T..a) 메소드는 ArrayList 와 다르게 크기가 고정되어 있다. 
```
=> T 타입 파라미터에 맞게 asList()의 매개값을 순차적으로 입력하거나, T[] 배열을 매개값으로 주면 된다.<br>

Arrays.asList 예제 <br>
```java

import java.util.Arrays;
import java.util.List;

public class ArraysAsListExample {

    public static void main(String[] args) {
        List<String> list1 = Arrays.asList("홍길동", "신용권", "김도형");

        for(String str: list1)
            System.out.println(str);

        System.out.println();
        List<Integer> list2 = Arrays.asList(1,2,3);

        for(Integer i : list2)
            System.out.println(i);
    }
}
```

### Bector
* Vector는 ArrayList와 동일한 내부 구조를 가지고 있고, Vector를 생성하기 위해서는 저장할 객체의 타입을 **타입 파라미터로 표기**하고 기본 생성자를 호출하면 된다. 

```java
List<E> list = new Vector<E>();
```

* ArrayList와 다른 점은 Vector는 동기화된(synchronized) 메소드로 구성되어 있기 때문에 멀티 스레드가 동시에 이 메소드들을 실행할 수 없고, 하나의 스레드가 실행을 완료해야만 다른 스레드를 실행할 수 있다. 그래서 멀티 스레드 환경에서 안전하게 객체를 추가, 삭제할 수 있다. 이것을 스레드가 안전(Thread Safe)하다라고 말한다. 

```java

import java.util.List;
import java.util.Vector;

public class VectorExample {

    public static void main(String[] args){
        List<Board> list = new Vector<>();

        list.add(new Board("제목1", "내용1", "글쓴이1"));
        list.add(new Board("제목2", "내용2", "글쓴이2"));
        list.add(new Board("제목3", "내용3", "글쓴이3"));
        list.add(new Board("제목4", "내용4", "글쓴이4"));
        list.add(new Board("제목5", "내용5", "글쓴이5"));

        list.remove(2);
        list.remove(3);


        //향샹된 for문
        for (Board board : list) {
            System.out.println(board.getSubject() + "\t" + board.getContent() + "\t" + board.getWriter());
        }

    }
}

```


### LinkedList
* LinkedList는 인접 참조를 링크해서 체인처럼 관리한다. 
* LinkedList는 특정 인덱스의 객체를 제거하면 앞 뒤 링크만 변경되고 나머지 링크는 변경되지 않는다. 그리고 특정 인덱스에 객체를 추가하는 경우에도 마찬가지이다. 
* ArrayList는 중간 인덱스의 객체를 제거하면 뒤의 객체는 인덱스가 1씩 앞으로 당겨지고, 중간 인덱스에 객체를 추가하면 원래 있던 객체부터 1씩 뒤로 물러나므로 시간적으로 오래 걸린다.
* 하지만 LinkedList는 삽입 삭제시, 해당 인덱스의 앞 뒤 링크만 변경되기 때문에 시간적으로 빠르다. 따라서 삽입 삭제가 잦은 경우에는 ArrayList 보다 LinkedList 가 훨씬 효율적이라고 할 수 있다. 



ArrayList vs LinkedList 삽입 속도 <br>  
```java
public class LinkedListExample {

    public static void main(String[] args) {
        List<String> list1 = new ArrayList<>();
        List<String> list2 = new LinkedList<>();

        long startTime;
        long endTime;

        startTime = System.nanoTime();
        for(int i=0; i<100000;i++){
            list1.add(0,String.valueOf(i));
        }
        endTime = System.nanoTime();
        System.out.println("ArrayList 걸린시간: " + (endTime - startTime) + "ns");

        startTime = System.nanoTime();
        for(int i=0; i<100000;i++){
            list2.add(0,String.valueOf(i));
        }
        endTime = System.nanoTime();
        System.out.println("LinkedList 걸린시간: " + (endTime - startTime) + "ns");
    }
}
//실행결과:
//ArrayList 걸린시간: 757624819ns
//LinkedList 걸린시간: 43813106ns
// => LinkedList 가 처리속도가 훨씬 빠르다. 
```
