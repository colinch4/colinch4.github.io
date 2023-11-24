---
layout: post
title: "[swift] SkyFloatingLabelTextField 입력한 텍스트 내용을 압축 파일로 저장하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

이번에는 Swift에서 SkyFloatingLabelTextField 컴포넌트를 사용하여 입력한 텍스트 내용을 압축 파일로 저장하는 방법을 알아보겠습니다.

## 1. 프로젝트에 SkyFloatingLabelTextField 추가하기

먼저, 프로젝트에 SkyFloatingLabelTextField를 추가합니다. 이를 위해 `CocoaPods`를 사용할 수 있습니다. `Podfile`에 다음과 같이 작성합니다.

```ruby
pod 'SkyFloatingLabelTextField'
```

그리고 터미널에서 다음 명령을 실행하여 CocoaPods를 설치합니다.

```bash
pod install
```

## 2. SkyFloatingLabelTextField 사용하기

스토리보드에서 SkyFloatingLabelTextField를 추가하거나, 코드에서 직접 생성할 수 있습니다. 이제 텍스트를 입력할 수 있는 입력 필드가 준비되었습니다.

```swift
import SkyFloatingLabelTextField

let textField = SkyFloatingLabelTextField(frame: CGRect(x: 20, y: 100, width: 200, height: 40))
textField.placeholder = "텍스트를 입력하세요."
view.addSubview(textField)
```

## 3. 텍스트 내용을 압축 파일로 저장하기

이제 입력한 텍스트를 압축 파일로 저장하는 코드를 작성해보겠습니다. 압축 파일로 저장하기 위해 `ZipArchive` 라이브러리를 사용합니다. 먼저, `ZipArchive`를 프로젝트에 추가하기 위해 `CocoaPods`를 사용합니다. `Podfile`에 다음과 같이 작성합니다.

```ruby
pod 'SSZipArchive'
```

터미널에서 다음 명령을 실행하여 CocoaPods를 설치합니다.

```bash
pod install
```

이제 압축 파일로 저장하는 코드를 작성합니다.

```swift
import SSZipArchive

guard let text = textField.text else {
    print("텍스트를 입력하세요.")
    return
}

let documentsDirectory = NSSearchPathForDirectoriesInDomains(.documentDirectory, .userDomainMask, true)[0]
let filePath = documentsDirectory + "/text.txt"

do {
    try text.write(toFile: filePath, atomically: true, encoding: .utf8)
    
    let zipFilePath = documentsDirectory + "/archive.zip"
    SSZipArchive.createZipFile(atPath: zipFilePath, withFilesAtPaths: [filePath])
    
    print("압축 파일로 저장되었습니다. 경로: \(zipFilePath)")
} catch {
    print("파일 저장에 실패하였습니다. 에러: \(error)")
}
```

위 코드는 입력한 텍스트를 파일로 저장한 뒤, 해당 파일을 `SSZipArchive`를 사용하여 압축 파일로 만듭니다. 압축된 파일은 `documents` 디렉토리에 `archive.zip`라는 이름으로 저장됩니다.

## 결론

SkyFloatingLabelTextField를 사용하여 입력한 텍스트 내용을 압축 파일로 저장하는 방법에 대해 알아보았습니다. 이를 통해 텍스트 데이터를 보다 효과적으로 관리하고 다른 시스템과 공유할 수 있습니다.