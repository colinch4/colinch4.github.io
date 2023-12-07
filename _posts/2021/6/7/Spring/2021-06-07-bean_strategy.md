---
layout: post
title: "[spring] Bean 등록 메타정보 구성 전략"
description: " "
date: 2021-06-07
tags: [springboot]
comments: true
share: true
---

## 🍈 Bean 등록 메타정보 구성 전략 🥑

> - Spring 프레임워크에서 객체간의 의존성을 줄이고 유지보수를 더 쉽게하는 **DI(의존성 주입)** 을 실행 할 경우 크게 세 가지의 방법으로 수행가능
> - Bean을 등록하고 환경을 설정하는 방법에 따라 나눠짐

<br />

### 🤟 Bean 등록 및 메타정보를 구성하는 세 가지 전략

#### 1. XML 설정 단독 사용

#### 2. Annotation & XML 혼용

#### 3. Annotaion 단독 사용 (XML 사용 X)

<br><br>

### 1. XML 설정 단독 사용

> - 모든 Bean을 명시적으로 XML에 등록
> - 모든 Bean을 XML에서 확인 할 수 있으나, 객체가 많아질수록 관리가 어려워짐
> - 여러 개발자가 하나의 설정파일을 공유하여 동시 작업하는 경우 충돌 가능성이 높음
> - DI에 필요한 적절한 setter매소드 또는 Constructor가 코드내에 반드시 존재해야함

<br >

[XML 설정파일] spring_beans.xml

```xml
<!-- StringPrinter Class를 Beans로 등록 -->
<bean id="strPrinter" class= "myspring.di.xml.StringPrinter" ></bean>

<!-- HelloClass를 Beans로 등록 -->
<!-- Hello 클래스의 id를 주고, class로 클래스 위치를 전달 -->

<bean id="hello" class="myspring.di.xml.Hello" scope="singleton">

<!-- setName(), setPrinter() 매소드 => property로 설정 -->

    <!-- value는 값 전달 setName(value) == setName("spring")과 같은 기능-->
	<property name="name" value="spring" />
    <!-- ref는 strPrinter라는 id를 가진 bean을 참조한다는 뜻 -->
	<property name="printer" ref="strPrinter" />
</bean>
```

<br>

[Hello class] Hello.java

```java

public class Hello {
	String name;
	Printer printer;
	List<String> names;

	public Hello() {
		System.out.println("Hello ! defualt constructor called");
	}

	public Hello(String name, Printer printer) {
		System.out.println("Overloaded Hello Constructor called" +
	name + " " + printer.getClass().getName());

		this.name = name;
		this.printer = printer;
	}

	public void setName(String name) {
		System.out.println("Hello setName method called " + name);
		this.name = name;
	}

	public void setPrinter(Printer printer) {
		System.out.println("Hello setPrinter method called " +
	printer.getClass().getName());
		this.printer = printer;
	}

	public String sayHello() {
		return "Hello " + name;
	}

	public void print() {
		this.printer.print(sayHello());
	}

}
```

[StringPrinter Class] StringPrinter Class.java

```java
package myspring.di.xml;

public class StringPrinter implements Printer {
	private StringBuffer buffer = new StringBuffer();

	//print override
	public void print(String message) {
		this.buffer.append(message);
	}


	public String toString() {
		return this.buffer.toString();
	}


}
```

<br><br>

### 2. Annotation & XML 혼용

> - Bean으로 사용될 클래스에 특별한 Annotation을 부여해주면 클래스를 자동으로 찾아서 Bean으로 등록
> - @Component가 선언된 클래스를 자동으로 찾아서 Bean으로 등록해주는 **빈 스캐닝(Bean Scanning)** 을 통한 자동인식 Bean 기능
> - Annotation으로 빈 자동등록시 XML문서 생성과 관리의 수고를 덜고 개발속도 향상
> - Bean들을 한번에 볼 수 없고 의존관계를 한 눈에 파악하기 힘듬

<br>

**[Bean 등록 Annotation]**

| Annotation  | 기능                                                                                                                       |
| ----------- | -------------------------------------------------------------------------------------------------------------------------- |
| @Component  | - 컴포넌트를 나타내는 일반적인 스테레오 타입<br> - Bean 태그와 동일한역할                                                  |
| @Repository | - @Component와 같은 기능 <br> - Persistance 레이어 (DB연결 등) <br> - 영속성을 갖는 속성(파일, 데이터베이스)을 갖는 클래스 |
| @Service    | - 서비스 레이어, 비지니스 로직을 갖는 클래스                                                                               |
| @Controller | - 프레젠테이션 레이어 <br> - 웹 어플리케이션의 요청과 응답 처리                                                            |

<br >

**[의존관계 주입 Annotation]**

| Annotation                      | 기능                                                                                                                                                     |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| @Autowired                      | - 의존하는 객체 자동 주입 (타입으로 연결) <br> - 정밀한 의존관계주입이 필요한 경우 유용 <br > - 변수, setter매소드, 생성자, 일반 매소드에 모두 적용 가능 |
| @Resource                       | - 의존하는 객체 자동 주입 (이름으로 연결)<br > - 변수, setter매소드에 적용 가능                                                                          |
| @Value                          | - 단순한 값 주입시 사용                                                                                                                                  |
| @Qualifier                      | - @Autowired와 같이 사용 <br> - @Autowired가 타입으로 찾아서 주입하므로 동일한 타입의 특정 Bean객체를 지정해줄 때 사용                                   |
| `<context:component-scan>` 태그 | - @Component로 자동으로 빈 등록 후 @Autowired로 의존관계를 주입받는 클래스를 사용할 때 <br> - 클래스가 위치한 패키지를 명시해주기위해 사용               |

<br>

[XML 설정파일] spring_beans.xml

```xml
<!-- Component AutoScanning을 위한 설정 -->
<context:component-scan base-package="myspring.di.annotaion" />
```

[Hello class] Hello.java

```java
@Component("hello")
public class Hello {
    @Value("스프링")
    String name;

    @Autowired
    @Qualifier("stringPrinter")
    Printer printer;

	public void setName(String name) {
		System.out.println("Hello setName method called " + name);
		this.name = name;
	}

	public String sayHello() {
		return "Hello " + name;
	}

	public void print() {
		this.printer.print(sayHello());
	}

}
```

[StringPrinter Class] StringPrinter Class.java

```java
@Component("stringPrinter")
public class StringPrinter implements Printer {
	private StringBuffer buffer = new StringBuffer();

	//print override
	public void print(String message) {
		this.buffer.append(message);
	}


	public String toString() {
		return this.buffer.toString();
	}
}
```

<br><br>

### 3. Annotaion 단독 사용 (XML 사용 X)

> - Spring JavaConfig 프로젝트로 XML없이 자바 코드만으로 컨테이너 설정
> - **@Configuration**과 **@Bean**을 통해 스프링컨테이너에 빈 객체 제공 가능
> - Spring3.0 부터는 XML전혀 사용 X

<br>

**[Bean등록과 설정 Annotaion]**

| Annotaion      | 기능                                                                                                                                                                  |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| @Bean          | - 새로운 빈 객체 제공시 사용 <br> - @Bean이 적용된 매소드의 이름이 Bean의 ID가 됨 <br> - @Component와 같은 역할이나 @Component는 클래스위에, @Bean은 매소드 위에 선언 |
| @Configuration | - config Class 생성시 XML을 대체하는 역할 <br> - @Component처럼 빈 스캔으로 자동 검색됨 <br> - @Configuration을 선언한 클래스도 Bean으로 정의됨 (스프링 IoC로 인해)   |

<br>

[Hello class] Hello.java

```java
public class Hello{
    String name;
    Printer printer;

    public Hello(){
    }

    public void setName(String name){
        this.name = name
    }

    public void setPrinter(Printer printer){
        this.printer = printer;
    }

    public String sayHello(){
        return "Hello" + name;
    }

    public void print(){
        this.printer.print(sayHello());
    }
}
```

[HelloConfig class] HelloConfig.java

```java
@Configuration
public class HelloConfig{
    @Bean
    public Hello hello(){
        Hello hello = new Hello();
        hello.setName("자바 컨피그");
        hello.setPrinter(printer());
        return hello;
    }

    @Bean
    @Qualifiter("stringPrinter")
    public Printer priter(){
        Printer printer = new StringPrinter();
        return printer;
    }
    @Bean
    @Qaulifer("consolePrinter")
    public Printer cPrinter(){
        Printer printer = new ConsolePrinter();
        return printer;
    }
}

```

<br>

#### - Sprng-test에서 테스트를 지원하는 어노테이션: @ContextConfiguration

    - Bean의 메타 설정파일의 위치를 지정할 때 사용되는 어노테이션
    - 경로를 지정하지 않으면 테스트 클래스가 있는 패키지내에서 설정파일 사용

<br >

**[configuration과 componentScan]**

[XML을 @Configuration과 @ComponentScan으로 대체]

```xml
<!-- Component AutoScanning을 위한 설정 -->
<context:component-scan base-package="myspring.di.annotaion" />
```

```java
@Configuration
@ComponentScan(basePackages = {"myspring.di.annotaion"})
public class HelloBeanConfig {
}
```

<br >

#### - 프로퍼티 파일을 이용한 설정방법

> - 환경에 따라 자주 변경되는 내용을 분리하여 프로퍼티 파일에 따로 관리 (key= value)구조
> - XML에 저장되는 Bean 메타정보는 어플리케이션 구조가 바뀌지 않으면 바뀌지 않음
> - 하지만 프로퍼티 값으로 제공되는 일부 설정정보는 어플리케이션 동작환경에 따라 자주 바뀔수 있음

<br>

| Annotion        | 기능                                                       |
| --------------- | ---------------------------------------------------------- |
| @PropertySource | - .properties 파일 경로를 지정해줌 <br> - "classpath:경로" |

[values.propterties] 확장자 : .properties

```txt
myName = \uC5B4\uB178\uD14C\uC774\uC158\ \uC0DD\uC131\uC790
myPrinter = stringPrinterBean
configName = JAVA CONFIG
```

```java
@Configuration
@PropertySource("classpath:config/values.properties")
public class HelloConfig {
    //Enviorment import
	@Autowired
	private Environment env;

	@Bean
	public Hello hello() {
		Hello hello = new Hello();
		hello.setName(env.getProperty("configName"));
		hello.setPrinter(strPrinter());
		return hello;
	}
}
```
