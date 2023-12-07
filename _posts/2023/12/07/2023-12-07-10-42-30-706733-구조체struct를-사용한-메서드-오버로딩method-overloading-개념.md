---
layout: post
title: "[go] 구조체(struct)를 사용한 메서드 오버로딩(Method Overloading) 개념"
description: " "
date: 2023-12-07
tags: [go]
comments: true
share: true
---

메서드 오버로딩은 같은 이름의 메서드를 여러 개 정의하는 것을 의미합니다. 이때 오버로딩된 메서드들은 매개변수의 개수, 타입 또는 순서가 서로 다르게 정의됩니다. 구조체를 사용하여 메서드 오버로딩을 구현하는 방법에 대해 알아보겠습니다.

#### 구조체 정의하기
먼저 구조체를 정의해야 합니다. 구조체는 관련 데이터를 묶어서 하나의 단위로 사용하기 위한 자료형입니다. 다음은 구조체를 정의하는 예시입니다.

```go
type Rectangle struct {
	width  int
	height int
}
```

위의 예시에서는 `Rectangle`이라는 구조체를 정의하였습니다. 이 구조체에는 `width`와 `height`라는 두 개의 필드가 포함되어 있습니다.

#### 메서드 오버로딩 구현하기
이제 구조체에 메서드를 추가하여 오버로딩을 구현해보겠습니다. 아래의 예시에서는 `Area`라는 메서드를 구조체에 추가하는 예시입니다.

```go
func (r Rectangle) Area() int {
	return r.width * r.height
}

func (r Rectangle) Area(scale int) int {
	return r.width * r.height * scale
}
```

위의 예시에서는 `Area` 메서드를 두 개 정의하였습니다. 첫 번째 `Area` 메서드는 매개변수를 받지 않고, `width`와 `height`를 곱한 값을 반환합니다. 두 번째 `Area` 메서드는 `scale`이라는 매개변수를 받아 `width`와 `height`를 곱한 후 `scale`로 곱한 값을 반환합니다.

#### 메서드 호출하기
이제 메서드를 호출하는 방법에 대해 알아보겠습니다. 아래의 예시는 구조체의 인스턴스를 생성한 후 `Area` 메서드를 호출하는 예시입니다.

```go
func main() {
	rectangle := Rectangle{width: 10, height: 5}

	area := rectangle.Area()
	fmt.Println("Area:", area) // 출력: Area: 50

	areaWithScale := rectangle.Area(2)
	fmt.Println("Area with scale:", areaWithScale) // 출력: Area with scale: 100
}
```

위의 예시에서는 구조체의 인스턴스 `rectangle`을 생성한 후, `Area` 메서드를 호출하여 넓이를 계산하고 출력합니다. 첫 번째 호출에서는 매개변수를 받지 않는 `Area` 메서드가 호출되어 넓이를 계산하며, 두 번째 호출에서는 `2`라는 매개변수를 받는 `Area` 메서드가 호출되어 `scale`을 곱한 넓이를 계산합니다.

이처럼 구조체를 사용하여 메서드 오버로딩을 구현할 수 있습니다. 메서드 오버로딩은 같은 이름의 메서드를 사용하지만 다양한 매개변수를 처리할 수 있으므로 유연한 코드 작성이 가능합니다.