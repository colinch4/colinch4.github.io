---
layout: post
title: "[swift] 터치 이벤트 처리를 위한 UITableView에서의 UIResponder 사용법"
description: " "
date: 2023-12-07
tags: [swift]
comments: true
share: true
---

UITableView는 iOS 앱에서 많이 사용되는 컴포넌트 중 하나이며, 사용자의 터치 이벤트에 응답할 수 있어야 합니다. 이를 위해 UITableView는 UIResponder를 상속받아 터치 이벤트를 처리할 수 있는 기능을 가지고 있습니다.

UITableView에서의 UIResponder를 사용하는 방법에 대해 알아보겠습니다.

## UITableView를 생성합니다.

우선 UITableView를 생성해야 합니다. UITableView는 UIViewController에 추가되는 subview이므로, UIViewController를 상속받은 클래스에서 UITableView를 선언하고 초기화해야 합니다.

```swift
class ViewController: UIViewController {
    private var tableView: UITableView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        tableView = UITableView(frame: view.bounds)
        view.addSubview(tableView)
    }
}
```

## UIResponder를 상속받은 커스텀 UITableViewCell을 생성합니다.

터치 이벤트를 처리하기 위해서는 UITableViewCell을 커스텀하여 UIResponder를 상속받아야 합니다. UITableViewCell을 상속받은 커스텀 클래스에서 UIResponder를 상속받아 터치 이벤트를 처리할 수 있는 메서드를 구현해야 합니다.

```swift
class CustomTableViewCell: UITableViewCell {
    override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
        super.touchesBegan(touches, with: event)
        
        // 터치 이벤트 처리 로직을 작성합니다.
        // ...
    }
}
```

## 커스텀 UITableViewCell을 사용하는 방법

앞서 생성한 커스텀 UITableViewCell을 사용하여 UITableView에 셀을 추가해봅시다. `tableView(_:cellForRowAt:)` 메서드를 구현하여 셀을 반환하고, 해당 셀에서 터치 이벤트를 처리합니다.

```swift
class ViewController: UIViewController, UITableViewDataSource, UITableViewDelegate {
    private var tableView: UITableView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        tableView = UITableView(frame: view.bounds)
        tableView.dataSource = self
        tableView.delegate = self
        view.addSubview(tableView)
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = CustomTableViewCell()
        return cell
    }
}
```

## 참고자료

- [UITableView - Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uitableview)
- [UITouch - Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uitouch)
- [UIResponder - Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiresponder)