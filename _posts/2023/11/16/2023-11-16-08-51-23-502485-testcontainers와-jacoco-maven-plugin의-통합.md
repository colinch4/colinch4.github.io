---
layout: post
title: "[java] TestContainers와 Jacoco Maven Plugin의 통합"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

TestContainers와 Jacoco Maven Plugin은 개발자들에게 테스트 컨테이너를 사용하여 애플리케이션을 테스트하는 강력하고 편리한 방법을 제공합니다. 테스트 컨테이너는 독립적인 환경에서 애플리케이션의 통합 및 인수 테스트를 가능하게 해주는 도구입니다. Jacoco Maven Plugin은 Jacoco를 사용하여 코드 커버리지를 측정하고 리포트를 생성하는 데 사용됩니다.

이번 글에서는 TestContainers와 Jacoco Maven Plugin을 함께 사용하는 방법을 알아보겠습니다. 이를 통해 애플리케이션의 테스트 커버리지를 정확하게 측정하고 리포트를 생성할 수 있습니다.

## 1. TestContainers 설정

먼저, 테스트 컨테이너를 설정해야 합니다. 아래는 PostgreSQL 데이터베이스를 사용하는 경우의 예시입니다. 

```java
@Testcontainers
public class MyIntegrationTest {

    @Container
    private final PostgreSQLContainer<?> postgresqlContainer = new PostgreSQLContainer<>("postgres:latest");

    // 테스트 코드 작성
}
```
위의 예시에서는 `@Testcontainers` 어노테이션을 사용하여 테스트 컨테이너를 활성화시킵니다. `@Container` 어노테이션을 사용하여 TestingContainers에서 제공하는 PostgreSQL 컨테이너를 생성하고 사용할 수 있습니다.

## 2. Jacoco Maven Plugin 설정

다음으로, Jacoco Maven Plugin을 설정해야 합니다. `pom.xml` 파일에 아래와 같이 추가합니다.

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.jacoco</groupId>
            <artifactId>jacoco-maven-plugin</artifactId>
            <version>0.8.7</version>
            <executions>
                <execution>
                    <id>prepare-agent</id>
                    <goals>
                        <goal>prepare-agent</goal>
                    </goals>
                </execution>
                <execution>
                    <id>report</id>
                    <phase>test</phase>
                    <goals>
                        <goal>report</goal>
                    </goals>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```
위의 설정은 Jacoco Maven Plugin을 추가하고 테스트를 실행할 때 코드 커버리지 리포트를 생성하도록 설정합니다. `prepare-agent` goal은 테스트를 실행하기 전에 Jacoco 에이전트를 실행하고, `report` goal은 테스트가 완료된 후에 리포트를 생성합니다.

## 3. 테스트 실행과 코드 커버리지 리포트 생성

이제 위의 설정이 완료되었으므로 테스트를 실행하고 코드 커버리지 리포트를 생성할 수 있습니다. Maven 명령어를 통해 테스트와 리포트 생성을 수행합니다.

```bash
mvn clean test
```

위 명령어를 실행하면 테스트가 실행되고 테스트 컨테이너가 자동으로 생성됩니다. 그리고 Jacoco Maven Plugin이 테스트 커버리지를 측정하고 리포트를 생성합니다. 생성된 리포트는 `target/site/jacoco/index.html` 경로에 저장됩니다.

## 결론

TestContainers와 Jacoco Maven Plugin의 통합을 통해 테스트 컨테이너를 활용하여 애플리케이션을 테스트하고 코드 커버리지를 정확하게 측정할 수 있습니다. 이를 통해 개발자는 테스트 방식을 고려하고 애플리케이션의 품질을 높일 수 있습니다.

- [TestContainers](https://www.testcontainers.org/)
- [Jacoco Maven Plugin](https://www.eclemma.org/jacoco/trunk/doc/maven.html)