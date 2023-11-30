---
layout: post
title: "[java] Apache Commons Collections의 다국어 처리 기능"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

Apache Commons Collections는 다양한 자료 구조와 유용한 기능을 제공하는 자바 라이브러리입니다. 이 라이브러리는 다국어 지원을 위한 기능도 제공합니다. 다국어 처리는 각 언어에 맞는 메시지를 제공하는 것을 의미하며, 여러 언어로 애플리케이션을 제작할 때 필요한 기능입니다. 이번 글에서는 Apache Commons Collections에서 제공하는 다국어 처리 기능에 대해 알아보겠습니다.

## ResourceBundleUtils 클래스

Apache Commons Collections의 ResourceBundleUtils 클래스는 ResourceBundle을 이용하여 다국어 처리를 쉽게 할 수 있도록 도와줍니다. ResourceBundle은 각 언어별로 메시지를 관리하는 인터페이스입니다. ResourceBundleUtils 클래스는 이 ResourceBundle을 활용하여 손쉽게 다국어 처리를 할 수 있도록 해줍니다.

## 메시지 파일 작성

다국어 처리를 위해서는 메시지 파일을 작성해야 합니다. 이 메시지 파일에는 각 언어별로 번역된 메시지를 포함시킬 수 있습니다. 메시지 파일은 `.properties` 확장자를 가지며, 여러 개의 파일을 사용하여 각 언어별로 메시지를 관리할 수 있습니다.

예를 들어, `messages.properties` 파일은 기본 메시지를 포함하고 있으며, `messages_en.properties` 파일은 영어로 번역된 메시지를 포함하고 있습니다.

## 메시지 파일 로드

다음은 ResourceBundleUtils를 사용하여 메시지 파일을 로드하는 예제입니다.

```java
ResourceBundle resourceBundle = ResourceBundleUtils.getBundle("messages");
```

위와 같이 `getBundle` 메소드를 사용하여 메시지 파일을 로드할 수 있습니다. 메시지 파일이 있는 클래스 패스에서 파일을 찾아 로드하게 됩니다.

## 메시지 조회

로드한 메시지 파일에서 특정 키에 해당하는 메시지를 조회하는 방법은 다음과 같습니다.

```java
String message = ResourceBundleUtils.getString(resourceBundle, "hello.message");
```

위의 예제는 "hello.message"라는 키에 해당하는 메시지를 가져옵니다.

## 매개변수화된 메시지

메시지 파일에서 가져온 문자열을 동적으로 변환하여 사용할 수도 있습니다. 이를 위해 `getString` 메소드의 다음과 같은 매개변수화된 형식을 사용할 수 있습니다.

```java
String message = ResourceBundleUtils.getString(resourceBundle, "welcome.message", "John");
```

위의 예에서는 "welcome.message"라는 키에 해당하는 메시지를 가져온 후, "John"이라는 값으로 치환하여 사용합니다.

## 결론

Apache Commons Collections의 ResourceBundleUtils 클래스는 다국어 처리를 간단하게 할 수 있는 유용한 기능을 제공합니다. 이를 활용하여 다국어 지원이 필요한 애플리케이션을 개발할 때, 번거로운 다국어 처리 작업을 간단하게 처리할 수 있습니다. 

자세한 내용은 아래 참고 자료를 참조하시기 바랍니다.

## 참고 자료
- [Apache Commons Collections 공식 문서](https://commons.apache.org/proper/commons-collections/)
- [Java ResourceBundle 공식 문서](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/ResourceBundle.html)