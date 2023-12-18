---
layout: post
title: "[c#] SynchronizedReadOnlyCollection 클래스"
description: " "
date: 2023-12-18
tags: [c#]
comments: true
share: true
---

`SynchronizedReadOnlyCollection` 클래스는 .NET Framework에서 제공하는 동기화된 읽기 전용 컬렉션입니다. 이 클래스는 여러 스레드가 동시에 해당 컬렉션에 안전하게 액세스할 수 있도록 지원합니다.

## 기능

`SynchronizedReadOnlyCollection` 클래스는 다음과 같은 기능을 제공합니다:

- **읽기 전용 기능**: 컬렉션을 읽기 전용으로 만들어서 수정을 방지합니다.
- **동기화**: 여러 스레드 간에 안전하게 액세스할 수 있도록 동기화를 제공합니다.
- **캐스팅 지원**: 원본 컬렉션의 데이터를 형식에 따라 캐스팅하여 액세스할 수 있습니다.
- **이벤트 처리**: 컬렉션의 변경 사항에 대한 이벤트 처리를 제공합니다.

## 사용 예시

```csharp
// 원본 컬렉션 생성
List<int> originalList = new List<int> { 1, 2, 3, 4, 5 };

// 동기화된 읽기 전용 컬렉션 생성
SynchronizedReadOnlyCollection<int> synchronizedCollection = new SynchronizedReadOnlyCollection<int>(originalList);

// 컬렉션 읽기
foreach (int item in synchronizedCollection)
{
    Console.WriteLine(item);
}
```

## 참고 자료

- Microsoft 공식 문서: [SynchronizedReadOnlyCollection 클래스](https://docs.microsoft.com/en-us/dotnet/api/system.collections.generic.synchronizedreadonlycollection-1)

`SynchronizedReadOnlyCollection` 클래스는 다중 스레드 환경에서 안전하게 컬렉션을 읽을 수 있는 유용한 도구입니다. 이를 활용하여 프로그램의 성능과 안정성을 향상시킬 수 있습니다.