---
layout: post
title: "@suppresswarnings( unchecked ) 예제"
description: " "
date: 2023-09-25
tags: [Java, Generics]
comments: true
share: true
---
@SuppressWarnings("unchecked")
public class Example {
    public static void main(String[] args) {
        List<String> stringList = new ArrayList();
        stringList.add("Hello");
        stringList.add("World");
        
        for (String str : stringList) {
            System.out.println(str);
        }
    }
}
```

- 이 예제는 `@SuppressWarnings("unchecked")` 어노테이션을 사용하여 경고를 무시하는 방법을 보여줍니다.
- `stringList`라는 `ArrayList`에 `String` 요소를 추가하고, `for-each`문을 사용하여 각 요소를 출력합니다.
- 경고를 무시하여, `ArrayList`에 제네릭을 지정하지 않아도 컴파일러 오류를 피할 수 있습니다.
- 이러한 방법은 항상 주의해서 사용해야 하며, 제네릭이 정확하게 지정되지 않아서 컴파일러가 타입 안정성을 보장할 수 없을 수도 있습니다.
- 따라서 이런 경고를 무시하는 경우에는 해당 코드가 안전하다는 확신이 있을 때에만 사용해야 합니다.

#Java #Generics #SuppressWarnings