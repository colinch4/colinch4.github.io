---
layout: post
title: "[Python] Using variables in lambda functions in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

Lambda functions, also known as anonymous functions, can be a powerful tool in Python. They allow us to create quick and concise functions without defining them using the `def` keyword. One interesting feature of lambda functions is that they can capture and use variables from their surrounding scope. In this blog post, we will explore how to use variables in lambda functions in Python.

## Using Variables in Lambda Functions

To use variables in lambda functions, we need to pass those variables as arguments to the lambda function. The lambda function can then refer to and use those variables within its body. Let's consider the following example:

```python
x = 10
y = 5

multiply = lambda num: num * x * y

result = multiply(2)
print(result)  # Output: 100
```

In this example, we have two variables `x` and `y` defined in the global scope. We have a lambda function `multiply` that takes a single argument `num`. Inside the lambda function, we can access and use the variables `x` and `y` in the expression `num * x * y`. We then call the lambda function with the argument `2` and assign the result to the variable `result`. Finally, we print the value of `result`, which is `100`.

## Capturing Variables from Outer Scope

Lambda functions can access variables from their surrounding scope at the time of their creation. This concept is known as "capturing variables". Let's take a look at an example to understand this better:

```python
def create_multiplier(x):
    return lambda num: num * x

multiply_by_2 = create_multiplier(2)
multiply_by_5 = create_multiplier(5)

result1 = multiply_by_2(3)
result2 = multiply_by_5(4)

print(result1)  # Output: 6
print(result2)  # Output: 20
```

In this example, we define a function `create_multiplier` that takes an argument `x` and returns a lambda function. The lambda function captures the `x` variable from the outer scope and multiplies it with the `num` argument. We then create two instances of the lambda function by calling `create_multiplier` with different arguments: `2` and `5`. We assign the results to `multiply_by_2` and `multiply_by_5`. Finally, we call the lambda functions with different arguments and print the results, which are `6` and `20`, respectively.

## Conclusion

Lambda functions in Python provide a convenient way to create anonymous functions. With the ability to capture and use variables from the surrounding scope, lambda functions become even more versatile. By understanding how to use variables in lambda functions, you can write more concise and expressive code in Python.

I hope you found this blog post helpful! Happy coding!