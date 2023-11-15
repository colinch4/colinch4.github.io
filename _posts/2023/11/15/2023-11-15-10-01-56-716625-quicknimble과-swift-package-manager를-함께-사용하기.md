---
layout: post
title: "[swift] Quick/Nimble과 Swift Package Manager를 함께 사용하기"
description: " "
date: 2023-11-15
tags: [swift]
comments: true
share: true
---

Swift는 Apple의 주도로 개발된 현대적이고 안전한 프로그래밍 언어입니다. Swift Package Manager(SPM)는 Swift 언어의 공식 의존성 관리 도구로, Swift 프로젝트의 종속성을 손쉽게 관리할 수 있게 해줍니다. Quick과 Nimble은 Swift로 작성된 유닛 테스트 프레임워크입니다. 

이 글에서는 Quick과 Nimble을 SPM을 사용하여 프로젝트에 추가하는 방법을 알아보겠습니다.

## 시작하기 전에

프로젝트를 생성하기 전에, Swift Package Manager를 사용하여 프로젝트를 관리하는 것이 좋습니다. SPM은 프로젝트의 디렉토리 구조를 관리하여 종속성 관리에 용이합니다. 

SPM을 사용하여 새로운 Swift 패키지를 생성하기 위해 다음 명령을 실행하세요:

```
$ swift package init --type executable
```

위 명령은 새로운 Swift Package를 초기화하고 실행 가능한 프로젝트로 설정합니다. 

## Quick/Nimble 추가하기

프로젝트를 생성한 후, Quick과 Nimble을 프로젝트에 추가해야 합니다. 이를 위해 `Package.swift`를 열고 `dependencies` 블록에 다음과 같이 추가하세요:

```swift
import PackageDescription

let package = Package(
    name: "MyPackage",
    dependencies: [
        .package(url: "https://github.com/Quick/Quick.git", from: "2.2.0"),
        .package(url: "https://github.com/Quick/Nimble.git", from: "8.0.0"),
    ],
    targets: [
        .target(
            name: "MyPackage",
            dependencies: ["Quick", "Nimble"]),
        .testTarget(
            name: "MyPackageTests",
            dependencies: ["MyPackage", "Quick", "Nimble"]),
    ]
)
```

위의 코드는 Quick과 Nimble을 프로젝트에 종속성으로 추가합니다.

## 패키지 종속성 설치하기

이제 패키지 종속성을 설치해야 합니다. 프로젝트 디렉토리에서 다음 명령을 실행하세요:

```
$ swift package resolve
```

위 명령은 `Package.swift` 파일에 명시된 종속성을 설치합니다.

## 테스트 작성하기

Quick과 Nimble이 프로젝트에 추가되었으므로 이제 테스트를 작성할 수 있습니다. 

프로젝트 디렉토리에서 `Tests/` 폴더를 생성하고, `MyPackageTests.swift` 파일을 만들어 다음과 같이 작성하세요:

```swift
import XCTest
import Nimble
import Quick

@testable import MyPackage

class MyPackageTests: QuickSpec {
    override func spec() {
        describe("MyPackage") {
            it("should return true") {
                expect(true).to(beTrue())
            }
        }
    }
}
```

위의 코드는 간단한 테스트를 정의하고 실행합니다.

## 테스트 실행하기

이제 모든 구성이 완료되었으므로 XCTest를 사용하여 테스트를 실행할 수 있습니다. 프로젝트 디렉토리에서 다음 명령을 실행하세요:

```
$ swift test
```

위 명령은 프로젝트의 테스트를 실행하고 결과를 출력합니다.

## 결론

이제 Quick과 Nimble을 Swift Package Manager와 함께 사용하는 방법에 대해 알게 되었습니다. SPM을 사용하여 Swift 프로젝트를 쉽게 관리하고 Quick/Nimble을 통해 유닛 테스트를 작성할 수 있습니다. Swift 패키지의 종속성을 관리하는 SPM은 프로젝트의 유지보수를 용이하게 만들어줍니다.