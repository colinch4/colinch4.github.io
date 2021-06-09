---
layout: post
title: "[Java8] 새로운 날짜와 시간 API"
description: " "
date: 2021-06-09
tags: [Java8]
comments: true
share: true
---

새로운 날짜와 시간 API
----------------------

### LocalDate, LocalTime, Instant, Duration, Period

#### LocalDate와 LocalTime 사용

-	LocalDate 인스턴스는 시간을 제외한 날짜를 표현하는 불변 객체다.

```java
LocalDate date = LocalDate.of(2014, 3, 18);
int year = date.getYear(); // 2014
Month month = date.getMonth(); // MARCH
int day = date.getDayOfMonth(); // 18
DayOfWeek dow = date.getDayOfWeek(); // TUESDAY
int len = date.lengthOfMonth(); // 31 (days in March)
boolean leap = date.isLeapYear(); // false (not a leap year)
System.out.println(date);

int y = date.get(ChronoField.YEAR);
int m = date.get(ChronoField.MONTH_OF_YEAR);
int d = date.get(ChronoField.DAY_OF_MONTH);
```

-	시간은 LocalTime 클래스로 표현할 수 있다.

```java
LocalTime time = LocalTime.of(13, 45, 20); // 13:45:20
int hour = time.getHour(); // 13
int minute = time.getMinute(); // 45
int second = time.getSecond(); // 20
System.out.println(time);
```

-	날짜와 시간 문자열로 LocalDate와 LocalTime의 인스턴스를 만드는 방법도 있다.

```java
LocalDate date = LocalDate.parse("2014-03-18");
LocalTime time = LocalTime.parse("13:45:20");
```

#### 날짜와 시간 조합

-	`LocalDateTime`은 LocalDate와 LocalTime을 쌍으로 갖는 복합 클래스이다.

```java
LocalDateTime dt1 = LocalDateTime.of(2014, Month.MARCH, 18, 13, 45, 20); // 2014-03-18T13:45
LocalDateTime dt2 = LocalDateTime.of(date, time);
LocalDateTime dt3 = date.atTime(13, 45, 20);
LocalDateTime dt4 = date.atTime(time);
LocalDateTime dt5 = time.atDate(date);
System.out.println(dt1);
```

#### Instant: 기계의 날짜와 시간

-	Instant 클래스는 유닉스 에포크시간을 기준으로 특정 지점까지의 시간을 초로 표현한다.

```java
Instant instant = Instant.ofEpochSecond(44 * 365 * 86400);
Instant now = Instant.now();
```

#### Duration과 Period 정의

-	Duration 클래스의 정적 팩토리 메서드 between으로 두 시간 객체 사이의 `지속시간`을 만들 수 있다.

```java
Duration d1 = Duration.between(LocalTime.of(13, 45, 10), time);
Duration d2 = Duration.between(instant, now);
System.out.println(d1.getSeconds());
System.out.println(d2.getSeconds());
// 단 LocalDateTime은 사람이 사용하도록, Instant는 기계가 사용하도록 만들어진 클래스로 같이 사용할 수는 없다.
```

-	Period 클래스의 팩토리 메서드 between을 이용하면 두 LocalDate의 차이를 확인할 수 있다.

```java
Period tenDays = Period.between(LocalDate.of(2014, 3, 8), LocalDate.of(2014, 3, 18));
```

-	Duration과 Period 클래스가 공통으로 제공하는 메서드

![Duration과 Period 클래스가 공통으로 제공하는 메서드](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzei1DODh5ZGVPdjA)

### 날짜 조정, 파싱, 포매팅

-	withAttribute 메서드로 기존 LocalDate를 바꿀 수 있다.

```java
LocalDate date = LocalDate.of(2014, 3, 18);
date = date.withYear(2017);
date = date.withDayOfMonth(25);
date = date.with(ChronoField.MONTH_OF_YEAR);
```

-	지정된 시간을 추가하거나 뺄 수 있다.

```java
LocalDate date1 = LocalDate.of(2014, 3, 18);
// 2017-05-03
LocalDate date2 = date1.plusWeeks(1);
// 2017-05-10
LocalDate date3 = date2.minusYears(3);
// 2014-05-10
LocalDate date4 = date3.plus(6, ChronoUnit.MONTHS);
// 2014-11-10
```

-	특정 시점을 표현하는 날짜 시간 클래스의 공통 메서드

![특정 시점을 표현하는 날짜 시간 클래스의 공통 메서드](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzcWdpSUJmRXZIZzQ)

#### TemporalAdjusters 사용하기

-	때로는 다음 주 일요일, 돌아오는 평일, 어떤 달의 마지막 날 등 좀 더 복잡한 날짜 조정 기능이 필요할 것이다. 이때는 오버로드된 버전의 with 메소드에 좀 더 다양한 동작을 수행할 수 있도록 하는 기능이 제공하는 TemporalAdjusters에서 정의하는 정적 팩토리 메서드로 이들 기능을 이용할 수 있다.

```java
import static java.time.temporal.TemporalAdjusters.*;
LocalDate date1 = LocalDate.of(2014, 3, 18);
// 2014-03-18
LocalDate date2 = date1.with(nextOrSame(DayOfWeek.SUNDAY));
// 2014-03-23
LocalDate date3 = date2.with(lastDayOfMonth());
// 2014-03-31
```

![TemporalAdjusters 클래스의 팩토리 메서드](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzZE1jYjhpU0kybmM)

-	커스텀 TemporalAdjusters 구현하기

```java
date = date.with(temporal -> {
    DayOfWeek dow = DayOfWeek.of(temporal.get(ChronoField.DAY_OF_WEEK));
    int dayToAdd = 1;
    if (dow == DayOfWeek.FRIDAY) dayToAdd = 3;
    if (dow == DayOfWeek.SATURDAY) dayToAdd = 2;
    return temporal.plus(dayToAdd, ChronoUnit.DAYS);
});
```

#### 날짜와 시간 객체 출력과 파싱

-	DateTimeFormatter를 이용해서 날짜나 시간을 특정 형식의 문자열로 만들 수 있다.

```java
LocalDate date = LocalDate.of(2014, 3, 18);
String sl = date.format(DateTimeFormatter.BASIC_ISO_DATE);
// 20140318
String s2 = date.format(DateTimeFormatter.ISO_LOCAL_DATE);
// 2014-03-18
```

-	반대로 날짜나 시간을 표현하는 문자열을 파싱해서 날짜 객체를 다시 만들 수 있다.

```java
LocalDate date1 = LocalDate.parse("20140318", DateTimeFormatter.BASIC_ISO_DATE);
LocalDate date2 = LocalDate.parse("2014-03-18", DateTimeFormatter.ISO_LOCAL_DATE);
```

-	특정 패턴으로 포매터를 만들 수 있는 정적 팩토리 메소드 제공.

```java
DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy");
LocalDate date1 = LocalDate.of(2014, 3, 18);
String formattedDate = date1.format(formatter);
LocalDate date2 = LocalDate.parse(formattedDate, formatter);
```

### 다양한 시간대와 캘린더 활용 방법

-	기존의 java.util.TimeZone을 대체할 수 있는 java.util.ZoneId 클래스가 새롭게 등장했다.

```java
// 새롭게 등장한 Zoneld
Zoneld romeZone = Zoneld.of("EuropejRome");
// 기존의 TimeZone -> Zoneld로 변경 가능
Zoneld zoneld = TimeZone.getDefault().toZoneld();

LocalDate date = LocalDate.of(2014, Month.MARCH, 18);
ZonedDateTime zdt1 = date.atStartOfDay(romeZone);

LocalDateTime dateTime = LocalDateTime .of(2014, Month.MARCH , 18, 13, 45);
ZonedDateTime zdt2 = dateTime.atZone(romeZone);

Instant instant = Instant.now();
ZonedDateTime zdt3 = instant .atZone(romeZone);
```

![ZonedDateTime](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzM2luMGtsT2JrVW8)

### 요약

-	자바 8 이전 버전에서 제공하는 기존의 java.util.Date 클래스와 관련 클래스에서는 여러 불일치점들과 가변성, 어설픈 오프셋, 기본값, 잘못된 이름 결정 등의 설계 결함이 존재했다.
-	새로운 날짜와 시간 API에서 날짜와 객체는 모두 불변이다.
-	새로운 API는 각각 사람과 기계가 편리하게 날짜와 시간 정보를 관리할 있도록 두 가지 표현 방식을 제공한다.
-	날짜와 시간 객체를 절대적인 방법과 상대적인 방법으로 처리할 수 있으며 기존 인스턴스를 변환하지 않도록 처리 결과로 새로운 인스턴스가 생성된다.
-	TemporalAdjusters를 이용하면 단순히 값을 바꾸는 것 이상의 복잡한 동작을 수행할 수 있으며 자신만의 커스텀 날짜 변환 기능을 정의할 수 있다.
-	날짜와 시간 객체를 특정 포맷으로 출력하고 파싱하는 포매터를 정의할 수 있다. 패턴을 이용하거나 프로그램으로 포매터를 만들 수 있으며 포매터는 스레드 안정성을 보장한다.
-	특정 지역/장소에 상대적인 시간대 또는 UTC/GMT 시준의 오프셋을 이용해서 시간대를 정의할 수 있으며 이 시간대를 날짜와 시간 객체에 적용해서 지역화할 수 있다.
-	ISO-8601 표준 시스템을 준수하지 않는 캘린더 시스템도 사용할 수 있다.
