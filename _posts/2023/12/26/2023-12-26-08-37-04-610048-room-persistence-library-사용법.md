---
layout: post
title: "[kotlin] Room Persistence Library 사용법"
description: " "
date: 2023-12-26
tags: [kotlin]
comments: true
share: true
---

Room Persistence Library는 안드로이드 앱에서 SQLite 데이터베이스와의 상호 작용을 보다 편리하게 만들어주는 라이브러리입니다. 이 라이브러리를 사용하면 데이터베이스에 쉽게 접근하고 데이터를 관리할 수 있습니다.

## 기본 설정

Room Persistence Library를 사용하기 위해서는 먼저 Gradle 파일에 다음 의존성을 추가해야 합니다.

```gradle
implementation "androidx.room:room-runtime:2.3.0"
annotationProcessor "androidx.room:room-compiler:2.3.0"
```

그 후, 앱의 `Application` 클래스에서 Room 데이터베이스를 초기화해야 합니다.

```kotlin
@Database(entities = [User::class], version = 1)
abstract class AppDatabase : RoomDatabase() {
    abstract fun userDao(): UserDao
}
```

## Entity 정의

Room 데이터베이스에서 관리할 데이터를 정의하기 위해 Entity 클래스를 작성해야 합니다. 예를 들어, 사용자(Users)에 대한 Entity 클래스는 다음과 같이 작성될 수 있습니다.

```kotlin
@Entity
data class User(
    @PrimaryKey val id: Int,
    val name: String,
    val age: Int
)
```

## DAO 작성

Data Access Object(DAO)는 데이터베이스에 접근하여 실제 CRUD(Create, Read, Update, Delete) 작업을 수행하는 메서드를 정의하는 인터페이스입니다. 

```kotlin
@Dao
interface UserDao {
    @Query("SELECT * FROM user")
    fun getAll(): List<User>

    @Query("SELECT * FROM user WHERE id = :userId")
    fun getUserById(userId: Int): User

    @Insert
    fun insert(user: User)

    @Update
    fun update(user: User)

    @Delete
    fun delete(user: User)
}
```

## 데이터베이스 사용

이제 Room 데이터베이스를 사용하여 데이터를 추가, 조회, 수정 및 삭제할 수 있습니다.

```kotlin
val db = Room.databaseBuilder(
    applicationContext,
    AppDatabase::class.java, "database-name"
).build()

val userDao = db.userDao()

// 사용자 추가
val user = User(1, "John Doe", 25)
userDao.insert(user)

// 모든 사용자 조회
val allUsers = userDao.getAll()

// 사용자 수정
user.name = "Jane Doe"
userDao.update(user)

// 사용자 삭제
userDao.delete(user)
```

Room Persistence Library를 사용하면 데이터베이스 관련 작업을 보다 쉽게 처리할 수 있으며, 코드의 가독성과 유지보수성을 높일 수 있습니다.

더 많은 정보는 [Room Persistence Library 공식 문서](https://developer.android.com/reference/android/arch/persistence/room/package-summary)를 참고할 수 있습니다.