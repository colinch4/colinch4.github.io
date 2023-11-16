---
layout: post
title: "[java] Java Apache Commons Configuration 활용 예제: 퀘스트 설정"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Java Apache Commons Configuration은 Java 애플리케이션에서 속성 파일이나 XML 파일과 같은 설정 파일을 읽어들이고 사용할 수 있는 유용한 라이브러리입니다. 이 예제에서는 Apache Commons Configuration을 사용하여 간단한 퀘스트 게임의 설정을 로드하는 방법을 살펴보겠습니다.

## 1. Apache Commons Configuration 라이브러리 추가하기

프로젝트의 build.gradle 파일에 아래의 의존성을 추가하여 Apache Commons Configuration 라이브러리를 프로젝트에 추가합니다.

```groovy
dependencies {
    implementation 'org.apache.commons:commons-configuration2:2.7'
}
```

## 2. 설정 파일 생성하기

퀘스트 게임의 설정을 저장할 properties 파일을 생성합니다. 예를 들어, quest.properties 파일을 아래와 같이 작성합니다.

```properties
quest.name=The Great Adventure
quest.difficulty=Medium
quest.reward=100
```

## 3. 설정 파일 로드하기

Java 코드에서 Apache Commons Configuration을 사용하여 설정 파일을 로드합니다. 아래의 예제 코드를 참고하세요.

```java
import org.apache.commons.configuration2.Configuration;
import org.apache.commons.configuration2.builder.FileBasedConfigurationBuilder;
import org.apache.commons.configuration2.builder.FileBasedConfigurationBuilderSupplier;
import org.apache.commons.configuration2.builder.fluent.FileBasedBuilderParameters;
import org.apache.commons.configuration2.builder.fluent.Parameters;
import org.apache.commons.configuration2.ex.ConfigurationException;

public class QuestConfiguration {
    public static void main(String[] args) {
        try {
            Parameters params = new Parameters();
            FileBasedBuilderParameters fileParams = params.fileBased().setFileName("quest.properties");
            FileBasedConfigurationBuilder<PropertiesConfiguration> builder = new FileBasedConfigurationBuilder<>(PropertiesConfiguration.class)
                    .configure(fileParams);

            Configuration config = builder.getConfiguration();

            String questName = config.getString("quest.name");
            String questDifficulty = config.getString("quest.difficulty");
            int questReward = config.getInt("quest.reward");

            System.out.println("Quest Name: " + questName);
            System.out.println("Quest Difficulty: " + questDifficulty);
            System.out.println("Quest Reward: " + questReward);
        } catch (ConfigurationException e) {
            e.printStackTrace();
        }
    }
}
```

## 4. 설정 값 사용하기

위의 예제 코드에서는 설정 파일에서 로드한 값들을 변수에 저장하고 콘솔에 출력하는 예제입니다. 실제 애플리케이션에서는 이러한 설정 값들을 필요에 따라 사용할 수 있습니다.

## 마무리

Java Apache Commons Configuration을 사용하여 설정 파일을 로드하는 예제를 살펴보았습니다. 이를 통해 애플리케이션의 설정을 외부 파일에서 관리하고 쉽게 변경할 수 있습니다. Apache Commons Configuration은 다양한 설정 파일 형식을 지원하므로 필요에 따라 XML, JSON 등의 형식으로 설정 파일을 작성할 수도 있습니다.

**참고 자료:**

- [Apache Commons Configuration 공식 문서](https://commons.apache.org/proper/commons-configuration/)
- [Java Properties 파일 다루기](https://www.baeldung.com/java-properties)