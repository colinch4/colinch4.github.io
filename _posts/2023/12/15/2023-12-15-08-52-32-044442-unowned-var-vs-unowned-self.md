---
layout: post
title: "[swift] unowned var vs. unowned self"
description: " "
date: 2023-12-15
tags: [swift]
comments: true
share: true
---

In Swift, `unowned` is a keyword used to define a *strong* reference to an object that doesn't keep a *strong* hold on the object (therefore avoiding retain cycles). However, there can be confusion about whether to use `unowned var` or `unowned self` in certain contexts.

Let's explore the difference between `unowned var` and `unowned self`.

## `unowned var`

When we define a property using `unowned var`, it creates an *optional* reference to the object. It means that this reference can be `nil` if the object it refers to is deallocated. Therefore, it's important to always make sure that this reference is not `nil` before accessing its properties or methods.

Here's an example:

```swift
class Person {
    unowned var spouse: Person?
    
    init(spouse: Person?) {
        self.spouse = spouse
    }
}
```

In this example, the `spouse` is defined as an `unowned var` since the existence of the spouse is not guaranteed.

## `unowned self`

On the other hand, when we use `unowned self` within a closure or completion block, it creates an *unowned* reference to the instance of the class that owns the closure or block. This is helpful in avoiding strong reference cycles between a class instance and a closure or completion block.

Usage example:

```swift
networkManager.fetchData { [unowned self] result in
    // Use self inside the closure
    self.process(result)
}
```

In this example, using `unowned self` avoids a strong reference cycle between `self` and the closure.

## Conclusion

In summary, `unowned var` is used to define an *optional* reference to an object, while `unowned self` is used to avoid strong reference cycles. Both are important features in Swift for managing memory and avoiding retain cycles.

Understanding their differences is crucial for writing efficient and safe code.

References:
- [The Swift Programming Language](https://docs.swift.org/swift-book/LanguageGuide/AutomaticReferenceCounting.html)
- [Managing Strong Reference Cycles](https://docs.swift.org/swift-book/LanguageGuide/AutomaticReferenceCounting.html#ID55)