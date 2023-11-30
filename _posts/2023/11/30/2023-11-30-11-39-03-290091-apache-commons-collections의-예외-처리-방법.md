---
layout: post
title: "[java] Apache Commons Collections의 예외 처리 방법"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

Apache Commons Collections는 다양한 유용한 자료구조와 알고리즘을 제공하는 자바 라이브러리입니다. 하지만 사용 중에 예외가 발생할 수 있으며, 이러한 예외를 효과적으로 처리하는 방법을 알아보겠습니다.

## 1. 예외 처리 기본 사항

Apache Commons Collections를 사용하는 경우, 다음과 같은 기본적인 예외 처리 사항을 고려해야 합니다.

- 적절한 예외 클래스 선택: 예외의 성격에 따라서 `IllegalArgumentException`, `UnsupportedOperationException`, `ConcurrentModificationException` 등을 사용할 수 있습니다.
- 예외 메시지 처리: 예외 메시지에는 발생한 이유와 발생한 위치 정보 등이 포함되어야 합니다.
- 예외 처리 방법 선택: `try-catch` 블록을 사용하여 예외를 처리할 수 있습니다.
- 예외 전파: 예외가 발생한 경우, 적절한 위치에서 예외를 처리하거나 호출자에게 전파해야 합니다.

## 2. 예외 처리 예제

아래는 Apache Commons Collections의 `ListUtils` 클래스를 사용하여 두 개의 리스트를 병합하는 예제입니다. 예외 처리를 위해 `try-catch` 블록을 사용하고, 예외 메시지를 출력하는 방법도 포함되어 있습니다.

```java
import org.apache.commons.collections4.ListUtils;

public class ListMergeExample {
    public static void main(String[] args) {
        try {
            List<String> list1 = Arrays.asList("A", "B", "C");
            List<String> list2 = Arrays.asList("X", "Y", "Z");

            List<String> mergedList = ListUtils.union(list1, list2);

            System.out.println("Merged list: " + mergedList);
        } catch (IllegalArgumentException ex) {
            System.err.println("Invalid argument: " + ex.getMessage());
        }
    }
}
```

위의 예제 코드에서는 `ListUtils.union()` 메소드를 사용하여 두 개의 리스트를 병합하고 있습니다. 그리고 `try-catch` 블록을 사용하여 `IllegalArgumentException` 예외를 처리하고 있습니다. 발생한 예외의 메시지는 `System.err.println()`을 사용하여 출력하고 있습니다.

## 3. 예외 처리 추가 고려 사항

Apache Commons Collections를 사용하는 동안 예외 처리에 대한 추가적인 고려 사항은 다음과 같습니다.

- Null 값 처리: 널 값이 아닌 인자를 전달해야 하는 경우, 예외를 발생시킬 필요가 있습니다.
- 읽기 전용 컬렉션 사용 시 주의: 읽기 전용 컬렉션을 수정하려고 시도할 때, `UnsupportedOperationException` 예외가 발생할 수 있습니다.
- 동시 수정 예외 처리: 동시에 컬렉션을 수정하려고 할 때, `ConcurrentModificationException` 예외가 발생할 수 있습니다. 이런 경우 수정 작업을 동기화하여 예외를 방지할 수 있습니다.

## 결론

Apache Commons Collections의 예외 처리는 안정적인 코드를 작성하기 위해 꼭 고려해야 할 사항입니다. 적절한 예외 클래스 선택, 예외 메시지 처리, `try-catch` 블록 사용, 예외 전파 등을 고려하여 예외 상황을 처리하는 것이 중요합니다. 이러한 예외 처리 기본 사항을 숙지하고 추가적인 고려 사항에 대비하면 더욱 안전하고 효율적인 코드를 작성할 수 있습니다.

## 참고 자료

- [Apache Commons Collections Documentation](https://commons.apache.org/proper/commons-collections/documentation.html)
- [Java SE 8 API 문서 - 예외 처리](https://docs.oracle.com/javase/8/docs/api/java/lang/Exception.html)