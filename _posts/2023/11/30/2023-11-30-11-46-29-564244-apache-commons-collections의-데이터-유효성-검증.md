---
layout: post
title: "[java] Apache Commons Collections의 데이터 유효성 검증"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

Apache Commons Collections는 자바 개발을 위한 유용한 라이브러리입니다. 이러한 라이브러리는 데이터 유효성 검증에도 도움을 줄 수 있습니다. 이번 포스트에서는 Apache Commons Collections를 사용하여 데이터 유효성을 검증하는 방법을 살펴보겠습니다.

## 1. Apache Commons Collections 라이브러리 추가

먼저, Apache Commons Collections를 프로젝트에 추가해야 합니다. 이를 위해 Maven을 사용한다면 `pom.xml` 파일에 다음 의존성을 추가하십시오.

```xml
<dependencies>
    <dependency>
        <groupId>org.apache.commons</groupId>
        <artifactId>commons-collections4</artifactId>
        <version>4.4</version>
    </dependency>
</dependencies>
```

Gradle을 사용하는 경우, `build.gradle` 파일에 다음 코드를 추가하십시오.

```gradle
dependencies {
    implementation 'org.apache.commons:commons-collections4:4.4'
}
```

## 2. 데이터 유효성 검증하기

Apache Commons Collections를 사용하여 데이터 유효성을 검증하는 가장 간단한 방법은 `Predicate` 인터페이스를 사용하는 것입니다. `Predicate`는 주어진 객체에 대한 테스트를 수행하고 결과를 반환하는 함수입니다. 예를 들어, 문자열이 비어 있는지 여부를 확인하는 `Predicate`를 작성해보겠습니다.

```java
import org.apache.commons.collections4.Predicate;
import org.apache.commons.collections4.PredicateUtils;

public class DataValidator {

    public static Predicate<String> isEmpty() {
        return PredicateUtils.emptyPredicate();
    }

    public static void main(String[] args) {
        String text = "";
        if (isEmpty().test(text)) {
            System.out.println("문자열이 비어 있습니다.");
        } else {
            System.out.println("문자열이 비어 있지 않습니다.");
        }
    }
}
```

위의 예제에서는 `isEmpty()` 메서드를 통해 빈 문자열을 검증하는 `Predicate`를 생성하고, `test()` 메서드를 호출하여 문자열이 비어 있는지 확인합니다.

## 3. 다양한 유효성 검증 방법 활용하기

Apache Commons Collections는 다양한 유효성 검증 메서드를 제공합니다. 예를 들어, 숫자가 특정 범위 내에 있는지 검사하거나, 리스트가 특정 길이보다 짧은지 확인할 수 있습니다. `Predicate` 인터페이스를 활용하여 필요한 유효성 검증 메서드를 정의할 수 있습니다.

```java
import org.apache.commons.collections4.Predicate;
import org.apache.commons.collections4.PredicateUtils;

public class DataValidator {

    public static Predicate<Integer> isPositive() {
        return new Predicate<Integer>() {
            @Override
            public boolean evaluate(Integer number) {
                return number > 0;
            }
        };
    }

    public static Predicate<List<?>> isShorterThan(int length) {
        return new Predicate<List<?>>() {
            @Override
            public boolean evaluate(List<?> list) {
                return list.size() < length;
            }
        };
    }

    public static void main(String[] args) {
        int number = 10;
        if (isPositive().test(number)) {
            System.out.println("숫자는 양수입니다.");
        } else {
            System.out.println("숫자는 양수가 아닙니다.");
        }

        List<String> list = Arrays.asList("A", "B", "C");
        if (isShorterThan(5).test(list)) {
            System.out.println("리스트의 길이가 5보다 짧습니다.");
        } else {
            System.out.println("리스트의 길이가 5보다 짧지 않습니다.");
        }
    }
}
```

위의 예제에서는 `isPositive()` 메서드를 통해 양수인지 검증하는 `Predicate`를 생성하고, `isShorterThan()` 메서드를 통해 리스트의 길이가 특정 길이보다 짧은지 확인하는 `Predicate`를 생성합니다. 생성된 `Predicate`를 `test()` 메서드에 전달하여 유효성을 검증합니다.

## 결론

Apache Commons Collections를 사용하면 데이터 유효성 검증을 간편하게 수행할 수 있습니다. 다양한 `Predicate` 메서드를 활용하여 필요에 맞는 유효성 검증 로직을 작성할 수 있습니다. 추가적으로 Apache Commons Collections의 공식 문서를 참조하여 더 많은 기능을 탐색해보시기 바랍니다.

## 참고 자료

- [Apache Commons Collections](https://commons.apache.org/proper/commons-collections/)
- [Apache Commons Collections - Predicate](https://commons.apache.org/proper/commons-collections/apidocs/org/apache/commons/collections4/Predicate.html)