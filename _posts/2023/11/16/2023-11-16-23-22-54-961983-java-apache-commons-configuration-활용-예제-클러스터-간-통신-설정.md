---
layout: post
title: "[java] Java Apache Commons Configuration 활용 예제: 클러스터 간 통신 설정"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Apache Commons Configuration은 Java 어플리케이션에서 속성 파일, XML 파일, 데이터베이스 등 다양한 소스로부터 설정 정보를 로드하고 파싱하는 기능을 제공하는 라이브러리입니다. 이번 예제에서는 Apache Commons Configuration을 사용하여 클러스터 간의 통신 설정을 다루는 방법에 대해 알아보겠습니다.

해당 예제를 구현하기 위해서는 먼저 Apache Commons Configuration 라이브러리를 프로젝트에 추가해야 합니다. Maven을 사용하는 경우, `pom.xml` 파일에 다음 의존성을 추가합니다:

```xml
<dependencies>
    <dependency>
        <groupId>org.apache.commons</groupId>
        <artifactId>commons-configuration2</artifactId>
        <version>2.7</version>
    </dependency>
</dependencies>
```

다음으로, 설정 정보를 저장할 `config.properties` 파일을 생성합니다. 이 파일을 사용하여 클러스터 간의 통신 설정을 관리할 것입니다. 파일 내용은 아래와 같습니다:

```properties
cluster.name=myCluster
cluster.ip=192.168.0.1
cluster.port=8080
```

이제 Java 코드로 Apache Commons Configuration을 사용하여 설정 정보를 로드하고 활용하는 예제를 작성해보겠습니다:

```java
import org.apache.commons.configuration2.Configuration;
import org.apache.commons.configuration2.builder.FileBasedConfigurationBuilder;
import org.apache.commons.configuration2.builder.fluent.Parameters;

public class ClusterConfiguration {
    private static final String CONFIG_FILE = "config.properties";

    public static void main(String[] args) {
        try {
            Parameters params = new Parameters();
            FileBasedConfigurationBuilder<PropertiesConfiguration> builder =
                    new FileBasedConfigurationBuilder<>(PropertiesConfiguration.class)
                            .configure(params.fileBased().setFileName(CONFIG_FILE));

            Configuration config = builder.getConfiguration();

            String clusterName = config.getString("cluster.name");
            String clusterIp = config.getString("cluster.ip");
            int clusterPort = config.getInt("cluster.port");

            System.out.println("Cluster Name: " + clusterName);
            System.out.println("Cluster IP: " + clusterIp);
            System.out.println("Cluster Port: " + clusterPort);
        } catch (ConfigurationException e) {
            e.printStackTrace();
        }
    }
}
```

위 예제 코드에서는 `config.properties` 파일을 로드하고, `cluster.name`, `cluster.ip`, `cluster.port` 세 개의 속성을 읽어와 출력하는 예제입니다. 이렇게 읽어온 설정 정보를 통해 클러스터 간의 통신을 설정할 수 있습니다.

이를 실행해보면 아래와 같은 결과를 볼 수 있습니다:

```
Cluster Name: myCluster
Cluster IP: 192.168.0.1
Cluster Port: 8080
```

Apache Commons Configuration을 사용하면 속성 파일이나 XML 파일과 같은 외부 설정 파일을 간편하게 로드하고 파싱할 수 있으므로, Java 어플리케이션의 설정 관리를 효율적으로 할 수 있습니다.

참고 자료:
- [Apache Commons Configuration Documentation](https://commons.apache.org/proper/commons-configuration/)
- [Apache Commons Configuration GitHub Repository](https://github.com/apache/commons-configuration)