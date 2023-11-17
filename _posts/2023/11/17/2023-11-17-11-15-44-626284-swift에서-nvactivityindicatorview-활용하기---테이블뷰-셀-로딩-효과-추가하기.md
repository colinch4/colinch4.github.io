---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView 활용하기 - 테이블뷰 셀 로딩 효과 추가하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

## 개요
이번 포스트에서는 Swift 프로그래밍 언어를 사용하여 NVActivityIndicatorView를 활용하여 테이블뷰 셀에 로딩 효과를 추가하는 방법에 대해 알아보겠습니다.

## NVActivityIndicatorView란?
NVActivityIndicatorView는 로딩 인디케이터를 쉽게 만들 수 있도록 도와주는 오픈 소스 라이브러리입니다. 웹페이지나 앱의 데이터 로딩 중에 사용자에게 진행 상태를 시각적으로 보여주는 역할을 합니다.

## NVActivityIndicatorView 설치
NVActivityIndicatorView를 사용하기 위해서는 Cocoapods를 통해 라이브러리를 설치해야 합니다. `Podfile`에 다음과 같은 내용을 추가하고 터미널에서 `pod install`을 실행하세요.

```ruby
pod 'NVActivityIndicatorView'
```

## 테이블뷰 셀에 NVActivityIndicatorView 추가하기
1. 라이브러리를 설치한 뒤에는 `import NVActivityIndicatorView`를 추가하여 라이브러리를 불러옵니다.

2. 테이블뷰 셀에 해당하는 클래스에서 `NVActivityIndicatorView` 인스턴스를 선언합니다. 예를 들어, 다음과 같이 `CustomTableViewCell` 클래스를 만들었다고 가정해봅시다.

```swift
class CustomTableViewCell: UITableViewCell {
    var activityIndicator: NVActivityIndicatorView!
    
    override init(style: UITableViewCell.CellStyle, reuseIdentifier: String?) {
        super.init(style: style, reuseIdentifier: reuseIdentifier)
        
        // NVActivityIndicatorView 설정
        activityIndicator = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 40, height: 40))
        activityIndicator.type = .ballSpinFadeLoader
        activityIndicator.color = .gray
        activityIndicator.center = self.contentView.center
        self.contentView.addSubview(activityIndicator)
    }
    
    required init?(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    // 로딩 효과 시작
    func startLoading() {
        activityIndicator.startAnimating()
    }
    
    // 로딩 효과 중지
    func stopLoading() {
        activityIndicator.stopAnimating()
    }
}
```

3. 테이블뷰의 `cellForRow(at:)` 메서드에서 셀에 로딩 효과를 추가하고 시작하는 코드를 작성합니다.

```swift
func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
    let cell = tableView.dequeueReusableCell(withIdentifier: "CustomTableViewCell", for: indexPath) as! CustomTableViewCell
    
    // 로딩 효과 시작
    cell.startLoading()
    
    // 데이터 로딩 및 설정
    // ...
    
    return cell
}
```

4. 데이터 로딩이 완료되면 해당 셀의 `stopLoading()` 메서드를 호출하여 로딩 효과를 중지합니다.

```swift
// 데이터 로딩 완료 후
cell.stopLoading()
```

## 마무리
이제 Swift에서 NVActivityIndicatorView를 활용하여 테이블뷰 셀에 로딩 효과를 추가하는 방법을 알아보았습니다. 이를 통해 사용자에게 진행 중인 작업을 시각적으로 보여줄 수 있으며, 사용자 경험을 향상시킬 수 있습니다.

## 참고 자료
- [NVActivityIndicatorView GitHub 저장소](https://github.com/ninjaprox/NVActivityIndicatorView)
- [NVActivityIndicatorView 문서](https://ninjaprox.github.io/NVActivityIndicatorView/)
- [Cocoapods 공식 사이트](https://cocoapods.org/)