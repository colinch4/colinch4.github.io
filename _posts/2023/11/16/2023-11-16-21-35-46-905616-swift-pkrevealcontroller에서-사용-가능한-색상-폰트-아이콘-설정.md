---
layout: post
title: "[swift] Swift PKRevealController에서 사용 가능한 색상, 폰트, 아이콘 설정"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

Swift에서 PKRevealController를 사용하여 앱의 슬라이드 메뉴를 구현하는 것은 매우 편리합니다. PKRevealController는 슬라이드 메뉴를 위한 커스텀 컨트롤러를 제공하며, 사용자가 컬러, 폰트, 아이콘 등을 커스터마이징할 수 있습니다.

## 1. 컬러 설정
PKRevealController에서는 백그라운드 컬러, 메뉴 셀 컬러, 텍스트 컬러 등 다양한 컬러를 설정할 수 있습니다. 아래 예제 코드는 각각의 컬러를 설정하는 방법을 보여줍니다.

```swift
// 백그라운드 컬러 설정
revealController.frontViewController.view.backgroundColor = UIColor.white
revealController.leftViewController.view.backgroundColor = UIColor.lightGray

// 메뉴 셀 컬러 설정
let cellColor = UIColor(red: 255/255, green: 110/255, blue: 64/255, alpha: 1)
revealController.leftViewController.view.backgroundColor = cellColor

// 텍스트 컬러 설정
revealController.leftViewController.view.tintColor = UIColor.white
```

## 2. 폰트 설정
슬라이드 메뉴의 텍스트를 변경하거나 폰트를 설정하고자 할 때는 UIFont를 사용하여 폰트를 지정할 수 있습니다.

```swift
let font = UIFont(name: "Arial", size: 16)
let attributes = [NSAttributedString.Key.font: font]
revealController.leftViewController.view.titleTextAttributes = attributes
```

## 3. 아이콘 설정
슬라이드 메뉴에 아이콘을 표시하려면 이미지를 사용하여 UIBarButtonItem을 설정해야 합니다.

```swift
// 왼쪽 메뉴 아이콘 설정
let menuImage = UIImage(named: "menu-icon")
let menuItem = UIBarButtonItem(image: menuImage, style: .plain, target: revealController, action: #selector(PKRevealController.showLeftView))

revealController.navigationItem.leftBarButtonItem = menuItem
```

위의 예제 코드는 각각 컬러, 폰트, 아이콘을 설정하는 방법을 보여줍니다. 이렇게 색상, 폰트 및 아이콘을 사용자 정의함으로써 PKRevealController를 앱의 디자인과 일치시킬 수 있습니다.

더 많은 정보나 예제 코드를 확인하려면 [PKRevealController GitHub 페이지](https://github.com/pkluz/PKRevealController)를 참조하세요.