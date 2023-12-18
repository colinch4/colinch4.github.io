---
layout: post
title: "[php] 동적 변수(dynamic variable)와 정적 변수(static variable)의 비교"
description: " "
date: 2023-12-18
tags: [php]
comments: true
share: true
---

PHP에서 변수는 동적 변수와 정적 변수 두 가지 유형으로 나뉩니다. 이러한 유형 간의 차이점과 각각의 사용 사례에 대해 간단히 살펴보겠습니다.

### 동적 변수

동적 변수는 사용 시에 선언되며, **소문자로 시작하는 변수명**을 가집니다. 예를 들어:

```php
$name = "John";
$age = 25;
```

동적 변수는 실행 중에 동적으로 값이 할당되며 변경될 수 있습니다. 이러한 유연성은 변수 이름을 포함한 어플리케이션 로직을 동적으로 조작해야 하는 경우 유용합니다.

### 정적 변수

반면에, 정적 변수는 **클래스** 내에서 **static** 키워드를 사용하여 선언됩니다. 예를 들어:

```php
class User {
    public static $count = 0;

    public static function incrementCount() {
        self::$count++;
    }
}
```

정적 변수는 클래스의 모든 인스턴스에서 **공유**되며, 일반적으로 동일한 값을 유지하는 데 사용됩니다. 예를 들어, 위의 예제에서 User 클래스의 모든 인스턴스는 **$count** 변수를 공유하게 됩니다.

### 결론

동적 변수는 실행 중에 할당되고 변경될 수 있는 반면, 정적 변수는 클래스 또는 메소드 내에서 값을 유지하고 공유하는 데 사용됩니다. 적절한 상황에 맞게 동적 변수와 정적 변수를 사용하여 PHP 프로그램을 작성할 수 있습니다.

이것은 PHP에서 동적 변수와 정적 변수의 간단한 비교에 대한 것이며, 두 유형의 변수를 사용하는데 가장 적합한 사례에 대해서는 개발자의 상황에 따라 다를 수 있습니다.

### 참고 자료
- PHP 공식 문서: [Variables](https://www.php.net/manual/en/language.variables.php)