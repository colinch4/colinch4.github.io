---
layout: post
title: "[android] 안드로이드 SQLite 데이터베이스와 ORM (Object Relational Mapping)"
description: " "
date: 2023-12-18
tags: [android]
comments: true
share: true
---

안드로이드 앱을 개발할 때 데이터를 저장하고 관리하는 것은 매우 중요합니다. SQLite 데이터베이스를 사용하여 안드로이드 앱에서 데이터를 지속적으로 저장하고 관리하는 방법을 알아보겠습니다.

## SQLite 데이터베이스

SQLite는 서버가 아닌 클라이언트-사이드의 로컬 데이터베이스로서 경량의 관계형 데이터베이스 관리 시스템입니다. 안드로이드에서 SQLite 데이터베이스를 사용하면 구조화된 데이터를 지속적으로 저장하고 검색할 수 있습니다. SQLite 데이터베이스는 기본적으로 안드로이드 프레임워크에 내장되어 있어 추가적인 설정이 필요하지 않습니다.

```java
// SQLite 데이터베이스 생성 및 버전 관리
public class MyDBHelper extends SQLiteOpenHelper {
    private static final String DATABASE_NAME = "mydatabase.db";
    private static final int DATABASE_VERSION = 1;

    public MyDBHelper(Context context) {
        super(context, DATABASE_NAME, null, DATABASE_VERSION);
    }

    @Override
    public void onCreate(SQLiteDatabase db) {
        // 테이블 생성
        db.execSQL("CREATE TABLE contacts (_id INTEGER PRIMARY KEY, name TEXT, email TEXT)");
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        // 데이터베이스 버전 관리
        db.execSQL("DROP TABLE IF EXISTS contacts");
        onCreate(db);
    }
}
```

## ORM (Object Relational Mapping)

ORM은 데이터베이스와 객체간의 매핑을 자동화하는 기술로, 객체 지향 프로그래밍 언어에서 관계형 데이터베이스의 데이터를 객체로 매핑하는 과정을 단순화합니다. 안드로이드 개발에서 ORM 라이브러리를 사용하면 데이터베이스 작업을 보다 쉽게 처리할 수 있습니다. 대표적인 안드로이드 ORM 라이브러리로는 Room, GreenDAO, Realm 등이 있습니다.

```java
// Room 라이브러리를 사용한 안드로이드 데이터베이스 처리 예시
@Entity
public class Contact {
    @PrimaryKey
    public int id;

    @ColumnInfo(name = "name")
    public String name;

    @ColumnInfo(name = "email")
    public String email;
}

@Dao
public interface ContactDao {
    @Query("SELECT * FROM contact")
    List<Contact> getAll();

    @Insert
    void insert(Contact contact);

    @Update
    void update(Contact contact);

    @Delete
    void delete(Contact contact);
}

@Database(entities = {Contact.class}, version = 1)
public abstract class AppDatabase extends RoomDatabase {
    public abstract ContactDao contactDao();
}
```

SQLite 데이터베이스와 ORM을 활용하여 안드로이드 앱에서 데이터를 효과적으로 저장하고 관리할 수 있습니다. 데이터베이스와 객체 간의 매핑이 더욱 간편해지므로 안드로이드 앱의 성능과 유지보수가 용이해집니다.

참고문헌:
- https://developer.android.com/training/data-storage/sqlite
- https://developer.android.com/jetpack/androidx/releases/room

[SQLite 관련 포스트]: (https://www.androidhive.info/2011/11/android-sqlite-database-tutorial/)