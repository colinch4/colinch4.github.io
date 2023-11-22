---
layout: post
title: "[springcore] 빈 설정 방법"
description: " "
date: 2021-06-18
tags: [spring]
comments: true
share: true
---

## 빈 설정 방법
- 빈 설정 방법 2가지
	- XML 설정
	- 자바 클래스 설정

## XML 설정 (고전적)
```xml
<!-- xml 설정파일 -->
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:context="http://www.springframework.org/schema/context"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context.xsd">

	<bean id="bookService" class="com.juho.springapplicationcontext.BookService">
	</bean>

	<bean id="bookRepository" class="com.juho.springapplicationcontext.BookRepository">
	</bean>
</bean>
```
- 위와 같이 설정하면 `bean`으로 등록
- @Autowired의 경우 애노테이션 붙은 객체가 빈으로 등록되어 있으면 알아서 주입시켜 주지만, setter 주입의 경우 `property`로 맵핑 시켜줘야 함
```xml
<!-- xml 설정파일 -->
... 생략
<bean id="bookService" class="com.juho.springapplicationcontext.BookService">
	<property name="bookRepository" ref="bookRepository" />
</bean>

<bean id="bookRepository" class="com.juho.springapplicationcontext.BookRepository">
</bean>
... 생략
```
```java
@Service
public class BookService {
    BookRepository bookRepository;

    public void setBookRepository(BookRepository bookRepository) {
        this.bookRepository = bookRepository;
    }
}
```
- XML로 설정한 내역을 토대로 빈을 가져오려면?
```java
public class DemoApplication {
    public static void main(String[] args) {
        ApplicationContext context = new ClassPathXmlApplicationContext("application.xml");
        String[] beanDefinitionNames = context.getBeanDefinitionNames();
        System.out.println(Arrays.toString(beanDefinitionNames));

        BookService bookService = (BookService) context.getBean("bookService");
        System.out.println(bookService.bookRepository != null);
    }
}
```
- `bean`이 많을 경우 일일이 등록하기 어려움
- 'componentScan`을 사용하면 해당 디렉토리 하위에 있는 모든 `@Component`를 `bean`으로 등록시켜줌 
- @Service, @Repository등 모두 @Component를 상속받아 구현한 애노테이션. 따라서 해당 애노테이션들도 `bean`으로 등록
```xml
<!-- xml 설정파일 -->
... 생략
<context:component-scan base-package="com.juho.springapplicationcontext"/>
... 생략
```

#### 자바 클래스 설정
- `@Configuration`을 붙이면 자바 객체도 설정파일로 사용할 수 있음
```java
@Configuration
public class ApplicationConfig {
    @Bean
    public BookRepository bookRepository() {
        return new BookRepository();
    }

    @Bean
    public BookService bookService() {
        BookService bookService = new BookService();
        bookService.setBookRepository(bookRepository());
        return bookService;
    }
}
```
- 해당 설정파일을 사용하려면
```java
public class DemoApplication {
    public static void main(String[] args) {
        ApplicationContext context = new AnnotationConfigApplicationContext(ApplicationConfig.class);
				
        String[] beanDefinitionNames = context.getBeanDefinitionNames();
        System.out.println(Arrays.toString(beanDefinitionNames));

        BookService bookService = (BookService) context.getBean("bookService");
        System.out.println(bookService.bookRepository != null);
    }
}
```
- 자바 객체에도 애노테이션을 사용하여 `componentScan`을 할 수 있음
```java
@Configuration
@ComponentScan(basePackageClasses = DemoApplication.class)
public class ApplicationConfig {
	...생략
```
- 특정 패키지를 지정할 수도 있지만 위와 같이 클래스를 지정하면 해당 클래스 하위에 있는 빈들을 등록시킨다는 의미