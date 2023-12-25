---
layout: post
title: "[java] Apache Commons Collections의 데이터 포맷팅"
description: " "
date: 2023-12-26
tags: [java]
comments: true
share: true
---

Apache Commons는 Java 개발을 위한 유용한 라이브러리 모음체이며, 그 중 Collections는 다양한 데이터 구조와 관련된 기능을 제공합니다. 이 라이브러리를 사용하여 데이터의 서식을 효율적으로 변경하는 방법에 대해 알아보겠습니다.

## 1. Maven Dependency 추가

먼저 Apache Commons Collections를 프로젝트에 추가합니다. `pom.xml` 파일에 다음 의존성을 추가합니다.

```xml
<dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-collections4</artifactId>
    <version>4.4</version>
</dependency>
```

## 2. 데이터 포맷팅

Apache Commons Collections의 `Transformer` 인터페이스와 `TransformerUtils` 클래스를 사용하여 데이터를 원하는 형식으로 변환할 수 있습니다.

예를 들어, 날짜 데이터를 포맷하는 변환기를 만들어보겠습니다.

```java
import org.apache.commons.collections4.Transformer;
import org.apache.commons.collections4.TransformerUtils;

import java.text.SimpleDateFormat;
import java.util.Date;

public class DateFormattingExample {
    public static void main(String[] args) {
        Transformer<Date, String> dateFormatter = TransformerUtils.decorate(new DateToStringTransformer(), new SimpleDateFormat("yyyy-MM-dd"));
        
        Date date = new Date();
        String formattedDate = dateFormatter.transform(date);
        
        System.out.println("Formatted Date: " + formattedDate);
    }
    
    private static class DateToStringTransformer implements Transformer<Date, String> {
        @Override
        public String transform(Date input) {
            return input.toString();
        }
    }
}
```

## 3. 결과

위 예제를 실행하면 현재 날짜가 "yyyy-MM-dd"의 형식으로 변환되어 출력됩니다. 이러한 방식으로 Apache Commons Collections를 사용하여 데이터 포맷팅을 수행할 수 있습니다.

## 참고 자료

- [Apache Commons Collections Documentation](https://commons.apache.org/proper/commons-collections/)
- [Apache Commons Collections Maven Repository](https://mvnrepository.com/artifact/org.apache.commons/commons-collections4)