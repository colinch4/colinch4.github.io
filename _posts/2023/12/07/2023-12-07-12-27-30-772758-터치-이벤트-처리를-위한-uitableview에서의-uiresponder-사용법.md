---
layout: post
title: "[swift] 터치 이벤트 처리를 위한 UITableView에서의 UIResponder 사용법"
description: " "
date: 2023-12-07
tags: [swift]
comments: true
share: true
---

UITableView는 iOS 애플리케이션에서 데이터를 표시하는 데 자주 사용되는 컨트롤입니다. UITableView에서는 사용자의 터치 이벤트를 처리해야 할 경우가 많은데, 이때 UIResponder를 사용하여 터치 이벤트를 처리할 수 있습니다.

## UIResponder란?

UIResponder는 iOS 애플리케이션의 이벤트 처리에 사용되는 추상 클래스입니다. UIView, UIViewController 등은 모두 UIResponder를 상속하고 있으며, 이벤트를 받고 처리할 수 있는 기능을 제공합니다.

## UITableView에서의 UIResponder 사용법

UITableView에서 특정 셀에 터치 이벤트를 처리하려면 다음의 단계를 따를 수 있습니다.

1. UITableViewCell에서 UIResponder를 상속받는 커스텀 클래스를 만듭니다.

```swift
class TouchableCell: UITableViewCell {

    override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
        super.touchesBegan(touches, with: event)
        
        // 터치 이벤트 처리 코드
        // ...
    }
}
```

2. UITableViewDelegate의 `didSelectRowAt` 메서드를 사용하여 특정 셀의 터치 이벤트를 처리합니다.

```swift
func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
    let cell = tableView.cellForRow(at: indexPath) as? TouchableCell
    
    // 터치 이벤트 처리 코드
    // ...
}
```

3. TableViewDelegate의 `willSelectRowAt` 메서드를 사용하여 선택 사전 이벤트를 처리할 수도 있습니다.

```swift
func tableView(_ tableView: UITableView, willSelectRowAt indexPath: IndexPath) -> IndexPath? {
    let cell = tableView.cellForRow(at: indexPath) as? TouchableCell
    
    // 선택 사전 이벤트 처리 코드
    // ...
    
    return indexPath
}
```

## 사용 예제

다음은 UITableViewController의 UITableView에서 터치 이벤트를 처리하는 예제입니다.

```swift
class MyTableViewController: UITableViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        
        tableView.register(TouchableCell.self, forCellReuseIdentifier: "Cell")
    }

    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "Cell", for: indexPath) as! TouchableCell
        
        // 셀 설정
        
        return cell
    }

    override func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        let cell = tableView.cellForRow(at: indexPath) as? TouchableCell
        
        // 터치 이벤트 처리 코드
        // ...
    }
}
```

위의 예제에서는 TouchableCell 클래스를 만들어 UITableViewCell에서 상속받아 특정 셀에 터치 이벤트를 처리하도록 하였습니다. UITableViewDelegate의 `didSelectRowAt` 메서드를 사용하여 특정 셀의 터치 이벤트를 처리하고 있습니다.

이제 UITableView에서 터치 이벤트를 처리하는 방법에 대해 알았습니다. UIResponder를 사용하여 UITableView의 터치 이벤트를 유연하게 처리할 수 있습니다.