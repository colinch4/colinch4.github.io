---
layout: post
title: "[swift] 13. 에러처리(Error Handling)"
description: " "
date: 2020-07-30
tags: [swift]
comments: true
share: true
---

### throw / throws / try
- throw keyword 로 exception 처리를 던질 수 있음. 
- throw 할 수 있는 메소드의 선언에 throws 를 표시하여 알린다.
- throws 가 선언된 메소드를 호출 시에는 try 가 있어야 함.

```swift
enum VendingMachineError: Error {
     case invalidSelection
     case insufficientFunds(coinsNeeded: Int)
     case outOfStock
}

func canThrowErrors() throws -> String {
    throw VendingMachineError.insufficientFunds(coinsNeeded: 5)
}

func func1() throws -> String {
    return try canThrowErrors()
}


do {
    let s = try func1()
    print(s)
}
catch {
    print("catch")
}
```

### do / try / catch
```swift
struct Item {
    var price: Int
    var count: Int
}


class VendingMachine {
    var inventory = [
        "Candy Bar": Item(price: 12, count: 7),
        "Chips": Item(price: 10, count: 4),
        "Pretzels": Item(price: 7, count: 11)
    ]
    var coinsDeposited = 0

    func vend(itemNamed name: String) throws {
        guard let item = inventory[name] else {
            throw VendingMachineError.invalidSelection
        }

        guard item.count > 0 else {
            throw VendingMachineError.outOfStock
        }

        guard item.price <= coinsDeposited else {
            throw VendingMachineError.insufficientFunds(coinsNeeded: item.price - coinsDeposited)
        }

        coinsDeposited -= item.price

        var newItem = item
        newItem.count -= 1
        inventory[name] = newItem

        print("Dispensing \(name)")
    }
}


let favoriteSnacks = [
    "Alice": "Chips",
    "Bob": "Licorice",
    "Eve": "Pretzels",
]
func buyFavoriteSnack(person: String, vendingMachine: VendingMachine) throws {
     let snackName = favoriteSnacks[person] ?? "Candy Bar"
     try vendingMachine.vend(itemNamed: snackName)
}


var vendingMachine = VendingMachine()
vendingMachine.coinsDeposited = 8
do {
    try buyFavoriteSnack(person: "Alice", vendingMachine: vendingMachine)
    print("Success! Yum.")
} catch VendingMachineError.invalidSelection {
    print("Invalid Selection.")
} catch VendingMachineError.outOfStock {
    print("Out of Stock.")
} catch VendingMachineError.insufficientFunds(let coinsNeeded) {
    print("Insufficient funds. Please insert an additional \(coinsNeeded) coins.")
} catch {
    print("Unexpected error: \(error).")
}
// Prints "Insufficient funds. Please insert an additional 2 coins."
```

### try?
- do-try-catch 대신 try? 로 optional 로 변경 가능. 에러가 생긴다면 nil로 반환

```swift
func someThrowingFunction() throws -> Int {
    // ...
}

let x = try? someThrowingFunction()
```

  
### try!
- 에러가 발생하지 않을 것으로 확신하는 경우 사용
```swift
let photo = try! loadImage(atPath: "./Resources/John Appleseed.jpg")
```

### defer
- finally 와 비슷. 더 넓게 사용. 블럭이 끝나기 전에 호출. defer 가 여러 개면 밑에서 부터 시작
```swift
func processFile(filename: String) throws {
    if exists(filename) {
        let file = open(filename)
        defer {
            close(file) // block이 끝나기 직전에 실행, 주로 자원 해제나 정지에 사용
        }
        while let line = try file.readline() {
            // Work with the file.
        }
        // close(file) is called here, at the end of the scope.
    }
}
```
