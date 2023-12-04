---
layout: post
title: "[java] 데이터 저장 (SQLite, SharedPreferences 등)"
description: " "
date: 2023-12-04
tags: [java]
comments: true
share: true
---

Java 언어는 다양한 방법으로 데이터를 저장할 수 있습니다. 여기에서는 SQLite와 SharedPreferences를 사용하는 방법을 알아보겠습니다.

## SQLite

SQLite는 임베디드 SQL 데이터베이스 엔진이며, 애플리케이션 내에서 구조화된 데이터를 저장하기에 적합합니다.

SQLite를 사용하기 위해 먼저 다음 단계를 따르세요.

1. SQLite 데이터베이스 파일을 생성합니다.
2. 데이터베이스 연결을 설정합니다.
3. 테이블을 만들고 필요한 데이터를 저장합니다.
4. 데이터를 조회하거나 수정할 수 있습니다.

아래는 예시 코드입니다.

```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;

public class SQLiteDataStorage {
    public static void main(String[] args) {
        Connection connection = null;
        Statement statement = null;
        
        try {
            // 1. SQLite 데이터베이스 파일 생성
            Class.forName("org.sqlite.JDBC");
            connection = DriverManager.getConnection("jdbc:sqlite:test.db");
            
            // 2. 데이터베이스 연결 설정
            statement = connection.createStatement();
            
            // 3. 데이터 저장하기
            String insertQuery = "INSERT INTO users (id, name) VALUES (1, 'John')";
            statement.executeUpdate(insertQuery);
            
            // 4. 데이터 조회하기
            String selectQuery = "SELECT * FROM users";
            ResultSet resultSet = statement.executeQuery(selectQuery);
            
            while (resultSet.next()) {
                int id = resultSet.getInt("id");
                String name = resultSet.getString("name");
                System.out.println("ID: " + id + ", Name: " + name);
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            try {
                if (statement != null)
                    statement.close();
                if (connection != null)
                    connection.close();
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }
}
```

위의 예시 코드에서는 `java.sql` 패키지를 사용하여 SQLite 데이터베이스에 연결하고 데이터를 저장하고 조회하는 방법을 보여줍니다.

## SharedPreferences

SharedPreferences는 애플리케이션 내에 작은 키-값의 쌍을 저장하기에 적합한 메커니즘입니다.

SharedPreferences를 사용하기 위해 다음 단계를 따르세요.

1. SharedPreferences 객체를 가져옵니다.
2. 필요한 데이터를 저장하거나 조회합니다.

아래는 예시 코드입니다.

```java
import android.content.Context;
import android.content.SharedPreferences;

public class SharedPreferencesDataStorage {
    public static void main(String[] args) {
        Context context = // 애플리케이션의 Context 객체를 가져옵니다.
        SharedPreferences sharedPreferences = context.getSharedPreferences("my_prefs", Context.MODE_PRIVATE);
        
        // 데이터 저장하기
        SharedPreferences.Editor editor = sharedPreferences.edit();
        editor.putInt("number", 10);
        editor.putString("name", "John");
        editor.apply();
        
        // 데이터 조회하기
        int number = sharedPreferences.getInt("number", 0);
        String name = sharedPreferences.getString("name", "");
        System.out.println("Number: " + number + ", Name: " + name);
    }
}
```

위의 예시 코드에서는 `android.content.SharedPreferences` 클래스를 사용하여 SharedPreferences에 데이터를 저장하고 조회하는 방법을 보여줍니다.

## 참고 자료

- SQLite: [https://www.sqlite.org/](https://www.sqlite.org/)
- SharedPreferences: [https://developer.android.com/reference/android/content/SharedPreferences](https://developer.android.com/reference/android/content/SharedPreferences)
- Java Database Connectivity (JDBC): [https://docs.oracle.com/en/java/javase/11/docs/api/java.sql/module-summary.html](https://docs.oracle.com/en/java/javase/11/docs/api/java.sql/module-summary.html)