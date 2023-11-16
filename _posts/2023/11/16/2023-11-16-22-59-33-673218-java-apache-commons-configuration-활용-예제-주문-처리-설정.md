---
layout: post
title: "[java] Java Apache Commons Configuration 활용 예제: 주문 처리 설정"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

이 예제에서는 Java 언어 및 Apache Commons Configuration 라이브러리를 사용하여 주문 처리 설정을 구현하는 방법을 알아보겠습니다. Apache Commons Configuration은 설정 파일을 읽고 관리하는 데 사용되는 유용한 도구입니다.

## 필요한 의존성 추가

먼저 Maven을 사용하여 Apache Commons Configuration을 프로젝트에 추가해야 합니다. `pom.xml` 파일에 다음 의존성을 추가해주세요:

```xml
<dependencies>
    ...
    <dependency>
        <groupId>org.apache.commons</groupId>
        <artifactId>commons-configuration2</artifactId>
        <version>2.7</version>
    </dependency>
    ...
</dependencies>
```

의존성을 추가한 뒤 Maven을 업데이트하여 라이브러리를 다운로드하십시오.

## 설정 파일 작성

주문 처리 설정을 담은 설정 파일을 작성해야 합니다. 예를 들어서, `order.properties`라는 파일을 다음과 같이 작성해보겠습니다:

```properties
order.processing.enabled=true
order.processing.timeout=30
order.processing.max.retry=3
order.processing.discount=0.1
```

위의 설정 파일은 주문 처리를 활성화하고 타임아웃 시간을 30초로 설정하며, 최대 3번까지 재시도하고 할인율을 0.1로 설정합니다.

## 설정 파일 로딩 및 사용

이제 Java 코드에서 설정 파일을 로딩하고 사용하는 방법을 알아보겠습니다.

```java
import org.apache.commons.configuration2.Configuration;
import org.apache.commons.configuration2.PropertiesConfiguration;
import org.apache.commons.configuration2.ex.ConfigurationException;

public class OrderProcessingConfiguration {
    private static final String CONFIG_FILE = "order.properties";
    private Configuration configuration;

    public OrderProcessingConfiguration() throws ConfigurationException {
        configuration = new PropertiesConfiguration(CONFIG_FILE);
    }

    public boolean isOrderProcessingEnabled() {
        return configuration.getBoolean("order.processing.enabled");
    }

    public int getOrderProcessingTimeout() {
        return configuration.getInt("order.processing.timeout");
    }

    public int getMaxOrderProcessingRetry() {
        return configuration.getInt("order.processing.max.retry");
    }

    public double getOrderProcessingDiscount() {
        return configuration.getDouble("order.processing.discount");
    }
}
```

위의 코드에서는 `OrderProcessingConfiguration` 클래스가 주문 처리 설정 파일을 로딩하고 해당 설정 항목들을 사용할 수 있는 간단한 방법을 제공합니다. 주문 처리 설정의 각 항목은 해당하는 메서드를 사용하여 값을 가져올 수 있습니다.

```java
try {
    OrderProcessingConfiguration configuration = new OrderProcessingConfiguration();
    if (configuration.isOrderProcessingEnabled()) {
        int timeout = configuration.getOrderProcessingTimeout();
        int maxRetry = configuration.getMaxOrderProcessingRetry();
        double discount = configuration.getOrderProcessingDiscount();
        
        // 주문 처리 설정 값 활용
        // ...
    }
} catch (ConfigurationException e) {
    e.printStackTrace();
}
```

위의 예제에서는 주문 처리가 활성화된 경우 설정 값을 가져와서 주문 처리와 관련된 로직을 수행할 수 있습니다.

## 결론

이 예제에서는 Java 언어 및 Apache Commons Configuration 라이브러리를 사용하여 주문 처리 설정을 구현하는 방법을 알아보았습니다. Apache Commons Configuration은 설정 파일을 쉽게 로딩하고 관리할 수 있는 유용한 도구입니다. 이를 통해 설정 변경시 코드 수정 없이 설정 값을 변경할 수 있습니다.