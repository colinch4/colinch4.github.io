---
layout: post
title: "suppresswarnings( unchecked ) 예제"
description: " "
date: 2023-09-25
tags: [java]
comments: true
share: true
---

자바에서 `@SuppressWarnings("unchecked")` 어노테이션은 경고 메시지를 억제하고자 할 때 사용됩니다. 이 어노테이션은 런타임에 언체크된 형변환이 발생하는 지점에서 경고를 무시하도록 컴파일러에게 알려줍니다.

다음은 `@SuppressWarnings("unchecked")` 어노테이션을 사용한 예제 코드입니다.

```java
import java.util.ArrayList;
import java.util.List;

public class UncheckedExample {

    @SuppressWarnings("unchecked")
    public static void main(String[] args) {
        List list = new ArrayList(); // 경고 발생

        list.add("Apple");
        list.add("Orange");
        list.add("Banana");

        for (Object item : list) {
            System.out.println((String) item); // 경고 발생
        }
    }
}
```

위 예제에서는 `List`에 대한 제네릭 타입을 명시하지 않고, `@SuppressWarnings("unchecked")` 어노테이션을 `main` 메소드에 추가하여 경고를 억제하였습니다. 이러한 방식으로, 형변환 경고를 무시하고 프로그램을 실행할 수 있습니다.

반드시 필요한 경우가 아니라면, `@SuppressWarnings` 어노테이션은 지속적으로 사용되어서는 안 됩니다. 경고 메시지가 발생하면, 해당 경고를 해결하고 적절한 타입 안전성을 유지하도록 코드를 수정하는 것이 좋습니다.

즉각적으로 경고를 억제하는 대신, 제네릭을 사용하거나, 형변환을 피하는 등 타입 안정성을 확보하는 더 좋은 코드를 작성하는 것이 중요합니다.

#Java #Unchecked #경고 #어노테이션