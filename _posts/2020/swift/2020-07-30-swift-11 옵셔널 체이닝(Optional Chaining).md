---
layout: post
title: "11. 옵셔널 체이닝(Optional Chaining) "
description: " "
date: 2020-07-30
tags: [swift]
comments: true
share: true
---

### nil 을 가질 수 있는 value에 "?" 를 붙인다. 
```swift
class Person {
    var residence: Residence?
}

class Residence {
    var numberOfRooms = 1
}
```

### 강제 unwrapping 
"!"를 붙여 unwrapping 가능
```swift
class Person {
    var residence: Residence?
}

class Residence {
    var numberOfRooms = 1
}


let john = Person()
// residence는 nil


let roomCount = john.residence!.numberOfRooms
// this triggers a runtime error
```

### 옵셔널 체이닝 접근
```swift
if let roomCount = john.residence?.numberOfRooms {
    print("John's residence has \(roomCount) room(s).")
} else {
    print("Unable to retrieve the number of rooms.")
}
// Prints "Unable to retrieve the number of rooms."


// 메소드의 반환값이 optional인 경우 ()? 로 접근
if let beginsWithThe =
    john.residence?.address?.buildingIdentifier()?.hasPrefix("The") {
    if beginsWithThe {
        print("John's building identifier begins with \"The\".")
    } else {
        print("John's building identifier does not begin with \"The\".")
}
}
// Prints "John's building identifier begins with "The"."
```
