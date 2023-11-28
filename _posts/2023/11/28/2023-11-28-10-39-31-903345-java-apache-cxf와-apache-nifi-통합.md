---
layout: post
title: "[java] Java Apache CXF와 Apache NiFi 통합"
description: " "
date: 2023-11-28
tags: [java]
comments: true
share: true
---

## 소개
Apache CXF와 Apache NiFi는 각각 웹 서비스 및 데이터 플로우를 처리하는 데 사용되는 Java 기반 오픈 소스 프레임워크입니다. 이들을 통합하여 웹 서비스 요청을 처리하고 데이터 흐름을 조작할 수 있습니다.

## Apache CXF
Apache CXF는 Java 언어로 작성된 오픈 소스 웹 서비스 프레임워크입니다. CXF는 강력한 웹 서비스 기능을 제공하며, WSDL 및 SOAP 프로토콜을 지원하여 웹 서비스를 구현 및 배포할 수 있습니다.

## Apache NiFi
Apache NiFi는 데이터 플로우 관리 시스템으로, 데이터 처리 및 통합을 위한 미리 정의된 구성 요소들을 제공합니다. NiFi를 사용하여 데이터를 수집, 전송, 처리 및 저장할 수 있으며, 강력한 흐름 제어 및 모니터링 기능을 제공합니다.

## Apache CXF와 Apache NiFi 통합 과정
Apache CXF와 Apache NiFi를 통합하는 과정은 다음과 같습니다:

1. Apache CXF를 사용하여 웹 서비스를 구현하고 배포합니다.
2. Apache NiFi에서 CXF 웹 서비스 요청을 수신하기 위해 NiFi의 ListenHTTP 컴포넌트를 설정합니다.
3. NiFi의 ListenHTTP 컴포넌트는 CXF 서비스의 엔드포인트 URL로 설정됩니다.
4. ListenHTTP 컴포넌트는 들어오는 웹 서비스 요청을 받아들이고, 바이트 배열로 변환하여 NiFi의 흐름으로 보냅니다.
5. NiFi 흐름에서 필요한 처리를 수행한 후, 결과를 다시 CXF 웹 서비스 클라이언트에 반환합니다.

## 예제 코드
```java
import org.apache.cxf.jaxrs.JAXRSServerFactoryBean;
import org.apache.nifi.http.HttpMethod;
import org.apache.nifi.processor.*;
import org.apache.nifi.processor.exception.ProcessException;
import org.apache.nifi.remote.client.SiteToSiteClient;
import org.apache.nifi.remote.protocol.SiteToSiteTransportProtocol;

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;

@Path("/data")
public class DataResource {

    @GET
    @Path("/get")
    @Produces(MediaType.TEXT_PLAIN)
    public String getData() {
        // Apache NiFi로부터 데이터를 가져옴
        return "Data from Apache NiFi";
    }

    public static void main(String[] args) throws Exception {
        // Apache CXF 서비스 세팅
        JAXRSServerFactoryBean sf = new JAXRSServerFactoryBean();
        sf.setResourceClasses(DataResource.class);
        sf.setAddress("http://localhost:8080/");
        sf.create();

        // Apache NiFi로 데이터 전달
        SiteToSiteClient client = new SiteToSiteClient.Builder()
                .url("http://localhost:8090/nifi")
                .transportProtocol(SiteToSiteTransportProtocol.HTTP)
                .portName("input")
                .build();

        Transaction transaction = client.createTransaction();
        try {
            // Apache NiFi로 데이터 전송
            String data = "Data to Apache NiFi";
            byte[] bytes = data.getBytes();
            transaction.send(bytes);
            transaction.confirm();
        } catch (ProcessException e) {
            transaction.rollback();
        } finally {
            transaction.complete();
        }
    }
}
```

## 참고 자료
- [Apache CXF 공식 사이트](https://cxf.apache.org/)
- [Apache NiFi 공식 사이트](https://nifi.apache.org/)