---
layout: post
title: "[swift] Structs and mutation in Swift"
description: " "
date: 2021-06-11
tags: [swift]
comments: true
share: true
---

## Structs and mutation in Swift

> 번역본 입니다. 

출처 : <https://chris.eidhof.nl/post/structs-and-mutation-in-swift/>


값 타입은 변수가 복사 될 때마다 값에 대한 참조가 아니라 값 자체가 복사됨을 의미합니다.
예를 들어, 거의 모든 프로그래밍 언어에서 스칼라 타입은 값 타입입니다. 즉, 값이 새 변수에 할당 될 때마다 참조로 전달되지 않고 복사됩니다.
예를 들어, 거의 모든 프로그래밍 언어에서 스칼라 타입은 값 유형입니다. 즉, 값이 새 변수에 할당 될 때마다 참조로 전달되지 않고 복사됩니다.

```swift
var a = 42
var b = a
b += 1
```

위의 코드가 실행 된 후 b의 값은 43이지만 a는 여전히 42입니다.
이것은 너무 자연스러워서 명백한 것을 말하는 것처럼 보입니다.
그러나 Swift에서 모든 구조체는 스칼라 타입뿐만 아니라 이러한 방식으로 작동합니다.

포인트를 설명하는 간단한 구조체부터 시작하겠습니다.
CGPoint는 CGFloat를 포함하는 반면 Int를 포함한다는 점을 제외하면 CGPoint와 유사합니다.

```swift
struct Point {
    var x: Int
    var y: Int
}
```

구조체의 경우 Swift는 **자동으로 멤버 이니셜 라이저를 추가**합니다.
<br> =>
```swift
init(x : Int, y : Int) {
    self.x = x
    self.y = y
}
```
이 멤버 이니셜 라이져를 자동으로 추가한다는 뜻이다.
<br>이것은 이제 새로운 변수를 초기화 할 수 있다는 것을 의미합니다.

Swift의 구조체에는 value semantic이 있으므로 let을 사용하여 정의 된 구조체 변수의 속성을 변경할 수 없습니다. 예를 들어 다음 코드는 작동하지 않습니다.

Even though we defined x within the struct as a var property, we cannot 
change it, because origin is defined using let.

구조체 내에서 x를 var 속성으로 정의했더라도 origin을 let으로 정의되어있으므로 이를 변경할 수 없습니다. 
이것은 몇 가지 주요 장점이 있습니다. 
예를 들어 let point = ...와 같은 줄을 읽고 그 점이 구조체 변수라는 것을 알고 있다면 당신이 또한 이 point가 결코 변하지 않을 것이란 걸 알고 있습니다.(it will never, ever, change.) 이것은 코드를 읽을 때 큰 도움이 됩니다.

변경할 수 있는 변수를 만들려면 **var를 사용하여 변수를 만들어야합니다.**

```swift
var otherPoint = Point(x: 0, y: 0)
otherPoint.x += 10
otherPoint
```


var를 사용하여 변수를 만들면 변수를 변경할 수 있습니다.
**그러나 객체와 달리 모든 구조체 변수는 고유합니다.(unlike with objects, every struct variable is unique. )**
예를 들어, 새 변수 thirdPoint를 작성하고 origin 값을 할당할 수 있습니다. 
이제 우리는 thirdPoint를 변경할 수 있지만 origin (let을 사용하여 불변 변수로 정의한)은 변경되지 않습니다.

```swift
var origin = Point(x: 0, y: 0)
var thirdPoint = origin
thirdPoint.x += 10
thirdPoint.y += 5
// origin.x = 0 , origin.y = 0
// thirdPoint.x = 10, thirdPoint.y = 5
```

구조체를 새로운 변수에 할당하면 Swift가 자동으로 사본을 만듭니다.
비록 이것이 매우 비싸게 들리더라도(Even though this sounds very expensive), 많은 사본들은 컴파일러에 의해 최적화 될 수 있고, 스위프트는 사본을 매우 싸게 만들기 위해 노력합니다.
<br>더 자주 사용하려는 구조체 값이 있으면 확장에서 정적 속성으로 정의 할 수 있습니다.
예를 들어 Point에서 origin 속성을 정의하여 필요한 곳 ​​어디에서나 Point.origin을 작성할 수 있습니다.

```swift
extension Point {
    static let origin = Point(x: 0, y: 0)
}
Point.origin
```

Structs에는 다른 구조체도 포함될 수 있습니다.
예를 들어 Size 구조체를 정의하면 점과 크기로 구성된 Rect 구조체를 만들 수 있습니다.

```swift
struct Size {
    var width: Int
    var height: Int
}

struct Rectangle {
    var origin: Point
    var size: Size
}
```
이전과 마찬가지로 Rectangle의 멤버 별 이니셜 라이저를 얻습니다. 매개 변수의 순서는 프로퍼티 선언의 순서와 일치합니다.
구조체의 커스텀 이니셜 라이저를 원한다면 구조체 정의 안에 직접 추가 할 수 있습니다. 
그러나 구조체 정의에 커스텀 이니셜 라이저가 포함되어 있으면 Swift는 멤버별 이니셜 라이저를 생성하지 않습니다. 
* **확장에서 사용자 정의 이니셜 라이저를 정의하면 멤버 단위 이니셜 라이저도 유지됩니다.**

```swift
extension Rectangle {
    init(x: Int = 0, y: Int = 0, width: Int, height: Int) {
        origin = Point(x: x, y: y)
        size = Size(width: width, height: height)
    }
}
```
가변 변수 화면을 정의하면 화면이 바뀔 때마다 실행되는 didSet 블록을 추가 할 수 있습니다. 이 didSet은 플레이그라운드, 클래스 또는 전역 변수를 정의 할 때 구조체의 모든 정의에 적용됩니다.

이것이 작동하는 이유를 이해하는 것이 가치 타입을 이해하는 데 중요합니다.
구조체 변수를 변경하는 것은 의미상 새 값을 할당하는 것과 동일합니다.
구조체 내부에서 무언가를 mutate해도 여전히 구조체를 mutating하고 있음을 의미하므로 didSet은 여전히 ​​트리거(trigger) 되어야 합니다.

규칙적인 스트럿(with regular strut)을 사용하면 컴파일러는 값을 변경하고 실제로 사본을 만들지 않습니다. COW (Copy-On-Write) 구조체 (나중에 설명 할)는 다르게 작동합니다.

두 점을 더하는 것이 합리적입니다. 이를 위해 + 연산자를 사용하고 두 멤버를 모두 추가하고 새로운 Point를 반환 할 수 있습니다.

self는 불변이기 때문에 (origin = 작문은 self.origin = 의 약자이므로) 컴파일러는 origin 속성에 할당 할 수 없다고 알려줍니다.
우리는 self를 Rectangle의 모든 메소드에 전달되는 추가의 암시적 매개 변수로 생각할 수 있습니다. 
매개 변수를 전달할 필요는 없지만 항상 메서드 본문 안에 있습니다. 기본적으로 let으로 정의되어 있습니다. 이 제한이 존재하는 이유는 value semantic이 보장 될 수 있기 때문입니다. self 또는 self의 어떤 속성이나 심지어 중첩된 속성 (예 : self.origin.x)을 변경하려면 메소드를 변경하는 것으로 표시해야합니다.

많은 경우에, 동일한 메소드의 mutating 버전과 non-mutating 버전을 모두 갖는 것이 합리적입니다.
예를 들어, 배열에는 sort () 메서드 (mutating 및 정렬)와 sorted () 메서드 (새 배열을 반환하는)가 있습니다. 또한 우리는 우리의 translate (by : _) 메소드의 non-mutating 버전을 추가 할 수도 있습니다. 자체를 변경하는 대신 사본을 만들고 변경 한 다음 새 Rectangle을 반환합니다.

```swift
extension Rectangle {
  func translated(by offset: Point) -> Rectangle {
        var copy = self
        copy.translate(by: offset)
        return copy
    }
}
```
> 정렬 및 정렬 된 이름은 임의로 선택되지 않지만 Swift API 설계 지침을 준수하는 이름입니다.
Likewise, we applied these guidelines to translate and translated. There is even specific documentation for methods that have a mutating and a non-mutating variant: because translate has a side-effect, it should read as an imperative verb phrase. The non-mutating variant should have a -ed or -ing suffix.

value semantic의 특징 중 하나 
<br>=> value type이 let으로 선언되면 아무리 프로퍼티가 var이어도 변경할 수 없다. 
왜냐하면 value type이 let으로 할당되면 상자 유추를 사용하여 해당 value type은 갇히기 때문입니다. 
(Once a value is assigned to that constant using the box analogy that constant is closed. 🔒)

매개변수는 기본적으로 let으로 설정되어있다. value semantic을 보증하기 위해서 
=> 와우 이해했다. call by value로 전달되려면 let으로 기본적으로 설정되어야 하는 구나.

함수형 프로그래밍에서 부작용은 예상치 못한 방식으로 코드에 영향을 줄 수 있기 때문에 종종 나쁜 것으로 간주됩니다. 예를 들어, 개체가 여러 위치에서 참조되면 모든 위치에서 모든 변경이 자동으로 수행됩니다. 소개에서 보았 듯이 멀티 스레드 코드를 처리 할 때 쉽게 버그가 발생할 수 있습니다. 방금 확인하려는 객체를 다른 스레드에서 수정할 수 있기 때문에 모든 가정이 유효하지 않을 수 있습니다.

Swift 구조체를 사용하면 mutating은 동일한 문제가 없습니다. 
구조체의 mutating는 local 한 부작용이며 현재 구조체 변수에만 적용됩니다. 
모든 구조체 변수는 고유(unique)하기 때문에 (즉, 모든 구조체 값에는 정확히 하나의 소유자가 있으므로) 이런 방식으로 버그를 도입하는 것은 거의 불가능합니다. 
즉, 스레드에서 전역 구조체 변수를 언급하지 않는 한 말이죠.

mutating 키워드의 작동 방식을 이해하기 위해 inout 동작(behavior)을 살펴볼 수 있습니다.
Swift에서는 함수 매개 변수를 inout으로 표시 할 수 있습니다.

그렇게 하기전에 두 축에서 사각형을 10 포인트 씩 이동시키는 자유 함수를 정의해 봅시다. 모든 함수 매개 변수는 기본적으로 불변이므로 직사각형 매개 변수에서 직접 translate를 호출 할 수 없습니다. 이를 변경하기 위해 var, call translate를 사용하여 변경 가능한 복사본을 만들고 변경된 값을 반환합니다. 그런 다음 화면에 다시 할당해야합니다.

```swift 
func moveByTenTen(rectangle: Rectangle) -> Rectangle {
    var changed = rectangle
    changed.translate(by: Point(x: 10, y: 10))
    return changed
}
screen = moveByTenTen(rectangle: screen)
```

사각형을 변경하는 함수를 어떻게 작성할 수 있습니까? 돌이켜 보면 mutating 키워드는 정확히 그렇게했습니다. 암시 적 자체 매개 변수를 변경 가능하게하고 변수 값을 변경합니다.
<br>함수에서 매개 변수를 'inout'으로 표시 할 수 있습니다.
일반 매개 변수와 마찬가지로 값의 사본이 함수에 전달됩니다. 그러나 사본은 var로 정의 된 것처럼 변경할 수 있습니다. 함수가 반환되면 원래 값을 덮어 씁니다. => 여전히 값이 복사되어 전달되겠지만, 값 자체가 주소값이겠지.

```swift
func moveByTwentyTwenty(rectangle: inout Rectangle) {
    rectangle.translate(by: Point(x: 20, y: 20))
}
moveByTwentyTwenty(rectangle: &screen)
```

moveByTwentyTwenty 함수는 화면 사각형을 가져 와서 로컬로 변경하고 새 값을 다시 복사합니다 (화면의 이전 값을 재정의 함).
이 동작은 'mutating'방법과 동일합니다. **실제로 mutating 메소드는 self가 inout으로 표시된다는 점을 제외하고 구조체의 일반 메소드와 같습니다.**

```swift
let immutableScreen = screen
moveByTwentyTwenty(rectangle: &immutableScreen) // error
```
=> 확인하기 위해 let을 사용하여 정의 된 사각형에서 moveByTwentyTwenty를 호출 할 수 없습니다. 변경 가능한 값으로 만 사용할 수 있습니다.
이제 += 와 같은 mutating 연산자를 정의 할 수있는 방법도 이해가됩니다. 이러한 연산자는 오른쪽을 추가하여 왼쪽을 수정합니다.

```swift
func +=(lhs: inout Point, rhs: Point) {
    lhs = lhs + rhs
}
var myPoint = Point.origin
myPoint += Point(x: 10, y: 10)
```

함수 장에서, 우리는 inout에 대해 더 자세히 설명 할 것입니다. 현재로서는 inout이 많은 곳에 있다고 말할 수 있습니다. 예를 들어 이제 아래 subscript가 어떻게 작동하는지 쉽게 이해할 수 있습니다.

```swift
var array = [Point(x: 0, y: 0), Point(x: 10, y: 10)]
array[0] += Point(x: 100, y: 100)
```
expression array\[0]은 'inout'변수로 자동 전달됩니다. 함수 장에서 'inout'매개 변수에 대해 자세히 살펴보고 array\[0]과 같은 표현식을 inout 매개 변수로 사용할 수있는 이유를 살펴 봅니다.
