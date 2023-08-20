---
layout: post
title: "[swift] Choosing Between Structures and Classes"
description: " "
date: 2021-06-11
tags: [swift]
comments: true
share: true
---

출처 : <https://developer.apple.com/documentation/swift/choosing_between_structures_and_classes>

## Choosing Between Structures and Classes

데이터 및 모델 동작 저장 방법을 결정하십시오. (Decide how to store data and model behavior.)

## Overview

구조 및 클래스는 앱에 데이터 및 모델링 동작을 저장하기에 적합한 선택이지만 유사성으로 인해 하나를 선택하기가 어려울 수 있습니다.

앱에 새 데이터 유형을 추가 할 때 어떤 옵션이 적합한 지(struct가 좋을지, class가 좋을지) 선택하려면 다음 권장 사항을 고려하십시오.

* 기본적으로 struct를 사용하십시오. ( Use structures by default. )
* Objective-C 와 상호 운용성이 필요할 때 클래스를 사용하십시오. ( Use classes when you need Objective-C interoperability. )
* 모델링 할 데이터의 identity를 제어해야 할 때 클래스를 사용하십시오. (Use classes when you need to control the identity of the data you're modeling.)
* 프로토콜을 채택해 구현을 공유할 때는 struct을 사용하십니오. (Use structures along with protocols to adopt behavior by sharing implementations.)

## Choose Structures by Default

일반적인 종류의 데이터를 나타내려면 struct을 사용하십시오. **Swift의 struct는 다른 언어의 클래스에 제한되는 많은 특징들을 포함하고 있습니다.** struct는 저장 프로퍼티, 연산 프로퍼티, 그리고 메소드를 가질 수 있습니다. 더구나, swift 구조체들은 프로토콜을 채택해 프로토콜의 기본 구현들을 통해 동작할 수도 있습니다. swift 표준 라이프브러리 와 Foundation의 당신이 자주 쓰는 타입들은 struct를 사용합니다, **예를 들어 numbers, strings, array, 그리고 dictionaries 이죠.**    

구조체를 사용하면 당신 앱의 전체 상태를 고려할 필요 없이 당신 코드의 일부를 쉽게 추론할 수 있습니다. 
왜냐하면 구조체는 클래스와 달리 값 타입이라 구조체의 로컬한 변화가 당신의 앱의 나머지에 보이지 않을 것입니다, 당신이 당신의 앱의 흐름의 부분으로서 이러한 변화들은 명시적으로 communicate 하지 않는 한. 
<br>( => 이 말은 모델 구조체의 프로퍼티를 변경하더라도 값 타입이라 뷰와 관련된 부분에서는 반영이 안될 것이라는 것이다. 뷰를 보여주는 메소드가 호출되야지만 이러한 변화가 반영될 것이라는 것이다. 반면에 클래스 타입은 모델 객체의 프로퍼티를 변경하면 관련 뷰의 부분도 같은 객체의 프로퍼티를 참조하고 있으면 뷰를 보여주는 메소드가 호출되기도 전에 뷰에 반영이 될 수 있는 것이다.=> 명확하지가 않다.)
<br>결과적으로, 당신은 코드의 섹션을 보고 해당 섹션의 인스턴스가 명시적으로 변화가 될 것에 대해 확신할 수 있습니다, 접선적으로 관련된 함수 호출로부터 해당 인스턴스가 눈에 보이지않게 변화되기 보다는.
<br>( => 따라서 구조체를 사용하면 구조체와 관련된 뷰가 함수가 호출될 때 구조체의 변화를 반영할 것이 때문에 인스턴스의 변화가 명시적으로 보이고, 개발자는 이에 대해 변화가 언제 일어나는지 확신할 수 있다는 것이다. )

## Use Classes When You Need Objective-C Interoperability

**당신의 데이터를 처리하는 데 Objective-C API를 사용할 필요가 있거나, 아니면 당신의 데이터 모델클 현존하는 -C 프레임워크에서 정의한 클래스 계층에 맞추어야 할 필요가 있을 때**, 당신은 당신의 데이터를 모델링하기 위해 클래스 및 클래스 상속을 사용해야 합니다. 예를 들어, 많은 Objective-C 프레임워크는 당신이 상속을 받아야 하는 클래스들을 노출합니다. (상속이 필요하므로 class를 사용해라)

## Use Classes When You Need to Control Identity

Swift의 클래스는 참조 유형이기 때문에 ID 개념을 제공합니다.( 메모리의 heap의 주소값을 노출하므로 참조가 가능합니다.)
이는 두 개의 서로 다른 클래스 인스턴스가 각각의 저장된 속성에 대해 동일한 값을 가질 때 ID 연산자 (===)에 따라 여전히 다른 것으로 간주됨을 의미합니다. (=> 객체 동등성(equality)은 같지만 객체 동일성(identity)은 다르다.)
이것은 또한 앱에서 클래스 인스턴스를 공유할 때, 당신이 인스턴스에 대해 만든 변경사항이 그 인스턴스를 참조하는 당신의 모든 코드에서 살펴볼 수 있다는 것이다.(주소값으로 해당 객체를 참조하므로!)
이러한 동일성의 종류을 가진 인스턴스가 필요하다면 클래스를 사용하십시오. 보통의 적용 사례는 파일 핸들, 네트워크 연결, 그리고 CBCCentralManager와 같은 공유 하드웨어입니다.  

예를 들어, 만약 너가 로컬 데이터베이스 연결을 나타내는 유형이 있는 경우, 해당 데이터 베이스에 대한 엑세스를 관리하는 코드는 당신의 앱에서 볼 때 데이터 베이스의 상태를 완전히 제어해야 합니다. 이러한 경우 클래스를 사용하는 것이 적절하지만, 그러나 공유된 데이터 베이스 객체에 접근을 할 수 있는 부분을 제한해야 합니다.( 공유 자원이므로 race condition이 나지 않게 조심하라는 뜻 등등이 있을 것 같다. )

> Important
<br>**동일성을 주의 깊게 다루십시오.** 클래스 인스턴스를 앱 전체에서 널이 공유하면 논리적 에러가 날 가능성이 높습니다.
공유량이 많은 인스턴스를 잘못 사용해서 논리적 오류가 나는 것을 바라지 않을 테니, 잘 작동하도록 이러한 코드는 올바르게 작성해야 합니다. 

## Use Structures When You Don't Control Identity

제어하지 않는 ID를 가진 엔티티에 대한 정보가 포함 된 데이터를 모델링 할 때 구조를 사용하십시오.

In an app that consults a remote database, for example, an instance's identity may be fully owned by an external entity and communicated by an identifier. If the consistency of an app's models is stored on a server, you can model records as structures with identifiers. 
In the example below, jsonResponse contains an encoded PenPalRecord instance from a server:

예를 들어 원격 데이터베이스를 참조하는 앱에서 인스턴스의 ID(PenPalRecord)는 외부 엔터티가 완전히 소유하고 변수(myRecord)로 통신 할 수 있습니다. 앱 모델의 일관성이 서버에 저장된 경우 변수를 사용하여 레코드를 struct로 모델링 할 수 있습니다.
아래 예에서 jsonResponse에는 서버의 인코딩 된 PenPalRecord 인스턴스가 포함되어 있습니다.

```swift
struct PenPalRecord {
    let myID: Int
    var myNickname: String
    var recommendedPenPalID: Int
}

var myRecord = try JSONDecoder().decode(PenPalRecord.self, from: jsonResponse)
```

PenPalRecord와 같은 모델 유형에 대한 로컬 변경이 유용합니다.
예를 들어, 앱은 사용자 의견에 따라 여러 개의 다른 펜팔을 추천 할 수 있습니다.
PenPalRecord 구조는 기본 데이터베이스 레코드의 ID를 제어하지 않기 때문에 로컬 PenPalRecord 인스턴스에 대한 변경으로 인해 데이터베이스의 값이 실수로 변경 될 위험이 없습니다.

만약 앱의 또 다른 부분이 myNickname을 바꾸고 변경 요청을 서버에게 다시 제출하면, 가장 최근에 거부된 펜팔 추천이 변경으로 인해 잘못 선택되지 않습니다. (닉네임을 잘못 변경되어도, struct 이므로 데이터베이스에 적용되지 않을 것이라는 것)

myID 프로퍼티가 상수로 선언되었기 때문에, 이것은 로컬하게 변화하지 않을 것입니다. 결과적으로 데이터베이스에 대한 요청들은 실수로 데이터베이스가 잘못 기록되게 하지 않을 것입니다.
## Use Structures and Protocols to Model Inheritance and Share Behavior
* 구조와 프로토콜을 사용하여 상속을 모델링하고 동작을 공유

구조체와 클래스들은 모두 상속의 형식을 지원합니다. 구조체와 프토콜은 오직 프로토콜만을 준수할 수 있습니다. 그들은 클래스를 상속할 수 없습니다. 
그러나 클래스 상속으로 빌드 할 수있는 상속 계층의 종류(예 : 클래스 )는 프로토콜 상속 및 구조를 사용하여 모델링 할 수도 있습니다. 

만약 당신이 처음부터 상속 관계를 구축하는 경우, protocol 상속을 선호하세요. **프로토콜은 클래스, 구조체, enum이 상속에 참여할 것을 허락하지만, 반면에 클래스 상속은 다른 클래스 타입만이 호환됩니다.** 당신이 당신의 데이터를 어떻게 모델링 할지 선택하고 있다면, 처음에는 데이터 타입의 계층을 protocol을 사용하여 구축한 다음, 당신의 struct을 protocol을 채택하도록 시도하십시오.( 첫 시도로는 struct & protocol 조합이 좋다. 왜냐하면 struct는 데이터 모델링의 default한 선택이고, 프로토콜은 클래스, 구조체 , enum 모두가 준수할 수 있는 이후의 변화에 대응하기 편한 inheritance이기 때문이다. )  
