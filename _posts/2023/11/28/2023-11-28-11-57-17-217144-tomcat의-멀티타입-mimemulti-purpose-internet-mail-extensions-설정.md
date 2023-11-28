---
layout: post
title: "[java] Tomcat의 멀티타입 MIME(Multi-Purpose Internet Mail Extensions) 설정"
description: " "
date: 2023-11-28
tags: [java]
comments: true
share: true
---

## 개요
Tomcat은 웹 서버와 같이 정적 리소스를 서비스하는 데 사용되는 Java 웹 애플리케이션 서버입니다. 정적 리소스의 MIME 타입은 클라이언트에게 전달되는 파일의 유형을 나타내는 데 사용됩니다. Tomcat은 확장자와 MIME 타입 간의 매핑을 통해 MIME 타입을 설정할 수 있습니다. 이 글에서는 Tomcat의 멀티타입 MIME 설정 방법에 대해 알아보겠습니다.

## 실습
Tomcat의 멀티타입 MIME 설정은 `conf/web.xml` 파일에서 수행됩니다. 아래는 `web.xml` 파일의 예시입니다.

```xml
<web-app>
  ...
  <mime-mapping>
    <extension>txt</extension>
    <mime-type>text/plain</mime-type>
  </mime-mapping>
  <mime-mapping>
    <extension>png</extension>
    <mime-type>image/png</mime-type>
  </mime-mapping>
  ...
</web-app>
```

위 예시에서는 `.txt` 확장자에 대해 `text/plain` MIME 타입을, `.png` 확장자에 대해 `image/png` MIME 타입을 설정하고 있습니다. 다른 확장자에 대해도 동일한 방식으로 MIME 타입을 설정할 수 있습니다.

`<mime-mapping>` 엘리먼트는 확장자와 MIME 타입 간의 매핑을 나타내며, `<extension>` 엘리먼트는 확장자를, `<mime-type>` 엘리먼트는 MIME 타입을 정의합니다.

## 주의사항
- `web.xml` 파일을 수정한 후에는 Tomcat 서버를 재시작해야 설정이 적용됩니다.
- Tomcat 7 이상부터는 `conf/web.xml` 파일 대신 각 웹 애플리케이션의 `WEB-INF/web.xml` 파일을 사용할 수도 있습니다.

## 참고 자료
- [Apache Tomcat Documentation](https://tomcat.apache.org/tomcat-9.0-doc/index.html)