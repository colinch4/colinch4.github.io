---
layout: post
title: "[swift] SwiftLint를 사용하여 IBOutlet과 IBAction의 사용 방식을 어떻게 통일할 수 있을까요?"
description: " "
date: 2023-11-28
tags: [swift]
comments: true
share: true
---

Interface Builder를 사용하여 iOS 앱을 개발할 때, IBOutlet과 IBAction을 사용하여 인터페이스 요소와 코드를 연결하는 것은 일반적입니다. 그러나 프로젝트 팀에서 여러 사람이 작업하다보면 코드 스타일이 일관되지 않을 수 있습니다. 이러한 문제를 해결하기 위해 SwiftLint를 사용할 수 있습니다.

SwiftLint는 Swift 코드 스타일 가이드를 자동으로 적용해주는 도구입니다. IBOutlet과 IBAction의 사용 방식을 통일하고 코드의 가독성을 향상시키기 위해 SwiftLint를 설정하는 방법을 살펴보겠습니다.

먼저, 프로젝트에 SwiftLint를 설치해야 합니다. SwiftLint는 CocoaPods나 Carthage를 통해 설치할 수 있습니다. 설치 후, 프로젝트 루트 디렉토리에 `.swiftlint.yml` 파일을 생성하여 설정을 추가합니다.

예를 들어, IBOutlet과 IBAction을 다음과 같이 통일하고 싶다고 가정해보겠습니다.
- IBOutlet 프로퍼티 이름은 `IBOutlet` 접두사를 사용한다.
- IBAction 메소드 이름은 `didTap` 접두사를 사용하고, 해당 컨트롤러에서 발생한 이벤트를 구체적으로 나타낸다.

다음은 `.swiftlint.yml` 파일에 추가할 설정입니다.

```yaml
attribute_rules:
  - identifier: IBOutlet
    kind: var
    prefix: IBOutlet
  - identifier: IBAction
    kind: func
    prefix: didTap
    severity: warning
```

위 설정을 추가하면 SwiftLint가 `IBOutlet` 프로퍼티에 접두사 `IBOutlet`을 사용하도록 지시하고, `IBAction` 메소드에는 접두사 `didTap`을 사용하도록 지시합니다. 또한 `IBAction` 메소드의 경고 수준을 설정하여 경고로 표시할 수 있습니다.

이제 SwiftLint를 실행하여 코드를 분석하고 IBOutlet과 IBAction의 사용 방식을 검사할 수 있습니다. Xcode에서 프로젝트 빌드 시 Build Phases 탭에 Run Script 단계를 추가하고, 다음과 같은 스크립트를 추가합니다.

```shell
if which swiftlint >/dev/null; then
  if [ -f ".swiftlint.yml" ]; then
    swiftlint
  else
    echo "warning: SwiftLint configuration file not found. Skipping linting."
  fi
else
  echo "warning: SwiftLint not installed. Download from https://github.com/realm/SwiftLint"
fi
```

위 스크립트는 SwiftLint가 설치되어 있고, 프로젝트 디렉토리에 `.swiftlint.yml` 파일이 있는 경우에만 SwiftLint를 실행합니다. 실행 결과로 IBOutlet과 IBAction의 사용 방식이 규칙에 맞지 않는 경우에는 경고로 표시되므로, 코드 리뷰 시 해당 사항을 수정할 수 있습니다.

이렇게하면 SwiftLint를 사용하여 IBOutlet과 IBAction의 사용 방식을 통일하고 코드의 가독성을 개선할 수 있습니다. SwiftLint는 다양한 설정 옵션을 제공하기 때문에 팀의 코딩 스타일에 맞게 설정을 수정할 수 있습니다.

참고:
- [SwiftLint](https://github.com/realm/SwiftLint)
- [SwiftLint 설정 문서](https://github.com/realm/SwiftLint/blob/main/.github/SwiftLint%20Configuration%20Options.md)