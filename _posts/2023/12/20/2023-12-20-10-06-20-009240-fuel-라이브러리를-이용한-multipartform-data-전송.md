---
layout: post
title: "[kotlin] Fuel 라이브러리를 이용한 multipart/form-data 전송"
description: " "
date: 2023-12-20
tags: [kotlin]
comments: true
share: true
---

이 포스트에서는 Kotlin의 Fuel 라이브러리를 사용하여 multipart/form-data 형식으로 데이터를 전송하는 방법에 대해 알아보겠습니다.

## Fuel 라이브러리란?

Fuel은 Kotlin으로 작성된 HTTP 클라이언트 라이브러리로, HTTP 요청을 쉽게 생성하고 실행할 수 있도록 도와줍니다. Fuel을 사용하면 POST 및 multipart/form-data 요청과 같은 다양한 HTTP 요청을 만들고 전송할 수 있습니다.

## multipart/form-data 요청 만들기

multipart/form-data를 사용하여 데이터를 전송하려면 `Fuel` 객체를 사용하여 요청을 만들어야 합니다. 다음은 간단한 multipart/form-data 요청 예제입니다.

```kotlin
import com.github.kittinunf.fuel.httpPost
import com.github.kittinunf.fuel.Fuel

fun main() {
    val url = "http://example.com/upload"
    val fileBytes = File("file.jpg").readBytes()
    
    val parameters = listOf("key1" to "value1", "key2" to "value2")

    url.httpPost()
        .header("Content-Type" to "multipart/form-data")
        .body(
            MultipartForm(Multipart("file", "file.jpg", "image/jpeg", fileBytes),
                          *parameters.map { Multipart(it.first, it.second) }.toTypedArray())
        )
        .response { /* 처리 */ }
}
```

위의 코드에서 `httpPost()` 함수는 POST 요청을 생성하고, `MultipartForm` 객체를 사용하여 멀티파트 폼 데이터를 구성합니다. 파일과 추가 파라미터들을 적절히 전송할 수 있습니다.

## 요청 실행 및 응답 처리

요청을 만들었으면 `.response` 함수를 사용하여 응답을 처리할 수 있습니다. 응답은 여러 유형일 수 있으며, 다운로드 파일, JSON 응답 등 원하는 형식으로 처리할 수 있습니다.

위에서 작성한 코드에서 `.response` 함수에 실제 응답을 처리하는 코드를 추가해야 합니다.

## 마치며

이렇게 Kotlin의 Fuel 라이브러리를 사용하여 multipart/form-data 형식으로 데이터를 전송하는 방법에 대해 알아보았습니다. Fuel을 사용하면 HTTP 요청을 간편하게 만들고 실행할 수 있으며, multipart/form-data를 사용하여 파일과 추가 데이터를 요청하는 것도 매우 간단합니다.