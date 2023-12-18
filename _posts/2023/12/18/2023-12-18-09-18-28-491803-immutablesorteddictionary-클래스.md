---
layout: post
title: "[c#] ImmutableSortedDictionary 클래스"
description: " "
date: 2023-12-18
tags: [c#]
comments: true
share: true
---

`ImmutableSortedDictionary` 클래스는 .NET에서 제공하는 `System.Collections.Immutable` 네임스페이스에 있는 불변의 정렬된 키-값 쌍 컬렉션을 나타냅니다. 이 클래스는 수정될 수 없는 (불변의) 딕셔너리를 효율적으로 처리할 수 있도록 고안되었습니다. 

이 클래스는 변경 불가능한 딕셔너리인데도 불구하고, 새로운 키-값 쌍을 추가하거나 기존의 값을 업데이트하는데 사용할 수 있는 메서드를 제공합니다. 그러나 이러한 작업을 수행할 때마다 새로운 `ImmutableSortedDictionary` 인스턴스를 반환하므로 원래의 딕셔너리를 변경하지 않는 불변 속성을 유지합니다.

```csharp
ImmutableSortedDictionary<string, int> original = ImmutableSortedDictionary<string, int>.Empty;
ImmutableSortedDictionary<string, int> updated = original.Add("key1", 1).Add("key2", 2);
int value = updated["key2"]; // 2
```

이 클래스는 메모리 점유와 성능상의 이점을 제공하며, 스레드로부터 안전하며 병행성 처리에 적합합니다. 따라서 여러 스레드에서 동시에 접근하여 수정하는 경우에도 안전하게 사용할 수 있습니다.

덧붙여서, `ImmutableSortedDictionary` 클래스는 LINQ 메서드와 함께 사용할 수 있어서 LINQ 쿼리와 함께 수정 불가능한 정렬된 딕셔너리를 효과적으로 조작할 수 있습니다.

`ImmutableSortedDictionary` 클래스는 .NET 런타임과 함께 제공되며, `System.Collections.Immutable` 네임스페이스를 사용하여 해당 기능을 활용할 수 있습니다.

참고 문헌: 
- https://docs.microsoft.com/en-us/dotnet/api/system.collections.immutable.immutablesorteddictionary-2?view=net-6.0