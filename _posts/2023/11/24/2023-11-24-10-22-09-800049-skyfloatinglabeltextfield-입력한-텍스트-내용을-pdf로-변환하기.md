---
layout: post
title: "[swift] SkyFloatingLabelTextField 입력한 텍스트 내용을 PDF로 변환하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

이번에는 SkyFloatingLabelTextField에서 입력한 텍스트 내용을 PDF 파일로 변환하는 방법에 대해 알아보겠습니다.

## 1. PDF 생성을 위한 준비 작업

PDF를 생성하기 위해서는 먼저 필요한 라이브러리를 프로젝트에 추가해야 합니다. Swift에서는 PDFKit 라이브러리를 사용하여 PDF를 생성할 수 있습니다. 따라서, 프로젝트에 PDFKit 라이브러리가 이미 포함되어 있는지 확인해보고, 포함되어 있지 않다면 다음 순서에 따라 추가해줍니다.

### 1-1. PDFKit 라이브러리 추가

1. 프로젝트 네비게이터에서 프로젝트 파일을 선택합니다.
2. Targets을 선택한 후, "Build Phases" 탭으로 이동합니다.
3. "Link Binary With Libraries" 섹션을 찾아 "+" 버튼을 클릭합니다.
4. "PDFKit.framework"를 선택한 후, "Add" 버튼을 클릭합니다.

## 2. SkyFloatingLabelTextField에서 텍스트 내용 가져오기

SkyFloatingLabelTextField는 UITextField의 subclass로, 입력한 텍스트를 쉽게 가져오거나 설정할 수 있습니다. 다음은 SkyFloatingLabelTextField에서 텍스트 내용을 가져오는 예제 코드입니다.

```swift
let textField = SkyFloatingLabelTextField(frame: CGRect(x: 0, y: 0, width: 200, height: 40))
// SkyFloatingLabelTextField 인스턴스를 생성합니다.

let text = textField.text
// textField에서 텍스트 값을 가져옵니다.
```

## 3. 텍스트 내용을 PDF로 변환하기

입력한 텍스트를 PDF로 변환하기 위해서는 다음 순서에 따라 작업해야 합니다.

### 3-1. PDF 문서 생성하기

PDF 문서를 생성하기 위해 PDFDocument 인스턴스를 생성합니다.

```swift
let document = PDFDocument()
```
### 3-2. 텍스트를 PDF 페이지에 추가하기

생성한 PDF 문서에 텍스트를 추가하기 위해 다음과 같이 작업합니다.

```swift
let page = PDFPage()
let textAnnotation = PDFAnnotation(bounds: CGRect(x: 0, y: 0, width: 200, height: 40), forType: .freeText, withProperties: nil)
textAnnotation.contents = textField.text
page.addAnnotation(textAnnotation)
document.insert(page, at: document.pageCount)
```

### 3-3. PDF 파일로 저장하기

생성한 PDF 문서를 파일로 저장하기 위해 다음과 같은 코드를 사용합니다.

```swift
let pdfData = document.dataRepresentation()
do {
    try pdfData?.write(to: URL(fileURLWithPath: "경로/파일명.pdf"))
} catch {
    print("Error: \(error)")
}
```

위 방법을 따르면, SkyFloatingLabelTextField에서 입력한 텍스트 내용을 PDF 파일로 변환할 수 있습니다.

참고 자료:
- [PDFKit](https://developer.apple.com/documentation/pdfkit)