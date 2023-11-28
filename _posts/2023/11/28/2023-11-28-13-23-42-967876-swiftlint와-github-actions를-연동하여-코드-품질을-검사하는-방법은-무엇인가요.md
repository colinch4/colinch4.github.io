---
layout: post
title: "[swift] SwiftLint와 GitHub Actions를 연동하여 코드 품질을 검사하는 방법은 무엇인가요?"
description: " "
date: 2023-11-28
tags: [swift]
comments: true
share: true
---

SwiftLint는 Swift 코드의 스타일과 품질을 검사하는 도구입니다. 이를 GitHub Actions와 연동하여 코드 변경 사항이 있을 때마다 자동으로 코드 품질을 검사하고 결과를 피드백 받을 수 있습니다. 이를 통해 코드 품질을 유지하고 일관성을 갖출 수 있습니다.

다음은 SwiftLint와 GitHub Actions를 연동하는 단계입니다:

## 1. SwiftLint 설치
먼저 SwiftLint를 설치합니다. SwiftLint는 Homebrew와 같은 패키지 매니저를 통해 설치할 수 있습니다. 아래 명령어를 터미널에 입력하여 SwiftLint를 설치합니다:

```shell
brew install swiftlint
```

## 2. SwiftLint 설정 파일 생성
SwiftLint를 설정하기 위해 프로젝트 루트 디렉토리에 `.swiftlint.yml` 파일을 생성합니다. 이 파일은 코드 스타일을 정의하고 SwiftLint가 검사할 규칙을 설정하는데 사용됩니다.

다음은 예시로 사용할 수 있는 `.swiftlint.yml` 파일의 내용입니다:

```yaml
opt_in_rules:
  - trailing_whitespace
  - line_length
  - cyclomatic_complexity
  - force_try
  - leading_whitespace

excluded:
  - Carthage
  - Pods
  - .build

line_length:
  warning: 120
  error: 160
```

이 설정 파일은 코드 뒤의 공백, 한 줄의 길이, 복잡도 등을 검사하고 경고와 에러를 정의합니다. 자세한 설정은 SwiftLint 문서를 참조하세요.

## 3. GitHub Actions 워크플로우 파일 생성
프로젝트 루트 디렉토리에 `.github/workflows` 디렉토리를 생성한 다음, 그 안에 `swiftlint.yml` 파일을 생성합니다. 이 파일은 GitHub Actions의 워크플로우를 정의하고 SwiftLint를 실행하는데 사용됩니다.

`.github/workflows/swiftlint.yml` 파일을 다음과 같이 작성합니다:

```yaml
name: SwiftLint

on: [push, pull_request]

jobs:
  SwiftLint:
    runs-on: macos-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v2

      - name: Set up Swift
        uses: actions/setup-swift@v2
        with:
          swift-version: "5.3"

      - name: Run SwiftLint
        run: swiftlint
```

위의 워크플로우 파일은 코드를 push하거나 pull request를 생성할 때마다 SwiftLint를 실행하고 결과를 표시합니다.

## 4. GitHub에 워크플로우 파일 푸시
마지막으로, 작성한 워크플로우 파일을 GitHub에 푸시합니다. 이렇게 하면 코드 변경 사항마다 GitHub Actions가 실행되어 SwiftLint로 코드 품질을 검사하게 됩니다.

이제 코드 변경 시마다 GitHub Actions에서 SwiftLint가 실행되어 코드 품질을 검사하고 결과를 확인할 수 있습니다.

더 많은 설정과 규칙을 적용하고 싶다면 SwiftLint 문서를 참고하세요.+