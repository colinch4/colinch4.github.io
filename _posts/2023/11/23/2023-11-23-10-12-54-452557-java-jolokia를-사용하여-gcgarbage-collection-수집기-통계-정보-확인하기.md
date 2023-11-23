---
layout: post
title: "[java] Java Jolokia를 사용하여 GC(Garbage Collection) 수집기 통계 정보 확인하기"
description: " "
date: 2023-11-23
tags: [java]
comments: true
share: true
---

GC(Garbage Collection)는 메모리 관리를 위해 자바 가상 머신(JVM)에 의해 수행되는 프로세스입니다. GC 통계 정보는 애플리케이션의 성능 모니터링 및 디버깅에 매우 유용합니다. Java Jolokia는 JVM의 MBean을 쉽게 엑세스하고 이러한 정보를 수집할 수 있는 오픈 소스 에이전트입니다. 이번 글에서는 Java Jolokia를 사용하여 JVM의 GC 수집기 통계 정보를 확인하는 방법에 대해 알아보겠습니다.

## Jolokia란?
Jolokia는 Java 애플리케이션의 MBean을 JSON 형식으로 노출시켜주는 오픈 소스 프로젝트입니다. 이를 통해 원격으로 MBean에 액세스하고 데이터를 읽고 쓸 수 있습니다. Jolokia는 HTTP 프로토콜을 사용하여 MBean 데이터를 JSON으로 전송하므로 원격에서 쉽게 데이터를 수집할 수 있습니다.

## Jolokia 설치 및 설정
1. Jolokia를 다운로드하고 설치합니다. Jolokia는 [공식 웹 사이트](https://jolokia.org/)에서 다운로드할 수 있습니다.
2. 애플리케이션의 `classpath`에 Jolokia JAR 파일을 추가합니다.
3. 애플리케이션의 `web.xml` 파일에 다음과 같이 Jolokia 서블릿을 추가합니다.
```xml
<servlet>
    <servlet-name>Jolokia</servlet-name>
    <servlet-class>org.jolokia.http.AgentServlet</servlet-class>
</servlet>
<servlet-mapping>
    <servlet-name>Jolokia</servlet-name>
    <url-pattern>/jolokia/*</url-pattern>
</servlet-mapping>
```
4. 애플리케이션을 다시 빌드하고 시작합니다.

## Jolokia를 사용하여 GC 통계 정보 수집하기
Jolokia를 사용하여 JVM의 GC 통계 정보를 수집하려면 다음과 같은 단계를 따르면 됩니다.

1. Jolokia 엔드포인트(URL)을 생성합니다. Jolokia는 기본적으로 `/jolokia`로 매핑되어 있습니다. 예를 들어, `http://localhost:8080/jolokia`와 같이 Jolokia 엔드포인트를 만들 수 있습니다.
2. 생성된 Jolokia URL에 GC MBean의 속성 경로를 추가합니다. GC 통계는 `java.lang:type=GarbageCollector,name=*` 경로를 사용하여 수집할 수 있습니다. 여기서 `*`은 모든 GC 수집기를 나타냅니다.
3. Jolokia URL에 HTTP GET 요청을 보내고 JSON 형식의 응답을 받습니다. 수신한 JSON 데이터에서 GC 통계 정보를 추출할 수 있습니다.

아래는 Java 코드로 Jolokia를 사용하여 GC 통계 정보를 수집하는 예제입니다.

```java
import org.apache.http.client.fluent.Request;
import org.json.JSONArray;
import org.json.JSONObject;

public class GcStatisticsExample {
    public static void main(String[] args) throws Exception {
        String jolokiaUrl = "http://localhost:8080/jolokia"; // Jolokia 엔드포인트 URL

        String gcMBeanPath = "java.lang:type=GarbageCollector,name=*"; // GC MBean 경로

        String fullUrl = jolokiaUrl + "/read/" + gcMBeanPath; // Jolokia URL 생성

        String response = Request.Get(fullUrl).execute().returnContent().asString(); // HTTP GET 요청 및 응답 수신

        JSONObject jsonResponse = new JSONObject(response); // JSON 데이터로 변환
        JSONObject gcMBeans = jsonResponse.getJSONObject("value"); // MBean 데이터 추출

        // 각 GC MBean에 대한 통계 정보 출력
        for (String mBeanName : gcMBeans.keySet()) {
            JSONObject gcMBean = gcMBeans.getJSONObject(mBeanName);
            JSONObject gcMBeanAttributes = gcMBean.getJSONObject("Attributes");

            String name = gcMBeanAttributes.getString("Name");
            long collectionCount = gcMBeanAttributes.getLong("CollectionCount");
            long collectionTime = gcMBeanAttributes.getLong("CollectionTime");

            System.out.println("GC MBean Name: " + name);
            System.out.println("Collection Count: " + collectionCount);
            System.out.println("Collection Time: " + collectionTime + "ms");
            System.out.println();
        }
    }
}
```

위의 코드는 Jolokia URL을 생성하고 HTTP GET 요청을 보내서 GC MBean의 통계 정보를 수집합니다. 각 GC MBean의 속성에서 이름, 수집 횟수 및 수집 시간 정보를 추출하여 출력합니다.

## 결론
Java Jolokia를 사용하여 JVM의 GC 통계 정보를 수집하는 방법을 알아보았습니다. Jolokia를 사용하면 원격에서 JVM의 MBean 데이터에 쉽게 접근할 수 있으며, 이를 통해 GC 통계 정보를 모니터링하고 애플리케이션의 성능을 개선할 수 있습니다. Jolokia 관련 자세한 정보는 [공식 문서](https://jolokia.org/reference/html/index.html)를 참조하시기 바랍니다.