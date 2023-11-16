---
layout: post
title: "[java] SnakeYAML을 사용하여 YAML 파일의 timestamp 데이터 처리하기"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

YAML은 인간이 읽고 쓰기에 편리한 데이터 직렬화 형식입니다. SnakeYAML은 Java에서 YAML 파일을 처리하는 라이브러리 중 하나로서, YAML 파일을 파싱하고 객체로 변환하는 기능을 제공합니다.

SnakeYAML을 사용하여 YAML 파일을 다룰 때, 때로는 timestamp 데이터를 처리해야 할 수도 있습니다. Timestamp는 날짜와 시간 정보를 포함하는 데이터 유형이며, SnakeYAML은 이를 자동으로 파싱하여 Java의 `java.util.Date` 객체로 변환합니다.

다음은 SnakeYAML을 사용하여 YAML 파일에서 timestamp 데이터를 처리하는 예시 코드입니다.

```java
import org.yaml.snakeyaml.Yaml;
import java.io.FileReader;
import java.util.Map;

public class YamlParser {
    public static void main(String[] args) {
        Yaml yaml = new Yaml();

        try (FileReader fileReader = new FileReader("example.yaml")) {
            // YAML 파일을 읽어옴
            Object yamlObject = yaml.load(fileReader);

            if (yamlObject instanceof Map) {
                Map<String, Object> yamlMap = (Map<String, Object>) yamlObject;
                // YAML 파일에서 timestamp 데이터 가져오기
                Object timestamp = yamlMap.get("timestamp");

                if (timestamp instanceof java.util.Date) {
                    // timestamp를 자유롭게 처리하는 로직 작성
                    java.util.Date date = (java.util.Date) timestamp;
                    // 예시: timestamp를 문자열로 변환하여 출력
                    System.out.println("Timestamp: " + date.toString());
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

예시 코드에서는 `example.yaml` 파일로부터 YAML 데이터를 읽어옵니다. YAML 파일의 `timestamp` 필드를 `java.util.Date` 객체로 변환하여 처리하는 부분을 확인할 수 있습니다. 이 예시에서는 단순히 timestamp를 문자열로 변환하여 출력합니다.

SnakeYAML을 사용하여 YAML 파일의 timestamp 데이터를 처리하는 방법에 대한 예시를 제공했습니다. SnakeYAML에 대한 자세한 사용법은 SnakeYAML 공식 문서를 참고하시기 바랍니다.

참고 문서: [SnakeYAML 공식 문서](https://bitbucket.org/asomov/snakeyaml/src/master/)