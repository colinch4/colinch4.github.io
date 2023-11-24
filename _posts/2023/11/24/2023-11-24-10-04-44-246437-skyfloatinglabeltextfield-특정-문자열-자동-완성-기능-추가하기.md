---
layout: post
title: "[swift] SkyFloatingLabelTextField 특정 문자열 자동 완성 기능 추가하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

SkyFloatingLabelTextField는 사용자가 텍스트를 입력하면 라벨이 위로부터 떠오르는 효과를 주는 TextField입니다. 이번에는 SkyFloatingLabelTextField에 특정 문자열의 자동 완성 기능을 추가해보겠습니다.

## 1. 자동 완성 데이터 구성하기
SkyFloatingLabelTextField에 자동 완성 기능을 추가하려면 먼저 자동 완성에 사용할 데이터를 구성해야 합니다. 예를 들어, 이메일 주소의 자동 완성을 구현한다고 가정해봅시다. 다음은 자동 완성에 사용할 이메일 도메인의 리스트입니다.

```swift
let emailDomains = ["gmail.com", "hotmail.com", "yahoo.com", "naver.com"]
```

## 2. 자동 완성 기능 추가하기
SkyFloatingLabelTextField에 자동 완성을 구현하기 위해 아래와 같이 코드를 작성해보겠습니다.

```swift
class AutoCompleteTextField: SkyFloatingLabelTextField {
    override func awakeFromNib() {
        super.awakeFromNib()

        self.addTarget(self, action: #selector(textFieldDidChange(_:)), for: .editingChanged)
    }

    @objc func textFieldDidChange(_ textField: UITextField) {
        guard let text = textField.text else { return }

        var suggestions: [String] = []
        for domain in emailDomains {
            if domain.hasPrefix(text) {
                suggestions.append(domain)
            }
        }

        if suggestions.count > 0 {
            self.inputView = buildAutoCompleteTableView(with: suggestions)
            self.reloadInputViews()
        } else {
            self.inputView = nil
        }
    }

    private func buildAutoCompleteTableView(with suggestions: [String]) -> UITableView {
        let tableView = UITableView()
        tableView.delegate = self
        tableView.dataSource = self
        // Customize the appearance of the table view if needed

        return tableView
    }
}

extension AutoCompleteTextField: UITableViewDelegate, UITableViewDataSource {
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return suggestions.count
    }

    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = UITableViewCell()
        cell.textLabel?.text = suggestions[indexPath.row]

        return cell
    }

    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        self.text = suggestions[indexPath.row]
        self.resignFirstResponder()
    }
}
```

위의 코드는 `AutoCompleteTextField`라는 클래스를 구현하여, `SkyFloatingLabelTextField`를 상속받고 자동 완성 기능을 추가하는 작업을 수행합니다. `textFieldDidChange(_:)` 메소드에서 입력된 텍스트를 이용하여 자동 완성을 위한 제안을 구성하고, `tableView(_:cellForRowAt:)` 메소드에서 제안 리스트를 보여주는 테이블 뷰를 생성합니다.

## 3. 사용하기
위의 작업을 모두 마치면, 자동 완성 기능이 추가된 SkyFloatingLabelTextField를 사용할 준비가 됩니다. 이제 아래와 같이 코드를 작성하여 사용할 수 있습니다.

```swift
let autoCompleteTextField = AutoCompleteTextField()
autoCompleteTextField.placeholder = "이메일 주소"
view.addSubview(autoCompleteTextField)
```

자동 완성이 필요한 TextField에 `AutoCompleteTextField`를 사용하고, `placeholder` 속성을 이용하여 원하는 입력 안내 메시지를 설정할 수 있습니다.

## 결론
이번 포스트에서는 SkyFloatingLabelTextField에 특정 문자열의 자동 완성 기능을 추가하는 방법을 알아보았습니다. 이를 응용하여 다양한 자동 완성 기능을 구현할 수 있으며, 사용자의 편의성을 더욱 높일 수 있습니다.

참고 자료:
- [SkyFloatingLabelTextField GitHub Repository](https://github.com/Skyscanner/SkyFloatingLabelTextField)