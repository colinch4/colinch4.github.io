---
layout: post
title: "[c#] C#과 데이터베이스 연동을 위한 ORM(Object-relational mapping) 사용 방법"
description: " "
date: 2023-12-18
tags: [c#]
comments: true
share: true
---

C# 언어를 사용하여 데이터베이스와 연동하기 위해 ORM(Object-relational mapping) 프레임워크를 사용하는 것은 일반적인 방법입니다. ORM은 데이터베이스 테이블을 객체로 매핑하여 데이터베이스와의 상호 작용을 추상화하는 도구입니다. 이를 통해 개발자는 데이터베이스 쿼리 및 연결 관리를 간소화하고, 객체 지향적인 접근 방식을 유지할 수 있습니다.

## Entity Framework를 통한 ORM 사용

C#에서 가장 일반적으로 사용되는 ORM 프레임워크 중 하나는 Entity Framework입니다. Entity Framework를 사용하면 C# 객체와 데이터베이스 테이블 간의 매핑이 자동으로 이루어집니다.

Entity Framework를 사용하기 위해서는 먼저 NuGet을 통해 Entity Framework 패키지를 설치해야 합니다.

```csharp
Install-Package EntityFramework
```

그런 다음, 데이터베이스에 연결하여 모델을 만들고 쿼리를 실행하거나 데이터를 저장할 수 있습니다. Entity Framework는 LINQ(Language Integrated Query)을 활용하여 강력한 데이터베이스 쿼리 기능을 제공합니다.

```csharp
using (var context = new MyDbContext())
{
    var products = context.Products
                        .Where(p => p.Category == "Electronics")
                        .ToList();
}
```

위의 코드에서 `MyDbContext`는 데이터베이스와의 연결을 나타내는 클래스이며, `Products`는 데이터베이스 테이블과 매핑된 C# 객체입니다. LINQ을 사용하여 `Products` 테이블에서 필터링된 데이터를 가져오는 예제입니다.

Entity Framework를 사용하면 데이터베이스 스키마의 변경 사항을 C# 코드에 반영할 수 있고, 편리한 데이터베이스 마이그레이션 기능을 제공하여 데이터베이스 업데이트를 관리할 수 있습니다.

## Dapper를 통한 ORM 사용

또 다른 인기 있는 ORM 도구로는 Dapper가 있습니다. Entity Framework와는 달리 Dapper는 간단하면서도 빠른 데이터베이스 액세스를 위한 마이크로 ORM이라고 볼 수 있습니다.

Dapper를 사용하려면 먼저 NuGet을 통해 Dapper 패키지를 설치해야 합니다.

```csharp
Install-Package Dapper
```

Dapper를 통해 데이터베이스 쿼리를 실행하려면 SQL 쿼리를 직접 작성하고, 그 결과를 C# 객체에 매핑해야 합니다. 다음은 Dapper를 사용하여 데이터베이스에서 데이터를 가져오는 예제입니다.

```csharp
using (var connection = new SqlConnection("connectionString"))
{
    var products = connection.Query<Product>("SELECT * FROM Products WHERE Category = @Category", new { Category = "Electronics" }).ToList();
}
```

위의 코드에서는 Dapper를 사용하여 데이터베이스에서 `Products` 테이블에서 필터링된 데이터를 가져오는 예제입니다. `connectionString`은 해당하는 데이터베이스에 대한 연결 문자열을 나타냅니다.

Dapper는 성능 면에서 우수하며, 복잡한 매핑 및 쿼리 기능을 제공하지 않지만, 빠른 데이터베이스 액세스와 가벼운 ORM 기능을 제공하여 C# 프로젝트에서 많은 사용자들에게 선호되는 선택지입니다.

## 결론

C#과 데이터베이스를 연동하기 위해 ORM을 사용하는 것은 효율적이고 편리한 방법입니다. Entity Framework와 Dapper는 각각의 장단점이 있으므로 프로젝트의 요구 사항과 성능 등을 고려하여 적절한 ORM 프레임워크를 선택해야 합니다.