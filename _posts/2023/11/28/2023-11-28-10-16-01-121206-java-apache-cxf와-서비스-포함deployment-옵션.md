---
layout: post
title: "[java] Java Apache CXF와 서비스 포함(Deployment) 옵션"
description: " "
date: 2023-11-28
tags: [java]
comments: true
share: true
---

Java Apache CXF는 웹 서비스를 구축하는 데 사용되는 한 오픈 소스 프레임워크입니다. CXF를 사용하면 Java로 웹 서비스를 쉽게 개발하고 배포할 수 있습니다. 이번 글에서는 CXF를 사용하여 웹 서비스를 배포할 때의 서비스 포함 옵션에 대해 알아보겠습니다.

CXF에서 웹 서비스를 배포하는 방법 중 하나는 서비스를 WAR 파일로 묶어 애플리케이션 서버에 배포하는 것입니다. 이 경우, CXF는 자동으로 Apache Tomcat, JBoss 등과 같은 애플리케이션 서버와 통합하여 웹 서비스를 실행하게 됩니다.

CXF에서 서비스 포함(Deployment) 옵션을 사용하려면 `cxf-servlet.xml` 파일을 작성해야 합니다. 이 파일은 서비스 포함(Deployment)에 필요한 설정을 정의하는데 사용됩니다.

다음은 `cxf-servlet.xml` 파일의 예입니다.

```xml
<beans xmlns="http://www.springframework.org/schema/beans"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.springframework.org/schema/beans
        http://www.springframework.org/schema/beans/spring-beans.xsd
        http://cxf.apache.org/jaxrs http://cxf.apache.org/schemas/jaxrs.xsd"
    xmlns:cxf="http://cxf.apache.org/core"
    xmlns:jaxrs="http://cxf.apache.org/jaxrs">

    <!-- 서비스 포함(Deployment)을 위한 설정 -->
    <jaxrs:server id="myService" address="/">
        <jaxrs:serviceBeans>
            <ref bean="myServiceBean" />
        </jaxrs:serviceBeans>
    </jaxrs:server>

    <bean id="myServiceBean" class="com.example.MyService" />

</beans>
```

위의 예제에서는 `myServiceBean`이라는 이름의 웹 서비스를 정의하고 `myService`라는 ID를 가진 `jaxrs:server`를 통해 서비스를 포함(Deployment)합니다. 웹 서비스 클래스는 `com.example.MyService`로 지정되어 있습니다.

이제 `cxf-servlet.xml` 파일을 생성하고 필요한 설정을 추가한 후, WAR 파일에 포함시켜 애플리케이션 서버에 배포하면 CXF가 자동으로 웹 서비스를 실행합니다. 배포된 웹 서비스는 루트 경로("/")로 접근할 수 있습니다.

위에 설명한 것은 CXF를 사용하여 웹 서비스를 배포할 때 서비스 포함(Deployment) 옵션을 설정하는 방법에 대한 간단한 예제였습니다. 물론 복잡한 설정이나 다양한 폼으로 배포하는 방법도 있을 수 있습니다. 더 자세한 내용은 CXF의 공식 문서를 참고하시기 바랍니다.

**참고 자료:**
- CXF 공식 문서: [https://cxf.apache.org/docs/](https://cxf.apache.org/docs/)
- Apache Tomcat: [https://tomcat.apache.org/](https://tomcat.apache.org/)
- JBoss: [https://www.jboss.org/](https://www.jboss.org/)