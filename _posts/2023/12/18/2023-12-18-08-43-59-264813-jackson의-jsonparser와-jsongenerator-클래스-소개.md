---
layout: post
title: "[java] Jackson의 JsonParser와 JsonGenerator 클래스 소개"
description: " "
date: 2023-12-18
tags: [java]
comments: true
share: true
---

Jackson은 Java에서 JSON을 다루는 데 사용되는 강력한 라이브러리입니다. 이 라이브러리에는 `JsonParser`와 `JsonGenerator` 클래스가 포함되어 있어 JSON 데이터를 읽고 쓰는 데 사용됩니다.

## JsonParser 클래스

`JsonParser` 클래스는 JSON 데이터를 읽을 때 사용됩니다. 이 클래스는 다음과 같은 메서드를 제공합니다.

- `nextToken()`: 다음 토큰을 읽습니다.
- `getText()`: 현재 토큰의 텍스트 값을 반환합니다.
- `getIntValue()`, `getDoubleValue()`, `getBooleanValue()`: 현재 토큰의 값을 해당하는 자료형으로 반환합니다.

다음은 `JsonParser` 클래스를 사용하여 JSON 데이터를 읽는 간단한 예제입니다.

```java
JsonFactory factory = new JsonFactory();
String jsonData = "{\"name\": \"John\", \"age\": 30}";
JsonParser parser = factory.createParser(jsonData);

while (parser.nextToken() != JsonToken.END_OBJECT) {
    String fieldname = parser.getCurrentName();
    parser.nextToken();
    if ("name".equals(fieldname)) {
        System.out.println("Name: " + parser.getText());
    } else if ("age".equals(fieldname)){
        System.out.println("Age: " + parser.getIntValue());
    }
}
parser.close();
```

## JsonGenerator 클래스

`JsonGenerator` 클래스는 JSON 데이터를 쓸 때 사용됩니다. 이 클래스는 다음과 같은 메서드를 제공합니다.

- `writeStartObject()`, `writeEndObject()`: 시작과 끝을 나타내는 객체 태그를 씁니다.
- `writeFieldName()`: 필드 이름을 씁니다.
- `writeString()`, `writeNumber()`, `writeBoolean()`: 문자열, 숫자, 논리값을 씁니다.
- `flush()`: 버퍼를 비웁니다.

다음은 `JsonGenerator` 클래스를 사용하여 JSON 데이터를 쓰는 간단한 예제입니다.

```java
JsonFactory factory = new JsonFactory();
StringWriter stringWriter = new StringWriter();
JsonGenerator generator = factory.createGenerator(stringWriter);

generator.writeStartObject();
generator.writeStringField("name", "John");
generator.writeNumberField("age", 30);
generator.writeEndObject();

generator.close();

String jsonData = stringWriter.toString();
System.out.println(jsonData);
```

`JsonParser`와 `JsonGenerator` 클래스를 사용하여 JSON 데이터를 쉽게 읽고 쓸 수 있습니다. Jackson 라이브러리는 다양한 JSON 처리 기능을 제공하여 개발 작업을 간편하게 만들어줍니다.

더 많은 정보는 [Jackson 공식 문서](https://github.com/FasterXML/jackson)를 참고하세요.