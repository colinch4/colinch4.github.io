---
layout: post
title: "[java] TestContainers로 Apache Ignite 애플리케이션 테스트하기"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Apache Ignite은 고성능 분산 인 메모리 컴퓨팅 플랫폼으로, 대규모 데이터 처리와 분석을 위한 기능을 제공합니다. 이를 활용하여 개발한 애플리케이션을 테스트하기 위해서는 실제 Ignite 클러스터가 필요합니다. 하지만 실제 클러스터를 구성하고 테스트하는 것은 번거로울 수 있습니다.

이런 경우, TestContainers를 사용하면 간편하게 Ignite 클러스터를 테스트 환경에서 실행할 수 있습니다. TestContainers는 도커 컨테이너를 사용하여 테스트 환경을 구성하므로, 별도의 클러스터 구성 과정이 필요하지 않습니다.

이번 포스트에서는 TestContainers를 사용하여 Apache Ignite 애플리케이션을 테스트하는 방법에 대해 알아보겠습니다.

## 1. TestContainers 설정

Apache Ignite를 사용하기 위해, 프로젝트의 의존성에 `ignite-core`를 추가해야 합니다. 또한 TestContainers에 대한 의존성인 `testcontainers`와 `testcontainers-ignite`도 추가해야 합니다. Maven을 사용하는 경우, pom.xml 파일에 다음과 같이 의존성을 추가할 수 있습니다.

```xml
<dependency>
    <groupId>org.apache.ignite</groupId>
    <artifactId>ignite-core</artifactId>
    <version>${ignite.version}</version>
    <scope>test</scope>
</dependency>

<dependency>
    <groupId>org.testcontainers</groupId>
    <artifactId>testcontainers</artifactId>
    <version>1.15.1</version>
    <scope>test</scope>
</dependency>

<dependency>
    <groupId>org.testcontainers</groupId>
    <artifactId>testcontainers-ignite</artifactId>
    <version>1.15.1</version>
    <scope>test</scope>
</dependency>
```

## 2. IgniteContainer 생성

Ignite를 테스트하기 위해 `IgniteContainer`를 사용합니다. `IgniteContainer`는 TestContainers의 일부로서, Ignite 클러스터를 실행하는 도커 컨테이너를 생성할 수 있습니다. 다음과 같이 `IgniteContainer`를 초기화합니다.

```java
@Container
private static GenericContainer igniteContainer = new IgniteContainer()
    .withClasspathResourceMapping("ignite-config.xml", "/opt/ignite/apache-ignite-2.10.0-bin/config/default-config.xml", BindMode.READ_ONLY);
```

위 코드에서 `ignite-config.xml` 파일은 Ignite 클러스터의 구성 파일로 사용됩니다. *withClasspathResourceMapping* 메서드를 사용하여 클래스 경로에 있는 파일을 도커 컨테이너 내의 경로로 매핑합니다.

## 3. 테스트 실행

이제 Ignite 클러스터가 실행되었으므로, 테스트를 실행할 수 있습니다. Ignite 클러스터에 접속하려면 Ignite 클라이언트를 사용해야 합니다. 다음은 Ignite 클라이언트를 초기화하는 예시 코드입니다.

```java
IgniteConfiguration config = new IgniteConfiguration();
config.setClientMode(true);
config.setAddresses(Collections.singletonList(igniteContainer.getTcpHostPorts()[0]));

try (Ignite ignite = Ignition.start(config)) {
    // Ignite 클러스터와 상호작용하는 테스트 로직 작성
    // ...
}
```

위 코드에서는 `IgniteConfiguration`을 생성하고, 클라이언트 모드로 설정하며, `igniteContainer.getTcpHostPorts()[0]`을 통해 Ignite 클러스터의 호스트 및 포트에 연결합니다.

테스트 로직 부분에는 실제 Ignite 클러스터와 상호작용하는 코드를 작성할 수 있습니다.

## 4. 테스트 종료

테스트가 종료되면 Ignite 클러스터를 정리하고 종료해야 합니다. TestContainers는 테스트 완료 후 컨테이너의 정리를 자동으로 처리합니다.

이로써 TestContainers를 사용하여 Apache Ignite 애플리케이션을 테스트하는 방법에 대해 알아보았습니다. TestContainers를 활용하면 간단하게 Ignite 클러스터를 구성하여 테스트할 수 있으므로, 개발 및 테스트 환경 구축에 편리함을 제공합니다.

더 자세한 정보는 아래 참고 자료를 확인해주세요.

- [Apache Ignite 홈페이지](https://ignite.apache.org/)
- [TestContainers 홈페이지](https://www.testcontainers.org/)
- [TestContainers GitHub 저장소](https://github.com/testcontainers/testcontainers-java)
- [TestContainers Ignite GitHub 저장소](https://github.com/testcontainers/testcontainers-java/tree/master/modules/ignite)