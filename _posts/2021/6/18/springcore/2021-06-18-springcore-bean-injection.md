---
layout: post
title: "[springcore] 빈 주입 방법"
description: " "
date: 2021-06-18
tags: [springcore]
comments: true
share: true
---

## 빈 주입 방법
- 빈 주입 방법 2가지
	- @Autowired
	- setter 주입

## Autowired
- 해당 객체에 주입시킬 빈을 찾아 주입시켜줌
- `required` 속성의 기본값은 true, 따라서 빈을 찾지 못하면 오류 발생 (어플리케이션 구동 실패)
- 사용 할 수 있는 위치
	- 생성자(스프링4.3부터는 생략 가능)
	- setter
	- 필드
- 생성자 예제
```java
@Service
public class BookService {
	BookRepository bookRepository;
	
	@Autowired
	public void bookService(BookRepository bookRepository) {
			this.bookRepository = bookRepository;
	}
}
```
- setter 예제
```java
@Service
public class BookService {
	BookRepository bookRepository;
	
	@Autowired
	public void setBookRepository(BookRepository bookRepository) {
			this.bookRepository = bookRepository;
	}
}
```
- 필드 예제
```java
@Service
public class BookService {
	@Autowired
	BookRepository bookRepository;
}
```
- 빈 주입시 경우의 수
	- 해당 타입의 빈이 없는 경우 : 에러 (required=false사용 시 오류 안남. 빈 등록만 안됨)
	- 해당 타입의 빈이 한 개인 경우 : 주입
	- 해당 타입의 빈이 여러개인 경우
		1. 빈 이름으로 시도
		2. 같은 이름의 빈 찾으면 해당 빈 사용
		3. 같은 이름 못찾으면 실패 

- 같은 타입의 빈이 여러개 일때
	- `@Primary`를 붙이면 해당 객체를 주입 시키라는 의미
	- 해당 타입의 빈 모두 주입 받기
	- `@Qualifier`를 붙이면 빈 이름으로 주입시킬 수 있음

- BeanPostProcessor를 통해 새로 만든 빈 인스턴스를 수정할 수 있는 라이프 사이클 인터페이스 
```java
@PostConstruct
public void setup() {
	...생략
}
```

- AutowiredAnnotationBeanPostProcessor extends BeanPostProcessor
	- 스프링에서 제공하는 @Autowired, @Value, @Inject(JSR-330) 애노테이션을 지원하는 애노테이션 처리기

## @Component와 ComponentScan
- ComponentScan의 주요 기능
	- 스캔 기능 설정
	- 필터 : 어떤 애노테이션을 스캔 할지, 안할지
- ComponentScan예제 (패키지명)
```java
// com.juho.demo 하위에 있는 빈 등록
@ComponentScan(value = "com.juho.demo")
```
- 위의 방법은 타입 세이프하지 않아 버그를 유발. 아래와 같은 방법으로 변경 가능
```java
// DemoApplication.class위치의 하위에 있는 빈 등록
@ComponentScan(basePackages = DemoApplication.class)
```
- 필터를 사용하여 스캔하지 않을 파일 지정 가능
```java
@ComponentScan(excludeFilters = {
		@Filter(type = FilterType.CUSTOM, classes = TypeExcludeFilter.class),
		@Filter(type = FilterType.CUSTOM, classes = AutoConfigurationExcludeFilter.class) })
```

- @Component 목록. 아래의 애노테이션들 또한 Component이므로 빈으로 등록
	- @Repository
	- @Service
	- @Controller
	- @Configuration

- @ComponentScan은 스캔할 패키지와 애노테이션에 대한 정보
- 실제 스캐닝은 `ConfigurationClassPostProcessor`라는 `BeanFactoryPostProcessor`에 의해 처리

- 펑션을 사용하여 빈 등록 가능
```java
@SpringBootApplication
public class Demospring51Application {
    public static void main(String[] args) {
        SpringApplication app = new SpringApplication(Demospring51Application.class);
        app.addInitializers((ApplicationContextInitializer<GenericApplicationContext>) ctx -> ctx.registerBean(BookService.class));
        app.run(args);
    }
}
```