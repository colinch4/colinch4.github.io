---
layout: post
title: "[swift] Swift PKRevealController와의 코어 데이터(Core Data) 연동"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

## 목차
1. [소개](#소개)
2. [코어 데이터 설정](#코어-데이터-설정)
3. [PKRevealController와의 연동](#PKRevealController와의-연동)

## 소개
Swift PKRevealController는 iOS 앱에서 사이드 메뉴를 제공하는 라이브러리입니다. 이 라이브러리를 사용하면 사용자에게 사이드 메뉴를 편리하게 제공할 수 있습니다. 이번 블로그 포스트에서는 Swift PKRevealController와 코어 데이터를 연동하는 방법을 알아보겠습니다.

## 코어 데이터 설정
먼저, 코어 데이터를 사용하려면 앱에서 데이터 모델을 설정해야 합니다. Xcode에서 `File - New - File`을 선택한 후, `Core Data`를 선택하여 데이터 모델을 생성합니다. 데이터 모델에는 엔티티와 속성을 정의할 수 있습니다.

## PKRevealController와의 연동
PKRevealController와 코어 데이터를 연동하기 위해서는 다음과 같은 단계를 따릅니다.
1. AppDelegate.swift 파일을 엽니다.
2. `application(_:didFinishLaunchingWithOptions:)` 메서드 내에 코어 데이터 스택을 초기화하는 코드를 추가합니다.

```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey: Any]?) -> Bool {
    // Core Data Stack 초기화 코드
    CoreDataStack.shared.initializeStack()
    
    // PKRevealController 설정
    let mainViewController = MainViewController()
    let sideMenuViewController = SideMenuViewController()
    let revealController = PKRevealController(frontViewController: mainViewController, leftViewController: sideMenuViewController)
    self.window?.rootViewController = revealController
    self.window?.makeKeyAndVisible()
    
    return true
}
```

3. CoreDataStack.swift 파일을 생성합니다. 이 파일에서는 코어 데이터 스택을 초기화하고 관리하는 코드를 작성합니다.

```swift
import CoreData

class CoreDataStack {
    static let shared = CoreDataStack()
    
    lazy var persistentContainer: NSPersistentContainer = {
        let container = NSPersistentContainer(name: "YourDataModelName")
        container.loadPersistentStores(completionHandler: { (storeDescription, error) in
            if let error = error as NSError? {
                fatalError("Unresolved error \(error), \(error.userInfo)")
            }
        })
        return container
    }()
    
    func initializeStack() {
        _ = persistentContainer
    }
    
    func saveContext() {
        let context = persistentContainer.viewContext
        if context.hasChanges {
            do {
                try context.save()
            } catch {
                let nserror = error as NSError
                fatalError("Unresolved error \(nserror), \(nserror.userInfo)")
            }
        }
    }
}
```

위의 코드에서 "YourDataModelName"은 데이터 모델의 이름으로 대체해야 합니다.

이제 PKRevealController와 코어 데이터를 성공적으로 연동했습니다. 앱을 실행하고 사이드 메뉴를 통해 데이터를 추가하거나 수정하면, 해당 데이터는 코어 데이터에 저장됩니다.

## 결론
이번 블로그 포스트에서는 Swift PKRevealController와 코어 데이터를 연동하는 방법을 알아보았습니다. PKRevealController를 사용하면 앱에 사이드 메뉴를 쉽게 추가할 수 있고, 코어 데이터와 연동하여 데이터를 관리할 수 있습니다. 이를 통해 사용자에게 편리하고 기능적인 앱을 제공할 수 있습니다.