---
layout: post
title: "프로토타입을 이용한 DI(Dependency Injection) 구현"
description: " "
date: 2023-11-06
tags: [프로토타입]
comments: true
share: true
---

## 개요
의존성 주입(Dependency Injection, DI)은 소프트웨어 디자인 패턴 중 하나로, 객체 간의 의존 관계를 외부에서 정의하여 객체 간의 결합도를 낮추는 방법입니다. DI를 구현하는 방법은 다양하지만, 여기서는 프로토타입을 이용하여 DI를 구현하는 방법을 알아보겠습니다.

## 프로토타입 기반 DI 구현 방법

### 1. 의존성 주입을 받을 객체 인터페이스 정의
DI를 받을 객체에 대한 인터페이스를 정의합니다. 이 인터페이스는 DI를 주입받을 메서드를 포함하고 있어야 합니다. 예를 들어, `DatabaseConnection` 인터페이스를 정의하고 `getConnection()` 메서드를 선언하는 것입니다.

```java
public interface DatabaseConnection {
    Connection getConnection();
}
```

### 2. 의존성 주입을 구현할 객체 클래스 정의
DI를 구현할 객체 클래스를 정의합니다. 이 클래스는 의존성 주입을 받을 객체를 멤버 변수로 가지고 있어야 합니다. 예를 들어, `DatabaseConnectionImpl` 클래스를 정의하고 `getConnection()` 메서드를 구현하는 것입니다.

```java
public class DatabaseConnectionImpl implements DatabaseConnection {
    private Connection connection;

    public DatabaseConnectionImpl(Connection connection) {
        this.connection = connection;
    }

    public Connection getConnection() {
        return connection;
    }
}
```

### 3. DI를 사용할 클래스에서 프로토타입 객체 생성 및 주입
DI를 사용할 클래스에서 프로토타입 객체를 생성하고 주입합니다. 예를 들어, `DatabaseService` 클래스에서 `DatabaseConnection` 프로토타입 객체를 생성하고 `getConnection()` 메서드를 호출하는 것입니다.

```java
public class DatabaseService {
    private DatabaseConnection databaseConnection;

    public DatabaseService() {
        // DI를 받을 프로토타입 객체 생성
        DatabaseConnection prototype = new DatabaseConnectionImpl(createConnection());

        // 프로토타입 객체 주입
        setDatabaseConnection(prototype);
    }

    public void setDatabaseConnection(DatabaseConnection databaseConnection) {
        this.databaseConnection = databaseConnection;
    }

    public void performDatabaseOperation() {
        // 의존성 주입 받은 객체의 메서드 호출
        Connection connection = databaseConnection.getConnection();
        // 데이터베이스 연산 수행
    }

    private Connection createConnection() {
        // 데이터베이스 연결 생성
    }
}
```

### 4. 의존성 주입 사용하기
DI를 사용한 클래스에서는 필요한 기능을 수행할 때 의존성 주입을 받은 객체의 메서드를 호출하여 작업을 수행합니다. 위 예시에서는 `DatabaseService` 클래스의 `performDatabaseOperation()` 메서드에서 `DatabaseConnection` 인터페이스를 통해 프로토타입 객체의 `getConnection()` 메서드를 호출하는 것을 볼 수 있습니다.

## 결론
프로토타입을 이용한 DI 구현은 객체 간의 결합도를 낮추고 유연성과 재사용성을 높일 수 있는 방법입니다. 프로토타입을 이용하면 DI를 받을 객체를 동적으로 생성하고 주입할 수 있어 런타임 시에 다양한 의존성을 주입할 수 있습니다. 이를 통해 소프트웨어의 유지보수성과 확장성을 향상시킬 수 있습니다.

---
참고 자료:
- Martin Fowler, "Inversion of Control Containers and the Dependency Injection pattern", [link](https://martinfowler.com/articles/injection.html)
- Baeldung, "Dependency Injection in Java", [link](https://www.baeldung.com/dependency-injection)