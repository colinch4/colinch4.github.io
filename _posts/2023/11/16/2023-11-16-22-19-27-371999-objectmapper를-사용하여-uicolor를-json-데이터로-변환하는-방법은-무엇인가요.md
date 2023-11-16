---
layout: post
title: "[swift] ObjectMapper를 사용하여 UIColor를 JSON 데이터로 변환하는 방법은 무엇인가요?"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

Swift에서 ObjectMapper 라이브러리를 사용하면 간단하게 JSON 데이터를 모델 객체로 변환할 수 있습니다. UIColor를 JSON 데이터로 변환하기 위해서는 ObjectMapper를 조금 수정해야 합니다.

먼저, ObjectMapper를 설치하기 위해 프로젝트의 Podfile에 다음과 같이 추가합니다.

```
pod 'ObjectMapper'
```

그런 다음, 터미널에서 `pod install` 명령을 실행하여 라이브러리를 설치합니다.

이제, UIColor를 JSON 데이터로 변환하기 위해 ObjectMapper를 수정해보겠습니다.

```swift
import ObjectMapper

class ColorTransform: TransformType {
    typealias Object = UIColor
    typealias JSON = String
    
    init() {}
    
    func transformFromJSON(_ value: Any?) -> UIColor? {
        if let hexString = value as? String {
            return UIColor(hexString: hexString)
        }
        return nil
    }
    
    func transformToJSON(_ value: UIColor?) -> String? {
        return value?.toHexString()
    }
}

extension UIColor {
    convenience init(hexString: String) {
        let hex = hexString.trimmingCharacters(in: CharacterSet.alphanumerics.inverted)
        var int: UInt32 = 0
        Scanner(string: hex).scanHexInt32(&int)
        let alpha, red, green, blue: UInt32
        switch hex.count {
        case 3: // RGB (12-bit)
            (alpha, red, green, blue) = (255, (int >> 8) * 17, (int >> 4 & 0xF) * 17, (int & 0xF) * 17)
        case 6: // RGB (24-bit)
            (alpha, red, green, blue) = (255, int >> 16, int >> 8 & 0xFF, int & 0xFF)
        default:
            (alpha, red, green, blue) = (255, 0, 0, 0)
        }
        self.init(red: CGFloat(red) / 255, green: CGFloat(green) / 255, blue: CGFloat(blue) / 255, alpha: CGFloat(alpha) / 255)
    }
    
    func toHexString() -> String {
        var red: CGFloat = 0, green: CGFloat = 0, blue: CGFloat = 0, alpha: CGFloat = 0
        self.getRed(&red, green: &green, blue: &blue, alpha: &alpha)
        
        let rgbInt = (Int)(red * 255) << 16 | (Int)(green * 255) << 8 | (Int)(blue * 255) << 0
        return String(format:"#%06x", rgbInt)
    }
}
```

위의 코드에서는 `ColorTransform` 클래스를 생성하여 UIColor와 JSON 사이의 변환을 담당합니다. `transformFromJSON()` 함수는 JSON 값을 UIColor로 변환하고, `transformToJSON()` 함수는 UIColor 값을 JSON 형식으로 변환합니다.

또한, UIColor에는 `hexString`을 사용하여 hex 값을 처리하는 편리한 초기화 메서드와 `toHexString()` 메서드를 추가했습니다.

이제 UIColor 객체를 JSON 데이터로 변환하거나, JSON 데이터를 UIColor로 변환하는 기능을 사용할 수 있습니다.

```swift
let color = UIColor.red
let jsonString = Mapper().toJSONString(color, prettyPrint: true)

print(jsonString) // JSON 데이터 출력: {"hexString":"#ff0000"}

let colorFromJSON = Mapper<UIColor>().map(JSONString: jsonString)
print(colorFromJSON) // UIColor(red: 1.0, green: 0.0, blue: 0.0, alpha: 1.0)
```

위의 예제에서는 UIColor 인스턴스를 JSON 데이터로 변환한 후, 다시 JSON 데이터를 UIColor로 변환하는 과정을 보여줍니다.

이와 같이 ObjectMapper와 UIColor 확장을 사용하여 UIColor를 JSON 데이터로 변환하고, JSON 데이터를 UIColor로 변환할 수 있습니다.