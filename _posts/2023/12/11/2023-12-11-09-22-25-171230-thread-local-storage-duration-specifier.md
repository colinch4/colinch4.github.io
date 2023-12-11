---
layout: post
title: "[c++] Thread-local storage duration specifier"
description: " "
date: 2023-12-11
tags: [c++]
comments: true
share: true
---

```c++
thread_local int tls_var;
```

In the above code, `tls_var` is declared as a thread-local variable. Each thread will have its own `tls_var` variable, and changes made to `tls_var` in one thread will not affect the `tls_var` in another thread.

This can be useful when you want to store thread-specific data, such as thread IDs or thread-local caches.

References:
- [C++ thread_local specifier](https://en.cppreference.com/w/cpp/keyword/thread_local)