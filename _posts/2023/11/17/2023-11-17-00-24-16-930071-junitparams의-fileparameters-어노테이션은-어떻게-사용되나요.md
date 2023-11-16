---
layout: post
title: "[java] JUnitParams의 @FileParameters 어노테이션은 어떻게 사용되나요?"
description: " "
date: 2023-11-17
tags: [java]
comments: true
share: true
---

@FileParameters 어노테이션을 사용하기 위해서는 다음과 같은 단계를 따라야 합니다.

1. 테스트 메소드 위에 @RunWith(JUnitParamsRunner.class) 어노테이션을 추가하여 JUnitParamsRunner를 사용한다고 선언합니다.

2. 테스트 메소드 위에 @FileParameters 어노테이션을 추가합니다. 이 어노테이션은 다음과 같은 매개 변수를 가집니다:
   - name: 테스트 메소드의 이름을 지정합니다. (기본값은 메소드의 이름과 동일합니다)
   - file: 테스트 데이터를 포함하는 파일의 경로를 지정합니다. 파일은 CSV 형식이어야 합니다.
   - mapper: 테스트 데이터를 Java 객체로 변환하는 데 사용될 매퍼 클래스를 지정합니다. (기본값은 CsvWithHeaderMapper.class 입니다)
   - numLinesToSkip: 파일에서 건너뛸 행의 수를 지정합니다. (기본값은 1입니다)

3. 테스트 메소드의 인수로 테스트 데이터를 나타내는 자바 객체를 선언합니다. 이 자바 객체는 @FileParameters 어노테이션에서 지정한 매퍼 클래스에 따라 파일의 한 행에 대응되는 필드를 가져야 합니다.

아래는 @FileParameters 어노테이션을 사용한 예제 코드입니다.

```java
import junitparams.FileParameters;
import junitparams.JUnitParamsRunner;
import org.junit.runner.RunWith;

@RunWith(JUnitParamsRunner.class)
public class ExampleTest {

    @Test
    @FileParameters(file = "testdata.csv")
    public void testMethod(int number, String name) {
        // 테스트 로직 작성
        System.out.println("Number: " + number);
        System.out.println("Name: " + name);
    }
}
```

위의 코드에서는 "testdata.csv" 파일에서 테스트 데이터를 읽어와서 testMethod 메소드를 매개 변수화된 테스트로 실행합니다. CSV 파일은 첫 번째 행에 헤더가 있고, 각 행은 number와 name 필드를 가지고 있어야 합니다.

참고 자료:
- JUnitParams 라이브러리 - https://github.com/Pragmatists/JUnitParams
- JUnitParams 문서 - https://github.com/Pragmatists/JUnitParams/wiki