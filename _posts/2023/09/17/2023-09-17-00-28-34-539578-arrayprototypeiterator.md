---
layout: post
title: "Array.prototype[@@iterator]()"
description: " "
date: 2023-09-17
tags: [JavaScript, Array, Iterator]
comments: true
share: true
---

## Example usage

Consider the following example:

```javascript
const fruits = ['apple', 'banana', 'cherry'];

const iterator = fruits[Symbol.iterator]();

console.log(iterator.next().value); // Output: 'apple'
console.log(iterator.next().value); // Output: 'banana'
console.log(iterator.next().value); // Output: 'cherry'
console.log(iterator.next().value); // Output: undefined
```

In the above code snippet, we create an array `fruits` containing three elements. We then call `fruits[Symbol.iterator]()` to get the iterator object. Finally, we use the `next()` method on the iterator object to move through the array and print the corresponding values.

## Conclusion

The `Array.prototype[@@iterator]()` method is a powerful tool for iterating over the elements of an array. It provides a convenient way to loop through the array without having to rely on traditional `for` or `while` loops. By using this method, you can easily access and manipulate the values stored in an array, enhancing the functionality and versatility of your JavaScript code.

#JavaScript #Array #Iterator