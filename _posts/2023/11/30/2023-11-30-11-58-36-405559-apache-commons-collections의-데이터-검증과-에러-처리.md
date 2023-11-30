---
layout: post
title: "[java] Apache Commons Collections의 데이터 검증과 에러 처리"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

Apache Commons Collections는 Java 개발자들이 자주 사용하는 라이브러리 중 하나입니다. 이 라이브러리는 다양한 유형의 데이터 구조와 컬렉션에 대한 유틸리티 클래스를 제공하여 개발 작업을 보다 쉽게 만들어 줍니다.

하지만, 데이터 검증과 에러 처리는 프로그래밍 작업에서 중요한 부분입니다. 이번 포스트에서는 Apache Commons Collections를 사용하여 데이터 검증과 에러 처리를 어떻게 할 수 있는지 살펴보겠습니다.

## 1. 객체 유효성 검증

일반적으로 프로그래밍 작업에서는 입력된 데이터의 유효성을 검증해야 합니다. Apache Commons Collections에는 `Validation` 클래스가 있어 객체의 유효성을 검증할 수 있습니다.

아래는 `Validation` 클래스를 사용하여 객체의 유효성을 검증하는 예시 코드입니다.

```java
import org.apache.commons.collections4.Validation;
import org.apache.commons.collections4.functors.PredicateValidator;

public class Main {
    public static void main(String[] args) {
        String username = "testUser";
        Validation<String> usernameValidator = PredicateValidator.notEmpty();

        ValidationResult validationResult = usernameValidator.validate(username);
        boolean isValid = validationResult.isValid();
        String errorMessage = validationResult.getErrorMessage();

        if (isValid) {
            System.out.println("입력된 사용자 이름은 유효합니다.");
        } else {
            System.out.println("입력된 사용자 이름이 유효하지 않습니다. 에러 메시지: " + errorMessage);
        }
    }
}
```

위의 코드에서는 먼저 `PredicateValidator.notEmpty()`를 사용하여 빈 문자열이 아닌지 검증할 `Validation` 객체를 생성합니다. 그리고 `validate()` 메소드를 사용하여 입력된 사용자 이름이 유효한지 검사합니다. `ValidationResult` 객체에서 유효성 검사 결과와 에러 메시지를 가져올 수 있습니다.

## 2. 컬렉션 유효성 검증

데이터가 담긴 컬렉션의 유효성도 검증해야 할 때가 있습니다. Apache Commons Collections에서는 `CollectionUtils` 클래스를 사용하여 컬렉션의 유효성을 검사할 수 있습니다.

아래는 `CollectionUtils` 클래스를 사용하여 컬렉션의 유효성을 검증하는 예시 코드입니다.

```java
import org.apache.commons.collections4.CollectionUtils;

import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<String> names = new ArrayList<>();
        names.add("Alice");
        names.add("");
        names.add("Bob");

        boolean isValid = CollectionUtils.isNotEmpty(names);

        if (isValid) {
            System.out.println("입력된 이름들은 유효합니다.");
        } else {
            System.out.println("입력된 이름들이 유효하지 않습니다.");
        }
    }
}
```

위의 코드에서는 `CollectionUtils.isNotEmpty()` 메소드를 사용하여 컬렉션이 비어있지 않은지 검사합니다. `isNotEmpty()` 메소드는 컬렉션이 `null`이 아니고 비어있지 않은 경우에 `true`를 반환합니다.

## 3. 에러 처리

Apache Commons Collections는 예외 처리를 위한 유틸리티 클래스들도 제공합니다. 예를 들어, `FunctorException`은 `Functor` 객체 내에서 발생한 예외를 처리하기 위한 클래스입니다.

아래는 `FunctorException`를 처리하는 예시 코드입니다.

```java
import org.apache.commons.collections4.FunctorException;
import org.apache.commons.collections4.functors.ExceptionTransformer;
import org.apache.commons.collections4.functors.TransformedPredicate;

public class Main {
    public static void main(String[] args) {
        try {
            TransformedPredicate<Integer> predicate = new TransformedPredicate<>(
                    integer -> {
                        if (integer == null) {
                            throw new IllegalArgumentException("숫자는 null일 수 없습니다.");
                        }
                        return integer < 10;
                    },
                    ExceptionTransformer.getInstance(IllegalArgumentException.class)
            );

            boolean result = predicate.evaluate(null);
        } catch (FunctorException e) {
            System.out.println("에러 발생: " + e.getMessage());
        }
    }
}
```

위의 코드에서는 `TransformedPredicate` 객체를 사용하여 숫자가 `null`이 아니고 10보다 작은지 검증합니다. 만약 숫자가 `null`이거나 10보다 크다면 `IllegalArgumentException`이 발생합니다. `ExceptionTransformer.getInstance()` 메소드를 사용하여 예외 클래스를 지정할 수 있습니다.

위의 예시 코드에서는 `null`을 입력하여 예외가 발생하도록 하였으므로, `FunctorException`이 발생하고 해당 에러를 처리하는 부분에서 에러 메시지가 출력됩니다.

## 결론

Apache Commons Collections는 데이터 검증과 에러 처리를 위한 다양한 유틸리티 클래스들을 제공하여 개발자들이 효율적으로 작업할 수 있도록 도와줍니다. 이번 포스트에서는 Apache Commons Collections를 사용하여 객체와 컬렉션의 유효성을 검증하고, 예외를 처리하는 방법을 알아보았습니다.

더 자세한 내용은 [Apache Commons Collections 공식 문서](https://commons.apache.org/proper/commons-collections/)를 참조하시기 바랍니다.