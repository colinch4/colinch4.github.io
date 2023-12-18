---
layout: post
title: "[c#] SynchronizedCollection 클래스"
description: " "
date: 2023-12-18
tags: [c#]
comments: true
share: true
---

`SynchronizedCollection` 클래스는 여러 스레드가 동시에 컬렉션에 접근할 때 발생할 수 있는 문제를 해결하기 위해 제공되는 .NET 프레임워크의 클래스입니다. 이 클래스는 멀티 스레드 환경에서 안전하게 컬렉션을 수정하고 업데이트할 수 있도록 지원합니다.

## SynchronizedCollection 클래스의 특징

- **다중 스레드 환경 지원**: `SynchronizedCollection`을 사용하면 여러 스레드에서 컬렉션에 안전하게 접근할 수 있습니다. 동기화 메커니즘이 내부적으로 구현되어 있어, 스레드 간의 충돌이나 경쟁 상태 문제를 방지합니다.

- **원자적 연산**: `SynchronizedCollection`을 통해 수행되는 수정 작업은 원자적 연산으로 보호됩니다. 따라서 여러 스레드가 동시에 컬렉션의 수정 작업을 수행해도, 데이터 불일치나 무효한 상태가 발생하지 않습니다.

- **Thread-Safe한 컬렉션 사용**: `SynchronizedCollection`은 내부적으로 `List<T>`나 `Collection<T>`를 사용하여 컬렉션을 관리하며, 이러한 내부 컬렉션을 스레드 안전하게 래핑하여 제공합니다.

## SynchronizedCollection 클래스 사용 예시

```csharp
using System.Collections.Generic;
using System.Collections.Concurrent;

class Program
{
    static void Main()
    {
        // SynchronizedCollection 인스턴스 생성
        var synchronizedList = new SynchronizedCollection<int>();

        // 여러 스레드에서 동시에 접근하여 수정
        Parallel.For(0, 100, i =>
        {
            synchronizedList.Add(i);
        });

        // SynchronizedCollection을 안전하게 순회
        foreach (var item in synchronizedList)
        {
            Console.WriteLine(item);
        }
    }
}
```

위 예시에서는 `SynchronizedCollection`을 사용하여 여러 스레드에서 안전하게 컬렉션을 수정하고, 안전하게 순회하는 방법을 보여줍니다.

`SynchronizedCollection` 클래스는 멀티 스레드 환경에서 안전하게 컬렉션을 다루는 데 유용한 도구로 활용될 수 있습니다.

## 참고 자료
- [.NET SynchronizedCollection Documentation](https://docs.microsoft.com/en-us/dotnet/api/system.collections.concurrent.synchronizedcollection-1?view=net-6.0)