---
layout: post
title: "[c#] SynchronizedKeyedCollection 클래스"
description: " "
date: 2023-12-18
tags: [c#]
comments: true
share: true
---

`SynchronizedKeyedCollection` 클래스는 .NET 프레임워크의 일부로, 키를 사용하여 항목을 저장하고 관리할 수 있는 **동기화된 컬렉션**을 제공합니다. 이 클래스는 여러 스레드가 안전하게 동시에 접근할 수 있도록 설계되었습니다. 

## 주요 특징

- **동기화**: `SynchronizedKeyedCollection`는 여러 스레드가 안전하게 컬렉션에 접근할 수 있도록 동기화되어 있습니다. 이를 통해 다중 스레드 환경에서의 안정성을 보장할 수 있습니다.

- **키 기반 저장**: 해당 클래스는 컬렉션에 키를 지정하여 항목을 저장하고 관리할 수 있도록 지원합니다. 이를 통해 효율적인 검색 및 업데이트 작업을 수행할 수 있습니다.

- **가변 컬렉션**: `SynchronizedKeyedCollection`는 컬렉션의 크기를 동적으로 조절할 수 있는 가변 컬렉션입니다. 새로운 항목을 추가하거나 기존 항목을 제거할 수 있습니다.

## 사용 예시

다음은 `SynchronizedKeyedCollection` 클래스의 간단한 사용 예시입니다.

```csharp
using System.Collections.Generic;
using System.Collections.ObjectModel;

public class Person
{
    public int Id { get; set; }
    public string Name { get; set; }
}

public class PeopleCollection : SynchronizedKeyedCollection<int, Person>
{
    protected override int GetKeyForItem(Person item)
    {
        return item.Id;
    }
}
```

위의 예시에서 `PeopleCollection` 클래스는 `SynchronizedKeyedCollection`을 상속받아 컬렉션을 만들고 있습니다. `GetKeyForItem` 메서드를 재정의하여 각 항목의 키를 반환하도록 설정합니다.

## 참고 자료

MSDN 문서: [SynchronizedKeyedCollection Class](https://docs.microsoft.com/en-us/dotnet/api/system.collections.generic.synchronizedkeyedcollection-2?view=netframework-4.8)

이러한 클래스는 다중 스레드 환경에서 효율적으로 작업할 수 있도록 도와주며, 키를 이용한 검색 및 업데이트 작업 등을 쉽게 수행할 수 있게 해줍니다.