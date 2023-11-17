---
layout: post
title: "[swift] - AlamofireNetworkActivityIndicator를 사용하여 네트워크 에러 정보를 포함한 알림 기능 추가하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

## 개요
앱에서 네트워크 요청을 할 때 사용자에게 알림을 통해 네트워크 에러 정보를 표시해주는 기능은 매우 유용합니다. 이번 글에서는 Swift 프로젝트에 `AlamofireNetworkActivityIndicator` 라이브러리를 사용하여 네트워크 에러 정보를 포함한 알림 기능을 추가하는 방법에 대해 알아보겠습니다.

## 준비물
- Swift 프로젝트
- Cocoapods (Alamofire 및 AlamofireNetworkActivityIndicator 설치)

## 단계별 진행
1. Cocoapods 설치
   - 터미널을 열고 프로젝트 루트 디렉터리로 이동합니다.
   - `Podfile`을 생성하고 편집합니다.
     ```shell
     $ touch Podfile
     $ open Podfile
     ```
   - `Podfile`에 아래 내용을 추가합니다.
     ```ruby
     platform :ios, '12.0'
     use_frameworks!

     target 'YourProjectName' do
       pod 'Alamofire'
       pod 'AlamofireNetworkActivityIndicator'
     end
     ```
   - 저장하고 터미널에서 아래 명령어를 실행하여 CocoaPods를 설치합니다.
     ```shell
     $ pod install
     ```

2. `AlamofireNetworkActivityIndicator` 사용
   - Xcode에서 프로젝트를 열고 `AppDelegate.swift` 파일을 연 후, 앱 런칭 시 `AlamofireNetworkActivityIndicatorManager.shared.isEnabled`를 호출하여 네트워크 활동 인디케이터를 설정합니다.
      ```swift
      import AlamofireNetworkActivityIndicator

      func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey: Any]?) -> Bool {
          AlamofireNetworkActivityIndicatorManager.shared.isEnabled = true
          return true
      }
      ```
   - 네트워크 요청 시에도 `AlamofireNetworkActivityIndicatorManager.shared.incrementActivityCount()` 를 호출하여 인디케이터를 표시하고, 에러 발생 시에는 `AlamofireNetworkActivityIndicatorManager.shared.decrementActivityCount()`를 호출하여 인디케이터를 숨깁니다.
      ```swift
      AlamofireNetworkActivityIndicatorManager.shared.incrementActivityCount()

      AF.request("https://api.example.com").response { response in
          AlamofireNetworkActivityIndicatorManager.shared.decrementActivityCount()

          if let error = response.error {
              // 에러 발생 시에 알림 창을 표시하고 에러 정보를 포함한 메시지를 보여줍니다.
              let alertController = UIAlertController(title: "Error", message: error.localizedDescription, preferredStyle: .alert)
              alertController.addAction(UIAlertAction(title: "OK", style: .default, handler: nil))
              UIApplication.shared.keyWindow?.rootViewController?.present(alertController, animated: true, completion: nil)
          }
      }
      ```

## 참고 자료
- [AlamofireNetworkActivityIndicator GitHub Repository](https://github.com/Alamofire/AlamofireNetworkActivityIndicator)