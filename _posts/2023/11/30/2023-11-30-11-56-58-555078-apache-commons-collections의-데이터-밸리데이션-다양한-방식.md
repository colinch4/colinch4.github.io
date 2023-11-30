---
layout: post
title: "[java] Apache Commons Collections의 데이터 밸리데이션 다양한 방식"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

Apache Commons Collections는 Java 개발자들에게 유용한 다양한 유틸리티 클래스와 메서드를 제공합니다. 이 중에서 데이터 밸리데이션에 관련된 기능을 사용할 수 있는 몇 가지 방법을 살펴보겠습니다.

## 1. Validator 인터페이스

Apache Commons Collections는 `Validator` 인터페이스를 제공하여 데이터의 유효성을 검증할 수 있습니다. 이 인터페이스를 구현하고 `validate` 메서드를 오버라이드하여 원하는 밸리데이션 로직을 구현할 수 있습니다.

```java
import org.apache.commons.collections4.Predicate;
import org.apache.commons.collections4.PredicateUtils;

public class AgeValidator implements Predicate<Integer> {
    @Override
    public boolean evaluate(Integer age) {
        return age >= 18;
    }
}

public class Main {
    public static void main(String[] args) {
        AgeValidator ageValidator = new AgeValidator();
        
        System.out.println(ageValidator.evaluate(20)); // true
        System.out.println(ageValidator.evaluate(15)); // false
    }
}
```

## 2. PredicateUtils 클래스

`PredicateUtils` 클래스는 몇 가지 유용한 밸리데이션 메서드를 제공합니다. 예를 들어, `and`, `or`, `not` 메서드를 활용하여 다양한 밸리데이션 조합을 만들 수 있습니다.

```java
import org.apache.commons.collections4.Predicate;
import org.apache.commons.collections4.PredicateUtils;

public class Main {
    public static void main(String[] args) {
        Predicate<Integer> ageValidator = PredicateUtils.and(
            new AgeValidator(),
            value -> value % 2 == 0
        );
        
        System.out.println(ageValidator.evaluate(20)); // true
        System.out.println(ageValidator.evaluate(15)); // false
        System.out.println(ageValidator.evaluate(22)); // false (AgeValidator는 true, value % 2 == 0은 false)
    }
}
```

## 3. ValidationUtils 클래스

`ValidationUtils` 클래스는 데이터의 유효성을 검증하는 데 도움이 되는 여러 유틸리티 메서드를 제공합니다. 예를 들어, `allPass` 메서드는 주어진 조건들이 모두 true일 때 true를 반환합니다.

```java
import org.apache.commons.collections4.ValidationUtils;

public class Main {
    public static void main(String[] args) {
        boolean isValid = ValidationUtils.allPass(
            new AgeValidator(),
            value -> value % 2 == 0
        ).validate(20);
        
        System.out.println(isValid); // true
    }
}
```

위의 예제에서는 `allPass` 메서드를 통해 두 개의 밸리데이션 조건을 모두 만족하면 true를 반환하도록 설정하고 있습니다.

## 4. 설정 파일 사용

Apache Commons Collections는 밸리데이션 설정을 파일로부터 읽어들일 수 있는 기능을 제공합니다. XML 또는 프로퍼티 파일 형식을 사용하여 밸리데이션 로직을 설정할 수 있습니다.

```xml
<validators>
    <validator name="ageValidator" class="com.example.AgeValidator"/>
    <validator name="evenNumberValidator" class="org.apache.commons.collections4.functors.PredicateUtils">
        <factory method="and">
            <constant>
                <validator ref="ageValidator"/>
            </constant>
            <constant>
                <dyn:script realClass="com.example.PredicateUtils" method="isEvenNumber"/>
            </constant>
        </factory>
    </validator>
</validators>
```

위의 XML 파일은 `ageValidator`와 `evenNumberValidator` 두 개의 밸리데이터를 설정하는 예시입니다. 자세한 설정 방법은 Apache Commons Collections의 공식 문서를 참고하시기 바랍니다.

## 결론

Apache Commons Collections를 사용하면 데이터의 밸리데이션을 간편하게 구현할 수 있습니다. `Validator` 인터페이스를 사용하거나 `PredicateUtils`, `ValidationUtils` 클래스를 활용하여 원하는 밸리데이션 로직을 구현해보세요.

## 참고 자료

- [Apache Commons Collections 문서](https://commons.apache.org/proper/commons-collections/)