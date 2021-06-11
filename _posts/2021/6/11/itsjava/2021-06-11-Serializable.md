---
layout: post
title: "[이것이자바다] chapter . Serializable"
description: " "
date: 2021-06-11
tags: [이것이자바다]
comments: true
share: true
---

## Serializable
## 직렬화가 가능한 클래스

* 자바는 Serializble 인터페이스를 구현한 클래스만 직렬화할 수 있도록 제한하고 있다. Serialiable 인터페이스는 필드나 메소드가 없는 빈 인터페이스지만, 객체를 직렬화할 때 private 필드를 포함한 모든 필드를 **바이트로 변환해도 좋다는 표시를 한다.**

```java
public class XXX implements Serializable { } 
```

객체를 직렬화하면 바이트로 변환되는 것은 필드들이고, 생성자 및 메소드는 직렬화에 포함되지 않는다. 따라서 역직렬화할 때에는 필드의 값만 복원된다.<br>
하지만 모든 필드가 직렬화 대상이 되는 것은 아니고 **transient 나 static 필드는 직렬화가 되지 않는다.**

```java
public class XXX implements Serializable {
  public int field1;  //직렬화 가능 
  protected int field2; //직렬화 가능
  int field3;  //직렬화 가능
  private int field4;  //직렬화 가능
  
  public static int field5; // 직렬화 불가능 
  transient int field6; // 직렬화 불가능 

}
```

* 역직렬화해서 필드의 값을 복원할 때, 새로운 인스턴스가 생성된다. 따라서 싱글턴인 경우 역직렬화할때 싱글턴이 깨질 위험이 있다. 이 경우 직렬화할 때 모든 인스턴스 필드를 transient이라고 선언하고, readResolve 메소드를 추가해야 싱글턴이 깨지지 않는다.



추후에 더 작성할 계획이다. <br>
