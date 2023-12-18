---
layout: post
title: "[android] 안드로이드 SQLite 데이터베이스와 Room Persistence Library"
description: " "
date: 2023-12-18
tags: [android]
comments: true
share: true
---

안드로이드 애플리케이션을 개발할 때 데이터를 지속적으로 저장하고 관리해야 할 때가 있습니다. 안드로이드에서 SQLite 데이터베이스를 사용하여 데이터를 로컬에 지속적으로 저장하는 방법과 최근에 안드로이드에서 소개된 Room Persistence Library를 사용하는 방법에 대해 알아보겠습니다.

## SQLite 데이터베이스

SQLite는 안드로이드 애플리케이션에서 사용할 수 있는 경량의 데이터베이스 엔진으로써, 안드로이드 시스템에 기본적으로 내장되어 있습니다. SQLite를 사용하면 안드로이드 애플리케이션에서 간단하게 데이터를 지속적으로 저장하고, 조회, 수정, 삭제할 수 있습니다.

SQLite를 사용하기 위해서는 데이터베이스 생성, 테이블 생성, 데이터 추가, 조회, 수정, 삭제 등의 다양한 작업을 수행해야 합니다. 이러한 작업들은 안드로이드에서 제공하는 `SQLiteOpenHelper`나 `SQLiteDatabase` 클래스 등을 사용하여 구현할 수 있습니다.

```java
// Example code
public class DBHelper extends SQLiteOpenHelper {
    private static final String DATABASE_NAME = "myapp.db";
    private static final int DATABASE_VERSION = 1;

    public DBHelper(Context context) {
        super(context, DATABASE_NAME, null, DATABASE_VERSION);
    }

    @Override
    public void onCreate(SQLiteDatabase db) {
        // Create tables and initialize the database
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        // Upgrade the database schema
    }
}
```

## Room Persistence Library

Room은 안드로이드에서 SQLite 데이터베이스를 좀 더 쉽게 사용할 수 있도록 도와주는 라이브러리입니다. Room을 사용하면 SQLite 데이터베이스에 접근하기 위한 코드를 간소화할 수 있고, 데이터베이스 구조를 정적으로 분석하여 컴파일 타임에 오류를 발견할 수 있습니다.

Room은 세 가지 주요 구성 요소로 구성되어 있습니다.
1. **Database**: 앱의 지속적인 관계형 데이터를 저장하는 주체로써의 역할을 합니다.
2. **Entity**: 데이터베이스의 테이블을 나타내는 클래스입니다.
3. **DAO**: 데이터베이스에서 데이터를 조회, 추가, 수정, 삭제하는 메서드를 정의하는 인터페이스입니다.

```java
// Example code
@Entity
public class User {
    @PrimaryKey
    public int id;
    public String name;
    public String email;
}

@Dao
public interface UserDao {
    @Query("SELECT * FROM user")
    List<User> getAll();

    @Insert
    void insert(User user);
}
```

Room은 데이터베이스와 관련된 번거로운 작업들을 캡슐화하여 코드의 간결성을 높여주고, SQLite 데이터베이스를 사용하여 안정적이고 효율적으로 데이터를 관리할 수 있도록 도와줍니다.

## 결론

SQLite 데이터베이스와 Room Persistence Library는 안드로이드 애플리케이션에서 데이터를 지속적으로 저장하고 관리하는 데 유용한 도구입니다. SQLite를 직접 다루는 것보다 Room을 사용하는 것이 코드의 간소화와 안정성 측면에서 더 나은 선택일 수 있으며, 개발자들이 데이터베이스 관련 작업에 더 많은 시간을 투자할 수 있도록 도와줍니다.

이러한 이점들로 인해 안드로이드 애플리케이션을 개발할 때 데이터베이스를 사용해야 할 경우, Room Persistence Library를 사용하는 것이 권장됩니다.

참고문헌:
- 안드로이드 공식 문서: https://developer.android.com/training/data-storage/room
- SQLite 공식 사이트: https://www.sqlite.org/

[Android]: /android
[SQLite]: /sqlite
[Room Persistence Library]: /room-persistence-library