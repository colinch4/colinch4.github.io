---
layout: post
title: "[android] 안드로이드 - MediaStore"
description: " "
date: 2021-06-04
tags: [android]
comments: true
share: true
---

# 안드로이드 - MediaStore



Media Provider와 MediaStore 정의



Media provider : 단말에 저장된 이미지,동영상,오디오 파일의 정보를 제공하는 프로바이더. 이 프로바이더에게 우리가 찾고 싶은 정보를 쿼리 할 수 있다. 파일 이름,저장된시간,저장된 위치등을 리턴값으로 가진다.

MediaStore : 앱이 Media provider가 제공하는 파일들을 접근 할 수 있도록 도와주는 API 묶음 쿼리에 필요한 데이터가 정의되어 있다.



*Android 10(Q)에서* [Scoped Storage](https://codechacha.com/ko/android-q-scoped-storage/)*가 적용되었습니다. 미디어 파일들은 MediaStore를 통해 read/write하도록 권장하고 있습니다.*

```kotlin
val projection = arrayOf(
    MediaStore.Images.Media._ID,
    MediaStore.Images.Media.DISPLAY_NAME,
    MediaStore.Images.Media.DATE_TAKEN
)
val selection = "${MediaStore.Images.Media.DATE_TAKEN} >= ?"
val selectionArgs = arrayOf(
    dateToTimestamp(day = 1, month = 1, year = 1970).toString()
)
val sortOrder = "${MediaStore.Images.Media.DATE_TAKEN} DESC"

val cursor = contentResolver.query(
    MediaStore.Images.Media.EXTERNAL_CONTENT_URI,
    projection,
    selection,
    selectionArgs,
    sortOrder
)

private fun dateToTimestamp(day: Int, month: Int, year: Int): Long =
    SimpleDateFormat("dd.MM.yyyy").let { formatter ->
        formatter.parse("$day.$month.$year")?.time ?: 0
    }
```



```kotlin
val cursor = contentResolver.query(
    MediaStore.Images.Media.EXTERNAL_CONTENT_URI,
    projection,
    selection,
    selectionArgs,
    sortOrder
)
```

- Uri : 찾고자 하는 데이터의 uri
- Projection : DB의 column과 같음. 결과로 받고 싶은 데이터의 종류를 알려줍니다.
- Selection : DB의 Where 키워드와 같다. 어떤 조건으로 필터링 된 결과를 받을 때 사용
- Selection args : Selection과 함께 사용
- Sort order : 쿼리 결과 데이터를 sorting할 때 사용합니다.

### Uri

Uri(Uniform Resource Identifier)는 데이터의 위치를 표현합니다.

`query()` API는 인자로 전달되는 Uri 내에서 데이터를 찾습니다.

MediaStore.Images.Media.EXTERNAL_CONTENT_URI 라는 Uri를 인자로 전달하였다면 이 Uri 경로 아래에서만 파일을 찾습니다. 이 Uri를 String으로 출력해보면 다음과 같습니다.

- content://media/external/images/media

이 패스와 이미지 쿼리 결과에서 출력된 파일의 Uri 패스를 비교해보시면 공통 패스가 있다는 것을 알 수 있습니다.

### Projection

Projection은 `String[]`을 인자로 받습니다. 결과로 받고 싶은 column 명을 배열에 입력하면 됩니다.

다음과 같은 column 들이 있습니다.

- MediaStore.Images.Media._ID
- MediaStore.Images.Media.DATA
- MediaStore.Images.Media.DISPLAY_NAME
- MediaStore.Images.Media.TITLE
- MediaStore.Images.Media.DATE_TAKEN
- MediaStore.Images.Media.DATE_ADDED



### Selection, Selection args

Selection은 DB의 where와 같습니다. 다음 코드는 날짜를 기준으로 어떤 조건을 충족시키면 결과에 포함시킵니다.

```kotlin
val selection = "${MediaStore.Images.Media.DATE_TAKEN} >= ?"
```

만약 모든 데이터를 쿼리하고 싶다면 selection과 args에 null을 입력하시면 됩니다.

```kotlin
val cursor = contentResolver.query(
    MediaStore.Images.Media.EXTERNAL_CONTENT_URI,
    projection,
    null,  // selection
    null,  // selectionArgs
    sortOrder
)
```

