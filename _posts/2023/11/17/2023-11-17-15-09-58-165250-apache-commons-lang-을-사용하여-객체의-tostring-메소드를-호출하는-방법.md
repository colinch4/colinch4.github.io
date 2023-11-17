---
layout: post
title: "[java] Apache Commons Lang 을 사용하여 객체의 toString() 메소드를 호출하는 방법"
description: " "
date: 2023-11-17
tags: [java]
comments: true
share: true
---

Java에서 객체의 `toString()` 메소드를 호출하는 가장 간단한 방법은 `System.out.println()`을 사용하는 것입니다. 그러나 때로는 더 복잡한 상황에서 객체를 문자열로 변환해야 할 수도 있습니다. 이러한 경우에는 Apache Commons Lang 라이브러리의 `ToStringBuilder` 클래스를 사용할 수 있습니다.

## Apache Commons Lang

Apache Commons Lang은 자주 사용되는 자바 클래스에 대한 보조 기능 및 유틸리티 메소드를 제공하는 라이브러리입니다. `ToStringBuilder`는 이 라이브러리의 구성원 중 하나로, 객체를 문자열로 변환하는 데 사용됩니다.

## `ToStringBuilder`를 사용한 객체의 문자열 변환

1. 먼저, Apache Commons Lang 라이브러리를 프로젝트에 추가해야 합니다. Maven을 사용하는 경우 `pom.xml` 파일에 다음 의존성을 추가하십시오.

```xml
<dependency>
   <groupId>org.apache.commons</groupId>
   <artifactId>commons-lang3</artifactId>
   <version>3.12.0</version>
</dependency>
```

2. 객체가 `toString()` 메소드를 호출할 때 `ToStringBuilder`를 사용하려면 다음과 같이 코드를 작성하십시오.

```java
import org.apache.commons.lang3.builder.ToStringBuilder;

public class MyClass {
   private String name;
   private int age;

   // 생성자, getter 및 setter 생략

   @Override
   public String toString() {
      return ToStringBuilder.reflectionToString(this);
   }
}
```

3. 이제 `MyClass` 객체를 문자열로 변환하려면 다음과 같이 코드를 작성하십시오.

```java
MyClass myObject = new MyClass();
myObject.setName("John");
myObject.setAge(30);

String objectAsString = myObject.toString();
System.out.println(objectAsString);
```

위의 예제에서 `ToStringBuilder.reflectionToString()` 메소드는 객체의 모든 필드를 반영하여 문자열로 변환합니다. 이를 통해 객체의 상세 정보를 포함한 문자열을 얻을 수 있습니다.

## 결론

Apache Commons Lang의 `ToStringBuilder` 클래스를 사용하면 자바 객체를 간편하게 문자열로 변환할 수 있습니다. 이를 통해 디버깅이나 기타 필요한 상황에서 객체의 내용을 쉽게 확인할 수 있습니다.

## 참고 자료

- [Apache Commons Lang 공식 문서](https://commons.apache.org/proper/commons-lang/javadocs/api-release/org/apache/commons/lang3/builder/ToStringBuilder.html)