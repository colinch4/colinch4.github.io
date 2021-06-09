---
layout: post
title: "[Refactoring] 일반화 처리"
description: " "
date: 2021-06-09
tags: [Refactoring]
comments: true
share: true
---

일반화 처리
-----------

### 필드 상향

-	두 하위클래스에 같은 필드가 들어 있을 땐 필드를 상위 클래스로 옮긴다.

### 메서드 상향

-	기능이 같은 메서드가 `여러 하위클래스에 들어 있을땐` 그 메서드를 상위클래스로 옮긴다.

### 생성자 내용 상향

-	하위클래스마다 거의 비슷한 내용의 생성자가 있을 땐 상위클래스에 생성자를 작성하고 그 생성자를 하위 클래스의 메서드에 호츨한다.

### 메서드 하향

-	상위클래스에 있는 기능을 `일부 하위클래스만 사용`할 땐 그 기능을 관련된 하위클래스 안으로 옮긴다.
-	`메서드 하향`은 `메서드 상향`과 반대되는 기법.
-	클래스의 기능을 특정 하위클래스로 옮겨야 할 때 사용한다.

### 필드 하향

-	일부 하위클래스만이 사용하는 필드가 있을 땐 그 필드를 사용하는 하위클래스로 옮긴다.

### 하위클래스 추출

-	일부 인스턴스에만 사용되는 기능이 든 클래스가 있을 땐 그 기능 부분을 전담하는 하위클래스를 작성한다.
-	`하위클래스 추출` 대신 `클래스 추출`을 사용할 수 있다. `위임`이냐 `상속`이냐의 차이이다.
-	객체가 생성된 후에는 객체의 클래스 `기반 기능`을 수정할 수 없다.
-	클래스 기반 기능을 수정하려면 단순히 다른 각종 컴포넌트를 연결해서 `클래스 추출`을 실시한다.

![하위클래스 추출](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzRENsR0M0SVpaZGs)

### 상위클래스 추출

-	기능이 비슷한 두 클래스가 있을 땐 상위클래스를 작성하고 공통된 기능들을 그 상위클래스로 옮긴다.

![상위클래스 추출](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzMU9BcWhKNlR1Rmc)

### 인터페이스 추출

-	클래스 인터페이스의 같은 부분을 여러 클라이언트가 사용하거나 두 클래스에 인터페이스의 일부분이 공통으로 들어 있을 땐 공통 부분을 인터페이스로 빼낸다.
-	많은 객체지향 언어에서 이 기능은 다중 상속을 통해 구현한다.
-	자바는 하나의 클래스밖에 상속을 할 수 없고, 인터페이스를 사용하여 구현할 수 있다.

### 계층 병합

-	상위클래스와 하위클래스가 거의 다르지 않을 땐 둘을 합친다.

### 템플릿 메서드 형성

-	하위클래스 안의 두 메서드가 거의 비슷한 단계들을 같은 순서로 수행할 땐 그 단계들을 시그너처가 같은 두 개의 메서드로 만들어 두 원본 메서드를 같게 만든 후, 두 메서드를 상위클래스로 옮긴다.
-	두 메서드가 똑같지는 않지만 거의 비슷한 단계를 같은 순서로 수행하는 경우 그 순서를 상위클래스로 옮기고 재정의를 통해 각 단계가 고유의 작업을 다른 방식으로 수행하게 하면 된다. 이러한 메서드를 `템플릿 메서드`라고 한다.

![템플릿 메서드 형성](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzajcwQTVJRXpUZmM)

**수정전**

```java
public class Customer {
    public String statement() {
        return new TextStatement().value(this);
    }
    public String htmlStatement() {
        return new HtmlStatement().value(this);
    }
}
```

```java
public class HtmlStatement {

    public String value(Customer customer) {
        int multiply = 10 * 8;
        String result = "HtmlStatement : 고객님 대여 기록";

        for (int i = 0; i < 6; i++) {
            result += "누적 포인트 HtmlStatement";
        }
        result += "누적 대여료 HtmlStatement";
        return result;
    }

}
```

```java
public class TextStatement {

    public String value(Customer customer) {
        int multiply = 10 * 8;
        String result = "TextStatement : 고객님 대여 기록";

        for (int i = 0; i < 6; i++) {
            result += "누적 포인트 TextStatement";
        }
        result += "누적 대여료 TextStatement";
        return result;
    }

}
```

**수정 후**

```java
public class Customer {
    public String statement() {
        return new TextStatement().value(this );
    }
    public String htmlStatement() {
        return new HtmlStatement().value(this );
    }
}
```

```java
public abstract class Statement {
    public abstract String headerString();
    public abstract String eachString();
    public abstract String footerString();

    public String value(Customer customer) {
        int multiply = 10 * 8;
        String result = headerString();

        for (int i = 0; i < 6; i++) {
            result += eachString();
        }
        result += footerString();
        return result;
    }
}
```

```java
public class HtmlStatement extends Statement{

    @Override
    public String headerString() {
        return "HtmlStatement : 고객님 대여 기록";
    }

    @Override
    public String eachString() {
        return "누적 포인트 HtmlStatement";
    }

    @Override
    public String footerString() {
        return "누적 대여료 HtmlStatement";
    }
}
```

```java
public class TextStatement extends Statement{

    @Override
    public String headerString() {
        return "TextStatement : 고객님 대여 기록";
    }

    @Override
    public String eachString() {
        return "누적 포인트 TextStatement";
    }

    @Override
    public String footerString() {
        return "TextStatement : 고객님 대여 기록";
    }
}
```

### 상속을 위임으로 전환

-	하위클래스가 상위클래스 `인터페이스의 일부`만 사용할 때나 데이터를 상속받지 않게 해야할 땐 상위클래스에 필드를 작성하고, 모든 메서드가 그 상위클래스에 위임하게 수정한 후 하위클래스를 없앤다.

### 위임을 상속으로 전환

-	위임을 이용중인데 `인터페이스 전반`에 간단한 위임으로 도배하게 될 땐 위임 클래스를 대리 객체의 하위클래스로 만든다.
-	`상속을 위임으로 전환`기법을 반대로 하면 된다.
