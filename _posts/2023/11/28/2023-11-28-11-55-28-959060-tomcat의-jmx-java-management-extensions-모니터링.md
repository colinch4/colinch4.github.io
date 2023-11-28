---
layout: post
title: "[java] Tomcat의 JMX (Java Management Extensions) 모니터링"
description: " "
date: 2023-11-28
tags: [java]
comments: true
share: true
---

Tomcat은 기본적으로 JMX (Java Management Extensions)를 사용하여 컨테이너와 애플리케이션의 모니터링을 지원합니다. JMX를 통해 Tomcat의 다양한 메트릭을 수집하고 모니터링할 수 있습니다. 

## JMX 설정

Tomcat에서 JMX를 사용하려면 `catalina.bat` 또는 `catalina.sh` 파일을 열어 아래와 같은 옵션을 추가해야 합니다.

```shell
-Dcom.sun.management.jmxremote
-Dcom.sun.management.jmxremote.port=<포트번호>
-Dcom.sun.management.jmxremote.authenticate=false
-Dcom.sun.management.jmxremote.ssl=false
```

위 설정은 JMX 리모트 접속을 허용하며, 인증 및 SSL 보안 사용을 비활성화합니다. 포트번호는 사용하려는 포트에 맞게 설정해야 합니다.

## JConsole을 통한 모니터링

JConsole은 JDK에 포함된 GUI 기반의 JMX 모니터링 툴입니다. JConsole을 실행하고, "Remote Process" 옵션을 선택한 후 Tomcat 서버의 호스트와 포트 정보를 입력하여 Tomcat에 접속할 수 있습니다. 

JConsole로 Tomcat에 접속하면 다양한 정보를 모니터링할 수 있습니다. 예를 들어, 메모리 사용량, 쓰레드 개수, 힙 사용량 등을 확인할 수 있습니다.

## JMX 원격 접속 보안 설정

JMX는 기본적으로 인증 및 보안 설정이 비활성화되어 있으므로, 원격에서 접속 가능한 포트를 통해 접속할 수 있습니다. 원격 접속을 허용할 때는 보안을 위해 인증 기능을 활성화하고 SSL 보안을 적용하는 것이 좋습니다.

위에서 설명한 JMX 설정에서 다음 옵션을 수정하여 보안 설정을 활성화할 수 있습니다.

```shell
-Dcom.sun.management.jmxremote.authenticate=true
-Dcom.sun.management.jmxremote.ssl=true
```

인증 옵션을 활성화하면 JConsole 또는 다른 JMX 클라이언트에서 접속 시 사용자 이름과 비밀번호를 입력해야 합니다. SSL 옵션을 활성화하면 클라이언트와 서버 간의 통신이 암호화됩니다.

## 결론

Tomcat의 JMX를 통해 다양한 메트릭을 수집하고 모니터링할 수 있습니다. JMX를 활용하면 Tomcat 서버의 상태를 실시간으로 모니터링하고 성능 이슈를 파악할 수 있으므로, 서버 관리 및 튜닝에 매우 유용한 도구입니다.

## 참고 자료

- [Apache Tomcat 9 Documentation - JMX Remote](http://tomcat.apache.org/tomcat-9.0-doc/monitoring.html#Configuring_JMX_Remote)
- [Java SE Documentation - Monitoring and Management Using JMX](https://docs.oracle.com/javase/tutorial/jmx/index.html)