---
layout: post
title: "[c++] Extended friend declarations"
description: " "
date: 2023-12-11
tags: [c++]
comments: true
share: true
---

In C++, the `friend` keyword allows a function or a class to access the private and protected members of another class. In some cases, you may need to provide access to private or protected members to a large number of functions or classes. **Extended friend declarations** come in handy in such situations.

## What are Extended Friend Declarations?

Extended friend declarations allow an external class or function to access the private or protected members of the declaring class and also its derived classes. This provides a way to grant access to a wider set of classes or functions than just the immediate friend. To use extended friend declarations, the `friend` keyword is followed by a class name or a function which is already a friend, and a scope resolution operator to specify the class or the function that is allowed access. 

## Example

Consider a base class `Base` and a derived class `Derived`. We want the class `Other` to access the private members of `Base` and `Derived`. Here's how we can achieve this using extended friend declarations:

```c++
class Base {
private:
    int privateData;
    friend class Other; // Extended friend declaration
};

class Derived : public Base {
private:
    int morePrivateData;
    friend class Other; // Extended friend declaration
};

class Other {
public:
    void accessPrivateMembers(Base &baseObj) {
        // Access private members of Base using baseObj
        std::cout << baseObj.privateData;
    }

    void accessPrivateMembers(Derived &derivedObj) {
        // Access private members of Derived using derivedObj
        std::cout << derivedObj.privateData << ", " << derivedObj.morePrivateData;
    }
};
```

In this example, the `Other` class is granted access to the private members of both `Base` and `Derived` through extended friend declarations.

## Advantages of Extended Friend Declarations

- **Simplified Access Control**: Extended friend declarations provide an efficient way to manage access to private and protected members for classes and functions that are not part of the same hierarchy.

- **Flexibility**: It enables fine-grained control over which specific classes or functions can access the private and protected members.

## Conclusion

Extended friend declarations in C++ allow classes and functions to access the private and protected members of a class and its derived classes. They provide a flexible and convenient way to manage access control in complex scenarios.

References:
- [C++ Extended Friend Declarations](https://en.cppreference.com/w/cpp/language/friend)