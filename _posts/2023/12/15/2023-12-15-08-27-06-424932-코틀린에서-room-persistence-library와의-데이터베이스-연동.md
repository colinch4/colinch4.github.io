---
layout: post
title: "[kotlin] 코틀린에서 Room Persistence Library와의 데이터베이스 연동"
description: " "
date: 2023-12-15
tags: [kotlin]
comments: true
share: true
---

안녕하세요! 이번에는 코틀린에서 Room Persistence Library를 사용하여 데이터베이스를 연동하는 방법에 대해 살펴보겠습니다.

## 1. Room Persistence Library란?

Room Persistence Library는 안드로이드 앱에서 SQLite 데이터베이스를 쉽게 사용할 수 있도록 도와주는 라이브러리입니다. Room은 SQLite의 추상화 계층을 제공하며, 데이터베이스에 대한 접근 및 쿼리 작성을 단순화합니다.

## 2. Room Persistence Library 설정

Room Persistence Library를 사용하기 위해서는 `build.gradle` 파일에 아래 의존성을 추가해야 합니다.

```gradle
implementation "androidx.room:room-runtime:2.3.0"
kapt "androidx.room:room-compiler:2.3.0"
```

그리고 데이터베이스 버전 및 엔터티(테이블)를 정의하기 위해 데이터베이스 클래스와 엔터티 클래스를 작성해야 합니다.

```kotlin
// 데이터베이스 클래스 정의
@Database(entities = [User::class], version = 1)
abstract class AppDatabase : RoomDatabase() {
    abstract fun userDao(): UserDao
}

// 엔터티(테이블) 클래스 정의
@Entity
data class User(
    @PrimaryKey val id: Int,
    val name: String
)
```

## 3. 데이터베이스 연동

Room Persistence Library를 사용하여 데이터베이스를 연동하려면 다음과 같이 데이터베이스 인스턴스를 생성하고 쿼리를 수행할 수 있습니다.

```kotlin
val db = Room.databaseBuilder(
    applicationContext,
    AppDatabase::class.java, "app-database"
).build()

val userDao = db.userDao()
val user = User(1, "John")
userDao.insert(user)
val users = userDao.getAll()
```

위 코드에서 `userDao`는 데이터베이스에 접근하여 쿼리를 수행하기 위한 DAO(Data Access Object)입니다. `insert` 메서드를 사용하여 사용자를 데이터베이스에 추가하고, `getAll` 메서드를 사용하여 모든 사용자를 가져올 수 있습니다.

## 4. 요약

이제 코틀린에서 Room Persistence Library를 사용하여 데이터베이스를 연동하는 방법에 대해 알아보았습니다. Room을 사용하면 SQLite 데이터베이스를 간단하게 다룰 수 있어서 안드로이드 앱의 데이터 관리를 효율적으로 처리할 수 있습니다.

더 많은 정보를 원하시면 [Room Persistence Library 공식 문서](https://developer.android.com/topic/libraries/architecture/room)를 참고하시기 바랍니다.