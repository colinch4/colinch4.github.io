---
layout: post
title: "[java] Mockito의 ArgumentCaptor를 사용하여 메소드 호출 시 전달된 인자들을 확인하는 방법은?"
description: " "
date: 2023-11-17
tags: [java]
comments: true
share: true
---

```java
import static org.mockito.Mockito.*;

import org.mockito.ArgumentCaptor;

// 테스트 대상 클래스
public class MyClass {
    public void myMethod(int number, String name) {
        // 메소드 내용
    }
}

// 테스트 클래스
public class MyClassTest {

    @Test
    public void testMyMethod() {
        // 객체와 모의 객체 생성
        MyClass myObj = new MyClass();
        MyClass myMockObj = mock(MyClass.class);

        // ArgumentCaptor 생성
        ArgumentCaptor<Integer> numberCaptor = ArgumentCaptor.forClass(Integer.class);
        ArgumentCaptor<String> nameCaptor = ArgumentCaptor.forClass(String.class);

        // 메소드 호출
        myMockObj.myMethod(1, "John");

        // 인자 캡처
        verify(myMockObj).myMethod(numberCaptor.capture(), nameCaptor.capture());

        // 캡처된 인자 값 확인
        int capturedNumber = numberCaptor.getValue();
        String capturedName = nameCaptor.getValue();

        // 값 비교
        assertEquals(1, capturedNumber);
        assertEquals("John", capturedName);
    }
}
```

위의 예제에서 `ArgumentCaptor`를 사용하여 `myMockObj.myMethod` 메소드 호출 시 전달된 `number`와 `name` 인자들을 캡처합니다. 그리고 나서 `getValue()` 메소드를 사용하여 캡처한 인자 값을 가져옵니다. 마지막으로 `assertEquals()` 메소드를 사용하여 캡처한 인자 값을 기대하는 값과 비교합니다.

더 자세한 내용은 Mockito 공식 문서를 참조하시기 바랍니다.

[Mockito 공식 문서](https://javadoc.io/doc/org.mockito/mockito-core/latest/org/mockito/Mockito.html#Captor_annotation)