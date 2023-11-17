---
layout: post
title: "suppresswarnings unchecked 예제"
description: " "
date: 2023-09-25
tags: [Java]
comments: true
share: true
---
public class UncheckedExample {

    public static void main(String[] args) {
        List<String> names = new ArrayList<>();
        names.add("John");
        names.add("Alice");

        // Warning: Unchecked conversion
        List uncheckedList = names;

        // Suppressing the unchecked warning
        @SuppressWarnings("unchecked")
        List<String> suppressedList = uncheckedList;

        // Accessing elements of the suppressedList does not generate a warning
        for (String name : suppressedList) {
            System.out.println(name);
        }
    }
}
```

In the example above, we have a list of names (`names`) that is of type `ArrayList<String>`. We assign this list to another list called `uncheckedList` without specifying its generic type, which results in an unchecked conversion warning since we are losing type safety.

To suppress this warning, we use the `@SuppressWarnings("unchecked")` annotation before the declaration of `suppressedList`. This tells the compiler to ignore the unchecked conversion warning for this specific line of code.

By using the `@SuppressWarnings("unchecked")` annotation, we are indicating that we are aware of the potential risks of this conversion and taking responsibility for handling any potential type safety issues.

It is important to note that suppressing warnings should be done with caution and only when necessary. It is recommended to provide proper type safety whenever possible.