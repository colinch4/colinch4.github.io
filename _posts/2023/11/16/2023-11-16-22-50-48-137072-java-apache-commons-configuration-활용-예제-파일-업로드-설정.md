---
layout: post
title: "[java] Java Apache Commons Configuration 활용 예제: 파일 업로드 설정"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

이번 예제에서는 Java 언어로 Apache Commons Configuration 라이브러리를 사용하여 파일 업로드 설정을 구현하는 방법을 살펴보겠습니다.

## Apache Commons Configuration 이란?

Apache Commons Configuration은 Apache 기반의 설정 라이브러리로, 프로퍼티 파일, XML 파일, INI 파일 등 다양한 형식의 설정 파일을 읽고 쓰는 기능을 제공합니다. 이를 통해 설정 값을 손쉽게 관리할 수 있습니다.

## 파일 업로드 설정 구현 예제

다음은 Apache Commons Configuration을 사용하여 파일 업로드 설정을 구현하는 예제 코드입니다.

```java
import org.apache.commons.configuration.Configuration;
import org.apache.commons.configuration.ConfigurationException;
import org.apache.commons.configuration.PropertiesConfiguration;

public class FileUploadConfigExample {

    private static final String CONFIG_FILE = "fileupload.properties";
    private static final String MAX_FILE_SIZE_KEY = "fileupload.maxfilesize";
    private static final String ALLOWED_EXTENSIONS_KEY = "fileupload.allowedextensions";

    private Configuration config;

    public FileUploadConfigExample() {
        try {
            config = new PropertiesConfiguration(CONFIG_FILE);
        } catch (ConfigurationException e) {
            e.printStackTrace();
        }
    }

    public long getMaxFileSize() {
        return config.getLong(MAX_FILE_SIZE_KEY);
    }

    public String[] getAllowedExtensions() {
        return config.getStringArray(ALLOWED_EXTENSIONS_KEY);
    }

    public static void main(String[] args) {
        FileUploadConfigExample example = new FileUploadConfigExample();
        long maxFileSize = example.getMaxFileSize();
        String[] allowedExtensions = example.getAllowedExtensions();

        System.out.println("Max File Size: " + maxFileSize);
        System.out.println("Allowed Extensions: " + Arrays.toString(allowedExtensions));
    }
}
```

위의 코드는 `fileupload.properties` 파일에서 `fileupload.maxfilesize`와 `fileupload.allowedextensions`의 값을 읽어오는 예제입니다. 예제에서는 `PropertiesConfiguration` 객체를 사용하여 파일을 읽어오고 설정 값을 가져올 수 있습니다.

## 설정 파일 예제(fileupload.properties)

```
fileupload.maxfilesize = 10485760
fileupload.allowedextensions = jpg,png,gif
```

위의 설정 파일은 파일 업로드에 관련된 최대 파일 크기와 허용되는 확장자 목록을 정의하고 있습니다.

이제 위의 예제 코드를 실행하면 설정 파일에서 값을 읽어와서 콘솔에 출력하게 됩니다. 예제의 출력 결과는 다음과 같을 것입니다:

```
Max File Size: 10485760
Allowed Extensions: [jpg, png, gif]
```

위의 예제를 기반으로 파일 업로드 설정을 손쉽게 관리할 수 있습니다.

## 결론

이번 포스트에서는 Java 언어에서 Apache Commons Configuration을 활용하여 파일 업로드 설정을 구현하는 방법을 알아보았습니다. Apache Commons Configuration을 사용하면 다양한 형식의 설정 파일을 쉽게 읽고 쓸 수 있으므로, 설정 관리를 효율적으로 할 수 있습니다. Apache Commons Configuration은 다양한 설정 관리 시나리오에 유용하게 사용될 수 있습니다.

## 참고 자료

- [Apache Commons Configuration 공식 홈페이지](https://commons.apache.org/proper/commons-configuration/)
- [Apache Commons Configuration GitHub 저장소](https://github.com/apache/commons-configuration)