---
layout: post
title: "[springcore] MessageSource"
description: " "
date: 2021-06-18
tags: [springcore]
comments: true
share: true
---

## MessageSource
- 국제화(i18n) 기능 제공 인터페이스
- 스프링 부트를 사용하면 별다른 설정없이 `message.properties`로 사용 가능
- 다른 언어의 메세지를 설정하려면 `message_언어_properties`로 가능
    - message_ko_KR.properties
- 예제
    - message.properties
    ```properties
    test=Hello, {0}
    ```
    - message_ko_KR.properties
    ```properties
    test=안녕, {0}
    ```
    - DemoAppRunner.java
    ```java
    @Component
    public class DemoAppRunner implements ApplicationRunner {
        @Autowired
        MessageSource messageSource;

        @Overrides
        public void run(ApplicationArguments args) {
            System.out.println(messageSource.getMessage("test", new String[]{"나야"}, Locale.KOREA));
            System.out.println(messageSource.getMessage("test", new String[]{"나야"}, Locale.getDefaultLocale()));
        }
    }
    ```    

- 리로드 가능한 `MessageSource` 설정
    - `MessageSource`를 재설정하여 가능
    - Bean 재정의
    ```java
    @Bean
    public MessageSource messageSource() {
        var messageSource = new ReloadableResourceBundleMessageSource();
        messageSource.setBasename("classpath:/messages");
        messageSource.setDefaultEncoding("UTF-8");
        messageSoruce.setCacheSeconds(3);

        return messageSource;
    }
    ```
    - while문으로 1초마다 한번씩 메시지 출력, properties를 수정하면 실시간으로 반영
    - DemoAppRunner.java
    ```java
    @Component
    public class DemoAppRunner implements ApplicationRunner {
        @Autowired
        MessageSource messageSource;

        @Overrides
        public void run(ApplicationArguments args) throws Exception {
            while(true) {
                System.out.println(messageSource.getMessage("test", new String[]{"나야"}, Locale.KOREA));
                System.out.println(messageSource.getMessage("test", new String[]{"나야"}, Locale.getDefaultLocale()));
                Thread.sleep(1000l);
            }
            
        }
    }
    ```
