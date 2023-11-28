---
layout: post
title: "[java] Java Apache CXF와 보안(Security) 기능"
description: " "
date: 2023-11-28
tags: [java]
comments: true
share: true
---

Apache CXF는 Java 언어로 작성된 오픈 소스 웹 서비스 프레임워크입니다. CXF는 다양한 보안 기능을 제공하여 웹 서비스의 보안 요구 사항을 충족시킬 수 있습니다.

## 1. HTTPS 보안 연결 설정

CXF를 사용하여 웹 서비스를 보호하기 위해 가장 기본적인 보안 기능은 HTTPS를 통한 안전한 연결 설정입니다. 이를 위해서는 CXF 설정 파일 또는 프로그래밍 방식으로 SSL 연결을 구성해야 합니다.

CXF 설정 파일을 사용하는 경우, 아래와 같이 `HTTPConduit` 요소를 추가하고 `tlsClientParameters` 요소 아래에 클라이언트의 인증서와 키를 지정해야 합니다.

```xml
<http:conduit name="*.http-conduit">
    <http:tlsClientParameters>
        <sec:keyManagers keyPassword="password">
            <sec:keyStore type="JKS" password="password"
                    file="client_keystore.jks" />
        </sec:keyManagers>
        <sec:trustManagers>
            <sec:keyStore type="JKS" password="password"
                    file="truststore.jks" />
        </sec:trustManagers>
    </http:tlsClientParameters>
</http:conduit>
```

프로그래밍 방식으로 SSL 연결을 구성하는 경우에는 `Client` 객체를 생성하고 `HTTPConduit` 객체를 설정해야 합니다.

```java
// SSL 설정
HTTPConduit conduit = (HTTPConduit) client.getConduit();
TLSClientParameters tlsParams = new TLSClientParameters();
KeyManager[] myKeyManagers = getKeyManagers();
TrustManager[] myTrustManagers = getTrustManagers();
tlsParams.setKeyManagers(myKeyManagers);
tlsParams.setTrustManagers(myTrustManagers);
conduit.setTlsClientParameters(tlsParams);
```

## 2. WS-Security 보안

CXF는 WS-Security 표준을 준수하는 웹 서비스에 대한 보안 기능을 제공합니다. WS-Security는 웹 서비스 메시지의 기밀성과 무결성을 보장하기 위해 여러 가지 보안 기능을 제공합니다.

CXF 설정 파일을 사용하여 WS-Security 보안을 활성화하는 방법은 다음과 같습니다.

```xml
<jaxws:client id="myClient" ...>
    <jaxws:binding>
        <soap:binding style="document" transport="http://schemas.xmlsoap.org/soap/http"/>
        <sec:binding
                xmlns:sec="http://schemas.xmlsoap.org/ws/2002/07/secext"
                xmlns:tns="http://my.service.namespace.uri"
                xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/">
            <sec:includeTimestamp/>
            <sec:encrypt>
                <sec:algorithmSuite>
                    <xenc:TripleDES xmlns:xenc="http://www.w3.org/2001/04/xmlenc#"/>
                        <xenc:C14NParameterSpec/>
                    </xenc:TripleDES>
                </sec:algorithmSuite>
                <sec:encryptSignature/>
                <sec:usernameToken
                        sec:passwordType="PasswordText"
                        sec:useNonce="false"
                        sec:digestAlgorithm="http://www.w3.org/2000/09/xmldsig#sha1"/>
            </sec:encrypt>
            <sec:signedSupportingTokens>
                <sec:UsernameToken
                        sec:passwordType="PasswordText"
                        sec:useNonce="false"
                        sec:digestAlgorithm="http://www.w3.org/2000/09/xmldsig#sha1">
                    <sec:policy>
                        <sp:WssUsernameToken10
                                xmlns:sp="http://schemas.xmlsoap.org/ws/2005/07/securitypolicy"/>
                    </sec:policy>
                </sec:UsernameToken>
            </sec:signedSupportingTokens>
        </sec:binding>
    </jaxws:binding>
</jaxws:client>
```

위의 설정에서는 메시지에 타임스탬프를 포함하고 메시지를 TripleDES 알고리즘으로 암호화하며, 서명한 보조 토큰을 포함합니다.

## 3. OAuth 보안

CXF는 OAuth 프로토콜을 지원하는 보안 기능도 제공합니다. OAuth는 웹 서비스 인증 및 인가를 위한 프로토콜로 많은 공급자가 지원하고 있습니다.

CXF를 사용하여 OAuth 보안을 설정하려면 OAuth 공급자와 액세스 토큰의 인증 및 인가 서버 URL을 지정해야 합니다. 이후에 CXF 설정 파일에 다음과 같이 추가합니다.

```xml
<cxf:bus>
    <cxf:properties>
        <entry key="security.oauth.consumer-key" value="your-consumer-key"/>
        <entry key="security.oauth.consumer-secret" value="your-consumer-secret"/>
        <entry key="security.oauth.access-token" value="your-access-token"/>
        <entry key="security.oauth.access-token-secret" value="your-access-token-secret"/>
    </cxf:properties>
</cxf:bus>
```

CXF 버스(bus)에 OAuth 속성을 설정하여 보안을 활성화합니다. 소비자 정보와 액세스 토큰은 각각 고유한 값으로 대체되어야 합니다.

## 참고 자료

- Apache CXF 공식 문서: [https://cxf.apache.org/docs/](https://cxf.apache.org/docs/)
- WS-Security 표준: [https://www.ws-security.org/](https://www.ws-security.org/)
- OAuth 공식 문서: [https://oauth.net/](https://oauth.net/)