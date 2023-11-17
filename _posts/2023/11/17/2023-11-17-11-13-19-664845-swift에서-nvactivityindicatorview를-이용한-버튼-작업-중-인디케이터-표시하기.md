---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView를 이용한 버튼 작업 중 인디케이터 표시하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

인디케이터는 사용자가 작업이 진행 중임을 알려주는 시각적인 표시입니다. NVActivityIndicatorView는 Swift 언어에서 인디케이터를 사용하기 위한 라이브러리입니다. 이 블로그 포스트에서는 NVActivityIndicatorView를 활용하여 버튼 작업 중에 인디케이터를 표시하는 방법에 대해 알아보겠습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 Swift언어로 작성된 인디케이터 라이브러리로, GitHub에서 공개되어 있습니다. 이 라이브러리를 사용하면 다양한 스타일의 인디케이터를 쉽게 구현할 수 있습니다. 또한, 커스터마이징도 가능하여 원하는 디자인의 인디케이터를 만들 수 있습니다.

## NVActivityIndicatorView 설치하기

NVActivityIndicatorView를 설치하려면, Swift Package Manager 또는 Cocoapods를 이용할 수 있습니다.

### Swift Package Manager를 이용한 설치

1. Xcode 프로젝트를 엽니다.
2. 상단 탐색 메뉴에서 `File -> Swift Packages -> Add Package Dependency`를 선택합니다.
3. 패키지 관리자 창에서 다음 URL을 입력합니다.
   ```
   https://github.com/ninjaprox/NVActivityIndicatorView.git
   ```
4. 버전을 선택한 후, 다음을 클릭하여 라이브러리를 추가합니다.

### Cocoapods를 이용한 설치

1. 터미널을 열고 프로젝트 폴더로 이동합니다.
2. `Podfile` 파일을 엽니다.
3. `pod 'NVActivityIndicatorView'`를 `Podfile`에 추가합니다.
4. 터미널에서 `pod update` 명령어를 실행하여 라이브러리를 설치합니다.

## NVActivityIndicatorView 사용하기

NVActivityIndicatorView를 사용하기 위해 다음 단계를 따릅니다.

1. NVActivityIndicatorView를 import합니다.
   ```swift
   import NVActivityIndicatorView
   ```

2. 버튼을 생성하고 이벤트를 처리하는 코드를 작성합니다.
   ```swift
   let button = UIButton(frame: CGRect(x: 100, y: 100, width: 200, height: 50))
   button.setTitle("작업 시작", for: .normal)
   button.addTarget(self, action: #selector(startButtonTapped), for: .touchUpInside)
   self.view.addSubview(button)
   ```

3. 버튼 탭 이벤트를 처리하는 함수를 구현합니다.
   ```swift
   @objc func startButtonTapped() {
       // 인디케이터 표시
       let indicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 40, height: 40))
       indicatorView.type = .ballSpinFadeLoader
       indicatorView.color = .red
       indicatorView.center = button.center
       self.view.addSubview(indicatorView)
       indicatorView.startAnimating()
      
       // 작업 수행
       // 인디케이터 작업 후 필요한 코드를 작성하세요.
   }
   ```

4. 작업이 완료된 후, 인디케이터를 제거합니다.
   ```swift
   indicatorView.stopAnimating()
   indicatorView.removeFromSuperview()
   ```

위 코드를 참고하여, 버튼을 터치할 때 인디케이터를 표시하고 작업을 수행한 후 인디케이터를 제거하는 기능을 구현할 수 있습니다.

## 마치며

이번 포스트에서는 Swift에서 NVActivityIndicatorView를 사용하여 버튼 작업 중에 인디케이터를 표시하는 방법에 대해 알아보았습니다. NVActivityIndicatorView는 다양한 스타일의 인디케이터를 제공하며, 커스터마이징도 가능합니다. 버튼 작업 중에 인디케이터를 통해 사용자에게 진행 중임을 알려주면, 사용자 경험을 개선할 수 있습니다.

더 자세한 사항은 [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)를 참조하시기 바랍니다.