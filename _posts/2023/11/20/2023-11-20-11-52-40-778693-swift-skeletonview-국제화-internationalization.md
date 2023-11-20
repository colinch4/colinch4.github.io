---
layout: post
title: "[swift] Swift SkeletonView 국제화 (Internationalization)"
description: " "
date: 2023-11-20
tags: [swift]
comments: true
share: true
---

Swift SkeletonView는 앱의 로딩 화면을 구성하는 라이브러리로서, 사용자에게 로딩이 진행 중임을 시각적으로 보여줍니다. Swift SkeletonView는 앱의 다국어 지원을 위해 국제화 기능을 가지고 있습니다. 다음은 Swift SkeletonView를 국제화하는 방법에 대한 설명입니다.

## 앱의 다국어 지원 설정

앱이 다국어를 지원하도록 설정해야 합니다. 앱의 "Localizations" 설정에서 원하는 언어를 추가하여 다국어 지원을 활성화할 수 있습니다. 아래는 앱의 다국어 설정을 변경하는 방법입니다.

1. 프로젝트 내비게이터에서 앱의 타깃을 선택합니다.
2. "Info" 탭을 선택합니다.
3. "Localizations" 섹션에서 "+" 버튼을 클릭하여 다국어를 추가합니다.
4. 원하는 언어를 선택하고 "Finish"를 클릭하여 설정을 완료합니다.

## 다국어 리소스 파일 생성

각 언어별로 SkeletonView의 텍스트나 이미지를 포함하는 리소스 파일을 생성해야 합니다. 이 리소스 파일은 앱이 특정 언어로 실행될 때 SkeletonView에 표시할 컨텐츠를 제공합니다. 아래는 다국어 리소스 파일을 생성하는 방법입니다.

1. 프로젝트 내비게이터에서 앱의 타깃을 선택합니다.
2. "File" 메뉴에서 "New"를 선택하고 "Resource" 탭을 클릭합니다.
3. "Strings File"을 선택하여 리소스 파일을 생성합니다.
4. 파일 이름을 입력하고 "Create"를 클릭합니다.
5. 생성된 리소스 파일을 선택하고 오른쪽 사이드바의 "Localization" 섹션에서 원하는 언어를 선택합니다.
6. 선택한 언어에 해당하는 SkeletonView 텍스트를 입력합니다.

## SkeletonView 설정

다국어 리소스 파일에 정의된 텍스트를 SkeletonView에 설정해야 합니다. 아래는 Swift SkeletonView를 다국어 지원하는 방법입니다.

1. SkeletonView를 사용하는 ViewController에서 다국어 리소스 파일을 로드합니다.

```swift
let skeletonText = NSLocalizedString("skeleton_text_key", comment: "") // 다국어 리소스 텍스트 로드
```

2. 로드한 텍스트를 SkeletonView에 설정합니다.

```swift
skeletonLabel.text = skeletonText // SkeletonView에 텍스트 설정
```

위와 같은 방법으로 SkeletonView의 텍스트를 다국어로 설정할 수 있습니다.

## 결론

Swift SkeletonView를 국제화하는 방법에 대해 알아보았습니다. 앱의 지역화 설정을 변경하고, 다국어 리소스 파일을 생성한 후에 SkeletonView에 텍스트를 설정하여 다국어 지원을 완성할 수 있습니다.