---
layout: post
title: "[swift] SwiftyUserDefaults vs UserDefaults"
description: " "
date: 2023-11-28
tags: [swift]
comments: true
share: true
---

When working with `UserDefaults` in a Swift project, you have two options - using the traditional `UserDefaults` or using the SwiftyUserDefaults library. In this post, we will compare the two and see which one is a better choice for your project.

## UserDefaults

`UserDefaults` is a simple way to store and retrieve user preferences and small amounts of data in your app. It provides a default instance that you can access globally to save and retrieve values using keys. Here is an example of how you would use `UserDefaults`:

```swift
// Saving a value
UserDefaults.standard.set("John", forKey: "name")

// Retrieving a value
if let name = UserDefaults.standard.string(forKey: "name") {
    print("Name: \(name)")
} else {
    print("Name not found")
}
```

One drawback of using `UserDefaults` is that it requires you to use string keys for storing and retrieving values. This can lead to runtime errors if you mistype the key name.

## SwiftyUserDefaults

SwiftyUserDefaults is a library that provides a type-safe and convenient wrapper around `UserDefaults`. It eliminates the need to use string keys and provides a cleaner and safer way to work with user defaults.

With SwiftyUserDefaults, you define your preference properties as extensions on a custom type conforming to the `UserDefaultsSettable` protocol. Here is an example:

```swift
import SwiftyUserDefaults

extension DefaultsKeys {
    static let name = DefaultsKey<String?>("name")
}

extension UserDefaults: UserDefaultsSettable {
    public static var defaults: UserDefaults {
        return UserDefaults.standard
    }
}

// Saving a value
Defaults[.name] = "John"

// Retrieving a value
if let name = Defaults[.name] {
    print("Name: \(name)")
} else {
    print("Name not found")
}
```

As you can see, the keys are now strongly typed and you no longer need to use string literals. This helps catch any typos or mistakes at compile-time.

Another advantage of SwiftyUserDefaults is that it provides support for more complex types, such as arrays, dictionaries, and custom types, without the need for additional boilerplate code.

## Conclusion

Although `UserDefaults` is sufficient for simple use cases, SwiftyUserDefaults offers a more elegant and type-safe way to work with user defaults. It eliminates the need for string keys and provides a cleaner syntax. If you are working on a project that relies heavily on user defaults, SwiftyUserDefaults can be a great choice to improve the readability and safety of your code.

References:
- [SwiftyUserDefaults GitHub](https://github.com/sunshinejr/SwiftyUserDefaults)
- [UserDefaults Apple Documentation](https://developer.apple.com/documentation/foundation/userdefaults)