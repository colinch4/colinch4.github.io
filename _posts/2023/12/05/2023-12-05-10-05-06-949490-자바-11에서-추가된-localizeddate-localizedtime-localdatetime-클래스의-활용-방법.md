---
layout: post
title: "[java] 자바 11에서 추가된 LocalizedDate, LocalizedTime, LocalDateTime 클래스의 활용 방법"
description: " "
date: 2023-12-05
tags: [java]
comments: true
share: true
---

자바 11에서 소개된 `java.time` 패키지는 시간과 날짜를 다루는 데 사용되는 유용한 클래스들을 포함하고 있습니다. 그 중에서도 `LocalizedDate`, `LocalizedTime`, `LocalDateTime` 클래스는 지역화된 날짜와 시간을 표현하는 데 사용됩니다. 이 클래스들을 활용하여 다양한 날짜와 시간 연산을 수행할 수 있습니다.

## 1. LocalizedDate 클래스

`LocalizedDate` 클래스는 지역화된 날짜를 표현하기 위해 사용됩니다. 다음은 `LocalizedDate` 클래스를 사용하여 현재 날짜를 생성하는 예제입니다:

```java
import java.time.LocalizedDate;
import java.time.format.DateTimeFormatter;

public class Example {
    public static void main(String[] args) {
        LocalizedDate currentDate = LocalizedDate.now();
        System.out.println("현재 날짜: " + currentDate);

        // 날짜를 지정된 형식으로 출력
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd");
        String formattedDate = currentDate.format(formatter);
        System.out.println("형식화된 날짜: " + formattedDate);
    }
}
```

위 예제에서는 `LocalizedDate.now()`를 호출하여 현재 날짜를 얻고, `DateTimeFormatter`를 사용하여 특정한 형식의 문자열로 날짜를 포맷합니다.

## 2. LocalizedTime 클래스

`LocalizedTime` 클래스는 지역화된 시간을 표현하기 위해 사용됩니다. 다음은 `LocalizedTime` 클래스를 사용하여 현재 시간을 생성하는 예제입니다:

```java
import java.time.LocalizedTime;
import java.time.format.DateTimeFormatter;

public class Example {
    public static void main(String[] args) {
        LocalizedTime currentTime = LocalizedTime.now();
        System.out.println("현재 시간: " + currentTime);

        // 시간을 지정된 형식으로 출력
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("HH:mm:ss");
        String formattedTime = currentTime.format(formatter);
        System.out.println("형식화된 시간: " + formattedTime);
    }
}
```

위 예제에서는 `LocalizedTime.now()`를 호출하여 현재 시간을 얻고, `DateTimeFormatter`를 사용하여 특정한 형식의 문자열로 시간을 포맷합니다.

## 3. LocalDateTime 클래스

`LocalDateTime` 클래스는 지역화된 날짜와 시간을 표현하기 위해 사용됩니다. 다음은 `LocalDateTime` 클래스를 사용하여 현재 날짜와 시간을 생성하는 예제입니다:

```java
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class Example {
    public static void main(String[] args) {
        LocalDateTime currentDateTime = LocalDateTime.now();
        System.out.println("현재 날짜와 시간: " + currentDateTime);

        // 날짜와 시간을 지정된 형식으로 출력
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
        String formattedDateTime = currentDateTime.format(formatter);
        System.out.println("형식화된 날짜와 시간: " + formattedDateTime);
    }
}
```

위 예제에서는 `LocalDateTime.now()`를 호출하여 현재 날짜와 시간을 얻고, `DateTimeFormatter`를 사용하여 특정한 형식의 문자열로 날짜와 시간을 포맷합니다.

---

위에서 소개한 예제들은 Java 11에서 도입된 LocalizedDate, LocalizedTime, LocalDateTime 클래스를 활용하는 방법을 보여줍니다. 이러한 클래스들은 지역화된 날짜와 시간을 표현하고 다양한 연산을 수행하는 데 편리하게 사용할 수 있습니다.

더 자세한 내용은 [Oracle Java SE 11 문서](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/time/package-summary.html)를 참조하세요.