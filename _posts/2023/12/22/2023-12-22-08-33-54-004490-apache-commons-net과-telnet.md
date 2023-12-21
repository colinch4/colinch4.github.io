---
layout: post
title: "[java] Apache Commons Net과 Telnet"
description: " "
date: 2023-12-22
tags: [java]
comments: true
share: true
---

Apache Commons Net은 네트워크 작업을 쉽게 처리할 수 있는 라이브러리입니다. 이 라이브러리는 다양한 프로토콜을 지원하며, Telnet 통신을 위한 간편한 API도 제공합니다.

## Apache Commons Net 추가

Apache Commons Net은 Maven을 사용하여 프로젝트에 쉽게 추가할 수 있습니다. 다음과 같이 의존성을 추가하여 pom.xml 파일에 라이브러리를 포함시킬 수 있습니다.

```xml
<dependency>
    <groupId>commons-net</groupId>
    <artifactId>commons-net</artifactId>
    <version>3.6</version>
</dependency>
```

의존성을 추가한 뒤에는 Maven을 통해 프로젝트를 업데이트하여 라이브러리를 다운로드할 수 있습니다.

## Telnet 클라이언트 구현

Telnet으로 서버에 접속하고 데이터를 주고받기 위한 간단한 Java 클라이언트를 구현해보겠습니다. 

```java
import org.apache.commons.net.telnet.TelnetClient;
import java.io.InputStream;
import java.io.PrintStream;

public class TelnetExample {
    public static void main(String[] args) {
        try {
            TelnetClient telnet = new TelnetClient();
            telnet.connect("hostname", 23);

            InputStream inputStream = telnet.getInputStream();
            PrintStream outputStream = new PrintStream(telnet.getOutputStream());

            // 서버 응답 받아오기
            byte[] buffer = new byte[1024];
            int bytesRead;
            do {
                bytesRead = inputStream.read(buffer);
                System.out.print(new String(buffer, 0, bytesRead));
            } while (bytesRead >= 0);

            // 데이터 서버로 보내기
            outputStream.println("ls");
            outputStream.flush();

            // 결과 받아오기
            buffer = new byte[1024];
            bytesRead = inputStream.read(buffer);
            System.out.println(new String(buffer, 0, bytesRead));

            telnet.disconnect() ;
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

위의 코드는 Telnet 클라이언트를 구현한 것으로, Apache Commons Net의 `TelnetClient`를 사용하여 Telnet 서버에 접속하고 데이터를 주고받는 예제입니다.

## 결론

Apache Commons Net을 사용하여 Telnet 클라이언트를 구현하는 것은 매우 간단합니다. 이를 통해 Telnet을 통한 네트워크 통신을 효과적으로 처리할 수 있습니다. 

더 자세한 내용은 [Apache Commons Net 공식 문서](https://commons.apache.org/proper/commons-net/)를 참고하시기 바랍니다.