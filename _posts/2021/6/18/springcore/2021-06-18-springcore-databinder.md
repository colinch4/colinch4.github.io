---
layout: post
title: "[springcore] 데이터 바인딩 추상화"
description: " "
date: 2021-06-18
tags: [springcore]
comments: true
share: true
---

## 데이터 바인딩 추상화

## PropertyEditor
- 프로퍼티 값을 타겟 객체에 설정하는 기능
- 사용자 입력값을 애플리케이션 도메인 모델에 동적으로 변환하여 넣어주는 기능
- 스프링 3.0 이전까지 DataBinder가 변환 작업 사용하던 인터페이스
- 스레드-세이프 하지 않음(상태 정보 저장)
- Object와 String간의 변환만 할 수 있어, 사용 범위가 제한적임
- `PropertyEditor` 인터페이스를 직접 구현해도 되지만 구현해야 할 메소드가 많으므로 `PropertyEditorSupport`를 상속받아 사용하는 것을 추천
```java
public class EventPropertyEditor extends PropertyEditorSupport {
    @Override
    public String getAsText() {
        return ((Event)getValue()).getTitle();
    }

    @Override
    public void setAsText(String text) throws IllegalArgumentException {
        int id = Integer.parseInt(text);
        Event event = new Event();
        event.setId(id);
        setValue(event);
    }
}
```
- `Controller`에 `@InitBinder`를 통해 등록시켜 사용할 수 있음
```java
@InitBinder
public void init(WebDeataBinder webDataBinder) {
    webDataBinder.registerCustomEditor(Event.class, new EventEditor());
}
```

## Converter
- `PropertyEditor`는 스레드-세이프 하지 않기 때문에 최근에는 `Converter/Formatter`를 많이 사용
- `ConverterRegistry`에 등록하여 사용
- Converter 예제
```java
public class EventConverter {

    public static class StringToEventConverter implements Converter<String, Event> {
        @Override
        public Event convert(String source) {
            Event event = new Event();
            event.setId(Integer.parseInt(source));
            return event;
        }
    }

    public static class EventToStringConverter implements Converter<Event, String> {
        @Override
        public Event convert(Event source) {
            return source.getId().toString();
        }
    }
}
```
- Spring Boot에서는 Bean으로 등록되어 있으면 registry에 자동 등록시켜 줌
- Spring Boot가 아닌 Web MVC로 구현된 스프링에서는 아래와 같이 등록시켜줘야 함
```java
@Configuration
public class WebConfig implements WebConfigurer {
    @Override
    public void addFormatters(FormatterRegistry registry) {
        registry.addConverter(new EventConverter.StringToEventConverter());
    }
}
```

## Formatter
- `PropertyEditor`를 대체하여 사용
- Object와 String 간의 변환을 담당
- Locale에 따라 다국어 기능도 제공
- `FormatterRegistry`에 등록하여 사용
```java
public class EventFormatter implements Formatter<Event> {
    @Override
    public Event parse(String text, Locale locale) throws ParseException {
        Event event = new Event();
        int id = Integer.parseInt(text);
        event.setId(id);
        return event;
    }

    @Override
    public String print(Event object, Locale locale) {
        return object.getId().toString();
    }
}
```
- `Converter`와 마찬가지로 Spring Boot환경이 아니라면 등록시켜줘야 함
```java
@Configuration
public class WebConfig implements WebConfigurer {
    @Override
    public void addFormatters(FormatterRegistry registry) {
        registry.addFormatter(new EventFormatter());
    }
}
```

## ConversionService
- 실제 변환 작업은 이 인터페이스를 통해 스레드-세이프하게 사용할 수 있음
- Spring MVC, Bean(value)설정, SpEL에서 사용
- `DefaultFormattingConversionService`는 `ConversionService`와 `FormatterRegistry`를 상속받아 구현되어 있고, `FormatterRegistry`는 `ConverterRegistry`를 상속받음
- 따라서 `FormatterRegistry`에서도 `Converter`를 등록 시켜줄 수 있음
- `DefaultFormattingConversionService`는 여러 기본 `Converter`와 `Formatter`를 등록시켜 줌
- Spring Boot에 경우 `DefaultFormattingConversionService`를 상속하여 구현한 `WebConversionService`를 Bean으로 등록시켜 줌

