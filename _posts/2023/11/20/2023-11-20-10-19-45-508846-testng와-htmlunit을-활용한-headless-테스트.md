---
layout: post
title: "[java] TestNG와 HTMLUnit을 활용한 Headless 테스트"
description: " "
date: 2023-11-20
tags: [java]
comments: true
share: true
---

이 글에서는 TestNG와 HTMLUnit을 이용하여 Headless 테스트를 수행하는 방법을 소개하고자 합니다.

## Headless 테스트란?

Headless 테스트는 GUI 없이 웹 어플리케이션을 테스트하는 방법입니다. 이를 통해 빠르고 자동화된 테스트를 수행할 수 있습니다. HTMLUnit은 Java에서 제공하는 Headless 브라우저로, 웹 페이지를 동적으로 로드하고 테스트를 수행할 수 있는 기능을 제공합니다.

## TestNG 소개

TestNG는 자바 기반의 테스팅 프레임워크로, JUnit과 같은 역할을 합니다. TestNG는 더 다양한 어노테이션 및 테스트 그룹 기능을 제공하여 테스트를 보다 효율적으로 관리할 수 있습니다.

## HTMLUnit 설치

HTMLUnit은 Maven을 통해 간편하게 설치할 수 있습니다. `pom.xml` 파일에 다음의 의존성을 추가해주세요.

```xml
<dependency>
    <groupId>net.sourceforge.htmlunit</groupId>
    <artifactId>htmlunit</artifactId>
    <version>2.36.0</version>
</dependency>
```

의존성 추가 후 Maven이 프로젝트를 업데이트하면 HTMLUnit이 설치됩니다.

## TestNG 테스트 작성

이제 TestNG를 사용하여 Headless 테스트를 작성해보겠습니다. 아래는 HTMLUnit을 이용하여 "https://www.example.com" 웹 페이지에 접속하여 타이틀을 확인하는 테스트입니다.

```java
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.htmlunit.HtmlUnitDriver;
import org.testng.annotations.Test;

public class HeadlessTest {

    @Test
    public void checkTitle() {
        // Headless 브라우저 생성
        WebDriver driver = new HtmlUnitDriver();

        // 웹 페이지 접속
        driver.get("https://www.example.com");

        // 타이틀 확인
        String title = driver.getTitle();
        System.out.println("페이지 타이틀: " + title);

        // 브라우저 종료
        driver.quit();
    }
}
```

위의 코드에서 `HtmlUnitDriver`는 HTMLUnit을 사용하는 WebDriver입니다. `driver.get(url)`을 통해 해당 URL에 접속하고, `driver.getTitle()`을 통해 페이지의 타이틀을 가져올 수 있습니다.

## TestNG 실행

테스트를 실행하기 위해 TestNG 실행 파일을 생성해야 합니다. TestNG 패키지를 다운로드하고, 실행 파일을 생성한 후 아래와 같이 작성해주세요.

```xml
<!DOCTYPE suite SYSTEM "http://testng.org/testng-1.0.dtd">
<suite name="Headless Test Suite">
    <test name="Headless Test">
        <classes>
            <class name="com.example.HeadlessTest"/>
        </classes>
    </test>
</suite>
```

위의 XML 파일에서 `class name`은 테스트 대상 클래스를 지정합니다. 만약 여러 개의 테스트 클래스가 있다면, 여러 개의 `class`를 추가해주면 됩니다.

테스트를 실행하기 위해 TestNG를 커맨드 라인에서 실행합니다.

```shell
java -cp "testng.jar:your-project.jar" org.testng.TestNG testng.xml
```

## 결과 확인

실행이 완료되면 테스트 결과를 확인할 수 있습니다. 콘솔에는 "페이지 타이틀: Example Domain"이 출력될 것입니다.

이처럼 TestNG와 HTMLUnit을 이용하여 Headless 테스트를 손쉽게 수행할 수 있습니다. 테스트 코드를 작성하고 TestNG를 실행함으로써 웹 어플리케이션의 동작을 자동으로 확인할 수 있습니다.

## 참고자료
- [HTMLUnit 공식 사이트](http://htmlunit.sourceforge.net/)
- [TestNG 공식 사이트](https://testng.org/doc/index.html)