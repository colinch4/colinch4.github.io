---
layout: post
title: "[java] 자바 11에서 추가된 OffsetDateTime의 ofInstant() 메서드 사용하기"
description: " "
date: 2023-12-05
tags: [java]
comments: true
share: true
---

자바 11에서는 java.time 패키지에 새로운 기능과 클래스가 추가되었습니다. 그 중 하나는 `OffsetDateTime` 클래스입니다. `OffsetDateTime` 클래스는 시간과 날짜에 대한 정보뿐만 아니라 시간대 오프셋을 표현하기 위한 정보도 포함하고 있습니다. 이를 통해 우리는 특정 시간대에서의 날짜와 시간을 쉽게 다룰 수 있습니다.

`OffsetDateTime` 클래스는 `ofInstant()` 메서드를 제공합니다. 이 메서드는 `Instant` 객체를 `OffsetDateTime`으로 변환할 때 사용됩니다. `Instant` 객체는 Epoc(1970년 1월 1일 00:00:00 UTC) 이후의 시간을 나노초 단위로 표현한 것입니다.

아래는 `ofInstant()` 메서드를 사용하여 `Instant` 객체를 `OffsetDateTime`으로 변환하는 예제 코드입니다.

```java
import java.time.Instant;
import java.time.OffsetDateTime;
import java.time.ZoneOffset;

public class Example {
    public static void main(String[] args) {
        Instant instant = Instant.now(); // 현재 시간의 Instant 객체 생성
        
        OffsetDateTime offsetDateTime = OffsetDateTime.ofInstant(instant, ZoneOffset.UTC); // Instant를 UTC 시간대로 변환
        
        System.out.println("Instant: " + instant);
        System.out.println("OffsetDateTime: " + offsetDateTime);
    }
}
```

위 예제 코드에서는 `now()` 메서드를 사용하여 현재 시간의 `Instant` 객체를 생성합니다. 그리고 `ofInstant()` 메서드를 사용하여 `instant` 객체를 UTC 시간대로 변환한 후, `offsetDateTime` 변수에 할당합니다. 마지막으로 `System.out.println()`을 사용하여 `instant`와 `offsetDateTime`의 값을 출력합니다.

출력 결과는 다음과 같습니다.

```
Instant: 2021-12-31T12:34:56.789Z
OffsetDateTime: 2021-12-31T12:34:56.789Z
```

위 예제에서는 `OffsetDateTime` 객체를 UTC 시간대로 변환하였지만, `OffsetDateTime` 클래스는 다양한 시간대 오프셋을 지원하므로 원하는 시간대로 변환할 수도 있습니다.

더 자세한 내용은 [Java 11의 OffsetDateTime](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/time/OffsetDateTime.html) 문서를 참조하시기 바랍니다.