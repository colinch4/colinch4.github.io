---
layout: post
title: "[kotlin] Room 라이브러리와 ORM (Object-Relational Mapping) 관련 기능"
description: " "
date: 2023-12-21
tags: [kotlin]
comments: true
share: true
---

안녕하세요! 이번에는 안드로이드 앱에서 SQLite 데이터베이스를 더 쉽게 다룰 수 있게 해주는 **Room 라이브러리**와 **ORM(Object-Relational Mapping)**에 대해 알아보겠습니다.

## 1. Room 라이브러리란 무엇인가요?
Room 라이브러리는 SQLite 데이터베이스에 접근하고 조작하는 기능을 제공하는 안드로이드 아키텍처 컴포넌트입니다. 또한, ORM 디자인 패턴을 구현하여 데이터베이스의 테이블과 자바 객체를 매핑할 수 있도록 도와줍니다.

## 2. Room에서 제공하는 주요 기능
Room 라이브러리는 세 가지 주요 구성 요소를 갖고 있습니다.
- **Entity**: 데이터베이스의 테이블을 나타내는 클래스입니다. 
- **DAO(데이터 액세스 객체)**: 데이터베이스에 액세스할 메서드를 정의한 인터페이스입니다.
- **Database**: 데이터베이스 홀더를 나타내며, 데이터베이스의 주요 기능을 포함하고 데이터베이스와 관련된 인터페이스를 제공합니다.

## 3. Room과 ORM
Room은 ORM(Object-Relational Mapping)에 기반하여 작동합니다. 이는 개발자가 데이터베이스의 테이블을 나타내는 클래스를 정의하고, 이 클래스의 객체를 사용하여 데이터베이스 작업을 수행할 수 있다는 장점을 제공합니다. 이를 통해 보다 관리하기 쉬운 코드를 작성할 수 있고, 데이터베이스 스키마 변경에 대한 처리도 간편해집니다.

```kotlin
@Entity
data class User(
    @PrimaryKey val userId: Int,
    val userName: String
)

@Dao
interface UserDao {
    @Query("SELECT * FROM user")
    fun getAll(): List<User>

    @Insert
    fun insert(user: User)
}

@Database(entities = [User::class], version = 1)
abstract class AppDatabase : RoomDatabase() {
    abstract fun userDao(): UserDao
}
```

위 코드에서 `@Entity` 어노테이션을 사용하여 `User` 클래스를 데이터베이스의 테이블로 지정하고, `@Dao` 어노테이션을 사용하여 `UserDao` 인터페이스를 데이터베이스 액세스 객체로 정의하였습니다.

## 4. Room 라이브러리의 장점
Room 라이브러리를 사용하면 안드로이드 앱에서 데이터베이스를 다루는 과정이 보다 간단해집니다. 또한, 컴파일 시간에 SQL 쿼리 오류를 잡을 수 있고, 데이터베이스 작업을 UI 스레드가 아닌 백그라운드 스레드에서 처리할 수 있도록 도와줍니다.

## 마치며
Room 라이브러리는 안드로이드 앱의 데이터베이스 처리를 보다 쉽고 안전하게 해주는 강력한 도구입니다. ORM 패턴을 적용하여 데이터베이스 작업을 추상화하고, 안드로이드 아키텍처 컴포넌트로서의 장점을 완벽하게 활용할 수 있습니다.

이상으로 Room 라이브러리와 ORM에 관한 기능에 대해 알아보았습니다. 감사합니다!

## 참고 자료
- [Android Developer - Room 라이브러리](https://developer.android.com/training/data-storage/room)
- [CodeLab - 안드로이드 데이터베이스와 Room 라이브러리](https://developer.android.com/codelabs/android-room-with-a-view#0)