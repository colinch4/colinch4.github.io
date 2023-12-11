---
layout: post
title: "[c++] Non-type template parameters with auto"
description: " "
date: 2023-12-11
tags: [c++]
comments: true
share: true
---

In C++, non-type template parameters allow you to pass values as template arguments. This feature has been enhanced in C++17 with the introduction of the auto keyword, which simplifies the declaration of non-type template parameters. In this post, we will explore how to use auto in non-type template parameters and discuss its benefits.

## Introduction to non-type template parameters

Non-type template parameters are used to specify types, integral values, or pointers as template arguments. Prior to C++17, you had to explicitly specify the data type of the non-type template parameter when defining a template. For example:
```c++
template <int N>
class MyClass {
    // ...
};
```
In this example, the template parameter N is an integer of type int.

## Using auto with non-type template parameters

With C++17, the auto keyword can be used as part of the declaration of non-type template parameters, allowing the type of the parameter to be deduced from the provided argument. For instance:
```c++
template <auto N>
class MyClass {
    // ...
};
```
In this case, the type of the non-type template parameter N will be automatically deduced from the argument passed when instantiating the template. This can greatly simplify the code, as you don't need to explicitly specify the type when defining the template.

## Benefits of auto in non-type template parameters

Using auto with non-type template parameters offers several benefits, such as:
- Simplifying the code and reducing the need for explicit type declarations.
- Allowing for cleaner and more concise template definitions.
- Enabling the use of more complex types, such as user-defined types, as non-type template parameters.

## Example

Let's consider an example where the auto keyword is used with a non-type template parameter to create a generic array class:
```c++
template <typename T, auto N>
class Array {
private:
    T data[N];
public:
    // ...
};
```
In this example, the size of the array is specified as a non-type template parameter using the auto keyword, allowing the array class to be instantiated with various sizes without explicitly specifying the data type.

## Conclusion

In conclusion, the introduction of the auto keyword for non-type template parameters in C++17 simplifies the handling of template classes and functions by allowing the type of the parameter to be deduced from the provided argument. This can lead to cleaner and more concise code, as well as greater flexibility in the use of non-type template parameters.

For further details, you can refer to the [C++ reference documentation](https://en.cppreference.com/w/cpp/language/auto).

Now that you have learned about using auto in non-type template parameters, you can take advantage of this powerful feature to enhance your C++ template programming.