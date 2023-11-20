---
layout: post
title: "@suppresswarnings(unchecked) 예제"
description: " "
date: 2023-09-25
tags: [java]
comments: true
share: true
---

자바 언어에서 `@SuppressWarnings(unchecked)` 애노테이션은 컴파일러 경고를 억제하여 개발자가 의도적으로 발생시킨 경고를 무시할 수 있게 해줍니다.

```java
import java.util.ArrayList;

public class UncheckedExample {

    public static void main(String[] args) {
        ArrayList<String> list = new ArrayList();
        list.add("Hello");
        list.add("World");
        list.add(20); // 컴파일러 경고 발생

        System.out.println("List: " + list);
    }
}
```

위의 예제에서 우리는 `ArrayList`에 String 값들을 추가하는데 마지막으로 정수형 값을 추가했습니다. 이렇게 하면 컴파일러는 경고를 발생시킬 것입니다. 그러나 우리는 `@SuppressWarnings(unchecked)`를 사용하여 이 경고를 억제할 수 있습니다.

출력 결과는 다음과 같습니다:

```
List: [Hello, World, 20]
```

개발자들은 이 애노테이션을 사용하여 일시적으로 경고를 무시할 수 있지만, 신중하게 사용해야 합니다. 오류가 발생할 가능성이 있는 코드에 이 애노테이션을 사용하면 에러를 발생시킬 수 있으므로 주의해야 합니다.

#Java #예외처리