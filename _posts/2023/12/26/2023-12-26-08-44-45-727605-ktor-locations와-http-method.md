---
layout: post
title: "[kotlin] Ktor Locations와 HTTP Method"
description: " "
date: 2023-12-26
tags: [kotlin]
comments: true
share: true
---

Ktor는 **Locations**를 사용하여 HTTP 메소드를 처리하는 강력한 기능을 제공합니다. 이 기능을 통해 URL 경로와 매개변수를 쉽게 처리하여 서버에서 요청을 라우팅할 수 있습니다.

## Locations 설정

먼저, `Locations`를 설정해야 합니다. 아래와 같이 `Locations`를 정의할 수 있습니다:

```kotlin
import io.ktor.locations.*
import io.ktor.application.*
import io.ktor.response.*
import io.ktor.routing.*

@Location("/users")
class Users

@Location("/users/{userId}")
data class User(val userId: Int)
```

위의 예제에서 `Users`와 `User`는 각각 `/users`와 `/users/{userId}`를 나타냅니다. 

## HTTP Method와 Locations

HTTP 메소드를 사용하여 `Locations`를 처리할 수 있습니다. 아래와 같이 `post`, `get`, `delete`, `put` 등의 메소드를 사용할 수 있습니다:

```kotlin
install(Locations)
...

routing {
    post<Users> {
        // 새 사용자 생성
    }
    get<Users> {
        // 모든 사용자 조회
    }
    delete<User> {
        // 특정 사용자 삭제
    }
    put<User> {
        // 특정 사용자 수정
    }
}
```

위의 예제에서 `/users`와 `/users/{userId}`의 `post`, `get`, `delete`, `put` 메소드에 대응하는 블록을 작성할 수 있습니다.

Ktor를 사용하여 위치와 HTTP 메소드를 처리하는 방법을 통해 강력한 RESTful API를 구축할 수 있습니다. 

더 많은 정보는 공식 Ktor 문서를 참고하세요.

[공식 Ktor 문서](https://ktor.io/docs/locations.html)