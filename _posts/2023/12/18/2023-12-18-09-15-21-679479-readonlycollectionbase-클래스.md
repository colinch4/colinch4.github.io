---
layout: post
title: "[c#] ReadOnlyCollectionBase 클래스"
description: " "
date: 2023-12-18
tags: [c#]
comments: true
share: true
---

```c#
public abstract class ReadOnlyCollectionBase : ICollection, IEnumerable
```

`ReadOnlyCollectionBase` 클래스는 `IEnumerable` 및 `ICollection` 인터페이스를 구현하므로 컬렉션을 반복하거나 컬렉션의 크기 및 요소를 확인하는 기능을 제공합니다. 추가적으로, 이 클래스를 상속하여 사용자 정의 읽기 전용 컬렉션을 만들 수 있습니다.

이 클래스의 인스턴스를 만들 때는 상속을 통해 새로운 읽기 전용 컬렉션을 만들고 필요한 메서드를 구현해야 합니다. 일반적으로 `ReadOnlyCollectionBase` 클래스는 구체적인 사용 사례에 따라서 해당 클래스를 직접 사용하기보다는 파생 클래스를 만들어서 사용하는 것이 일반적입니다.

`ReadOnlyCollectionBase` 클래스는 .NET Framework의 이전 버전에서 사용되었으며, .NET Framework 2.0에 도입된 제네릭 클래스 및 컬렉션 라이브러리를 사용하는 것이 권장됩니다. 이에 따라, `ReadOnlyCollectionBase` 클래스는 현재 권장되는 컬렉션 구현 방법이 아니며, 대신에 `ReadOnlyCollection<T>` 또는 `ImmutableList<T>` 등을 사용하는 것이 좋습니다.

참고 문헌:
- https://docs.microsoft.com/en-us/dotnet/api/system.collections.readonlycollectionbase?view=netframework-4.8