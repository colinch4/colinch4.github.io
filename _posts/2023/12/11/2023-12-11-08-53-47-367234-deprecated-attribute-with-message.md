---
layout: post
title: "[c++] deprecated attribute with message"
description: " "
date: 2023-12-11
tags: [c++]
comments: true
share: true
---
[[deprecated("Please use the new_function instead")]] 
void old_function() {
    // function body
}
```

In this example, the `old_function` is marked as deprecated with a message indicating that `new_function` should be used instead. This is a useful way to provide additional information to developers about the deprecation.

Reference: [GCC documentation - Deprecated attributes](https://gcc.gnu.org/onlinedocs/gcc/Attribute-Syntax.html#Attribute-Syntax)