---
layout: post
title: "[lib] Reachability란?"
description: " "
date: 2021-05-14
tags: [swift]
comments: true
share: true
---

## Reachability    
네트워크의 상태를 파악할 때 사용하는 라이브러리    

## 사용법
cocoapod 설치           
```swift
source 'https://github.com/CocoaPods/Specs.git'
platform :ios, '10.0'
use_frameworks!

target 'MyApp' do
  pod 'ReachabilitySwift'
end
```   

기본 사용법              
```swift
import Reachability

//declare this property where it won't go out of scope relative to your listener
let reachability = try! Reachability()

reachability.whenReachable = { reachability in
    if reachability.connection == .wifi {
        print("Reachable via WiFi")
    } else {
        print("Reachable via Cellular")
    }
}
reachability.whenUnreachable = { _ in
    print("Not reachable")
}

do {
    try reachability.startNotifier()
} catch {
    print("Unable to start notifier")
}
```    

## Reachability git 주소       

https://github.com/ashleymills/Reachability.swift
