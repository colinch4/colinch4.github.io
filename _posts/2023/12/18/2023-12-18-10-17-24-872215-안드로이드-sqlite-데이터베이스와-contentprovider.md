---
layout: post
title: "[android] 안드로이드 SQLite 데이터베이스와 ContentProvider"
description: " "
date: 2023-12-18
tags: [android]
comments: true
share: true
---

안드로이드 앱에서 데이터를 저장하고 관리하는 가장 일반적인 방법 중 하나는 SQLite 데이터베이스를 사용하는 것입니다. SQLite는 경량의 관계형 데이터베이스이며 안드로이드 플랫폼에 기본으로 내장되어 있어 안드로이드 앱의 데이터 저장 및 관리에 이상적입니다. 또한, ContentProvider를 사용하여 데이터를 다른 애플리케이션과 공유할 수 있습니다.

## SQLite 데이터베이스

SQLite 데이터베이스를 안드로이드 앱에 구현하는 방법은 다음과 같습니다.

### 데이터베이스 생성

```java
public class DatabaseHelper extends SQLiteOpenHelper {
    private static final String DATABASE_NAME = "MyDatabase";
    private static final int DATABASE_VERSION = 1;

    public DatabaseHelper(Context context) {
        super(context, DATABASE_NAME, null, DATABASE_VERSION);
    }

    // onCreate() 메서드에서 테이블 생성 및 초기 데이터 삽입
    @Override
    public void onCreate(SQLiteDatabase db) {
        db.execSQL("CREATE TABLE MyTable (id INTEGER PRIMARY KEY, name TEXT)");
    }

    // onUpgrade() 메서드에서 테이블 업그레이드
    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        db.execSQL("DROP TABLE IF EXISTS MyTable");
        onCreate(db);
    }
}
```

### 데이터 조작

```java
public class DataRepository {
    private SQLiteDatabase database;

    public DataRepository(Context context) {
        DatabaseHelper dbHelper = new DatabaseHelper(context);
        database = dbHelper.getWritableDatabase();
    }

    public void insertData(String name) {
        ContentValues values = new ContentValues();
        values.put("name", name);
        database.insert("MyTable", null, values);
    }

    // 데이터 조회, 갱신, 삭제 등의 메서드 추가
}
```

## ContentProvider

ContentProvider를 통해 데이터를 다른 애플리케이션과 공유할 수 있습니다.

### ContentProvider 구현

```java
public class MyContentProvider extends ContentProvider {
    public static final Uri CONTENT_URI = Uri.parse("content://com.example.provider/MyTable");

    @Override
    public boolean onCreate() {
        // ContentProvider 초기화 작업 수행
        return true;
    }

    @Nullable
    @Override
    public Cursor query(@NonNull Uri uri, @Nullable String[] projection, @Nullable String selection, @Nullable String[] selectionArgs, @Nullable String sortOrder) {
        // 데이터 조회 구현
    }

    @Nullable
    @Override
    public Uri insert(@NonNull Uri uri, @Nullable ContentValues values) {
        // 데이터 삽입 구현
    }

    // 나머지 CRUD 메서드 및 MIME 타입 정의
}
```

### ContentProvider 사용

```java
Uri uri = MyContentProvider.CONTENT_URI;
ContentValues values = new ContentValues();
values.put("name", "John Doe");
getContentResolver().insert(uri, values);
```

SQLite 데이터베이스와 ContentProvider는 안드로이드 앱에서 데이터 저장 및 공유의 중요한 기능을 담당합니다.

참고 자료:
- 안드로이드 공식 문서: https://developer.android.com/guide/topics/providers/content-providers
- SQLite 공식 문서: https://www.sqlite.org/docs.html