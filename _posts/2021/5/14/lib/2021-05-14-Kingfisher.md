---
layout: post
title: "[lib] Kingfisher란?"
description: " "
date: 2021-05-14
tags: [lib]
comments: true
share: true
---


## Kingfisher
이미지를 간편하게 사용할 수 있게 해주는 라이브러리       
첫 다운로드 때 캐시에 저장해두기 때문에 이후에 다시 이미지를 로드 할 때  캐시에서 데이터를 가져오기 때문에 
매우 빠른 속도로 받을 수 있다.     

## 사용법
cocoapod 설치      
```swift
source 'https://github.com/CocoaPods/Specs.git'
platform :ios, '10.0'
use_frameworks!

target 'MyApp' do
  pod 'Kingfisher', '~> 6.0'
end
```      

기본 사용법       
```swift
import Kingfisher

let url = URL(string: "https://example.com/image.png")
imageView.kf.setImage(with: url)
```

옵션     
```swift
// 트랜지션 옵션
imageView.kf.setImage(
                    with: url, 
                    options: [.transition(.fade(0.2))]
                   )
                   
// 라운드 옵션
let processor = RoundCornerImageProcessor(cornerRadius: 20)
imageView.kf.setImage(
                    with: url, 
                    options: [.processor(processor)]
                   )
```

퍼포먼스 향상 (캐슁)     
```swift
if let url = URL(string: cast.tec_img) {
    let resource = ImageResource(downloadURL: url, cacheKey: cast.tec_img)
    let processor = DownsamplingImageProcessor(size: tecImg.bounds.size)
    tecImg.kf.setImage(
        with: resource,
        options: [
            .transition(.fade(0.3)),
            .processor(processor),
            .scaleFactor(UIScreen.main.scale),
            .cacheOriginalImage
        ])
}

// 테이블 뷰 또는 콜렉션 뷰에 적용
func tableView(_ tableView: UITableView,
                              didEndDisplaying cell: UITableViewCell,
                              forRowAt indexPath: IndexPath) {
    cell.imageView?.kf.cancelDownloadTask()
}
```
## Kingfisher git 주소
<img width="594" alt="스크린샷 2021-03-01 오후 5 32 50" src="https://user-images.githubusercontent.com/45002556/109471514-33ff3f80-7ab4-11eb-918a-9cd5f06313bb.png">

https://github.com/onevcat/Kingfisher
