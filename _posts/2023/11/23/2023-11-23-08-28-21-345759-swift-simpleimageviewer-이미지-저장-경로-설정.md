---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 저장 경로 설정"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

### 개요
Swift로 개발된 SimpleImageViewer는 이미지 뷰어를 구현하는데 사용할 수 있는 간단하고 편리한 라이브러리입니다. 이 라이브러리를 사용하여 이미지를 다운로드하고 저장하는 기능을 구현하려면 저장 경로를 설정해야 합니다.

### 저장 경로 설정하기

다음은 SimpleImageViewer를 사용하여 이미지를 저장할 경로를 설정하는 방법입니다.

1. `FileManager`를 사용하여 저장 경로를 생성합니다.

   ```swift
   func getDocumentDirectory() -> URL? {
       let fileManager = FileManager.default
       let documentDirectory = fileManager.urls(for: .documentDirectory, in: .userDomainMask).first
       return documentDirectory
   }
   ```

2. 이미지를 저장할 경로를 생성한 후, 이미지 파일명을 포함하여 `URL` 객체를 생성합니다.

   ```swift
   func getImageURL() -> URL? {
       guard let documentDirectory = getDocumentDirectory() else {
           return nil
       }
       let imageName = "myImage.jpg" // 이미지 파일명
       let imageURL = documentDirectory.appendingPathComponent(imageName)
       return imageURL
   }
   ```

3. 이미지를 다운로드하여 해당 경로에 저장합니다.

   ```swift
   if let imageURL = getImageURL() {
       let image = // 이미지 다운로드 또는 생성 로직
       if let imageData = image.jpegData(compressionQuality: 1.0) {
           do {
               try imageData.write(to: imageURL)
               print("이미지 저장 성공")
           } catch {
               print("이미지 저장 실패: \(error.localizedDescription)")
           }
       }
   }
   ```

이제 SimpleImageViewer를 사용하여 이미지를 저장하기 위해 경로를 설정하는 방법을 알았습니다. 이 코드를 참고하여 원하는 저장 경로를 설정하고, 이미지를 다운로드하여 저장해보세요.

### 참고 자료
- [SimpleImageViewer GitHub 페이지](https://github.com/Krisiacik/SimpleImageViewer)
- [Swift FileManager](https://developer.apple.com/documentation/foundation/filemanager)
- [URL - Apple Developer Documentation](https://developer.apple.com/documentation/foundation/url)