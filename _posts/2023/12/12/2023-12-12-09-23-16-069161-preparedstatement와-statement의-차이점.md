---
layout: post
title: "[java] PreparedStatement와 Statement의 차이점"
description: " "
date: 2023-12-12
tags: [java]
comments: true
share: true
---

Java에서 데이터베이스와 상호작용할 때 `Statement`와 `PreparedStatement`는 두 가지 주요 방법입니다. 이 둘의 차이점에 대해 알아보고 각각의 장단점을 살펴보겠습니다.

## Statement

`Statement` 클래스는 SQL 쿼리를 디비로 보내기 위한 인터페이스를 제공합니다. 이 클래스를 사용하여 쿼리를 실행할 때마다 SQL 쿼리가 디비로 전송되고 실행됩니다. 그러나 이러한 방식은 쿼리를 실행할 때마다 SQL 문을 파싱하고 컴파일해야 하므로 성능이 저하될 수 있습니다.

## PreparedStatement

`PreparedStatement`는 `Statement`와는 달리 미리 컴파일된 SQL 문을 실행할 수 있도록 지원합니다. 또한 `PreparedStatement`를 사용하면 매개변수를 사용하여 쿼리를 실행할 수 있으므로 보다 간단하고 안전한 방법입니다. 또한 동일한 쿼리를 여러 번 실행해야 하는 경우에는 `PreparedStatement`가 효율적입니다.

## 차이점 요약

- `Statement`는 매번 실행될 때마다 SQL이 디비로 전송되고 실행되지만, `PreparedStatement`는 미리 컴파일된 SQL을 디비로 보내므로 성능적으로 이점이 있습니다.
- `PreparedStatement`는 매개변수 사용으로 보안을 강화하고, 코드 가독성을 높입니다.
- 동일한 쿼리를 반복해서 실행해야 할 때는 `PreparedStatement`가 효율적입니다.

따라서, 보안과 성능을 고려할 때 `PreparedStatement`를 사용하는 것이 좋습니다.

참고 문헌:
- [Oracle Java Documentation](https://docs.oracle.com/javase/tutorial/jdbc/basics/prepared.html)