---
layout: post
title: "Conditional statement with multiple membership operators in Python"
description: " "
date: 2023-09-21
tags: [hashtags, Python, ConditionalStatements]
comments: true
share: true
---

In Python, membership operators are used to test whether a value or variable is present in a sequence, such as a list, tuple, or set. The commonly used membership operators are `in` and `not in`. In some scenarios, you may need to combine multiple membership operators to create complex conditional statements.

Let's take a look at an example of how to use multiple membership operators in a conditional statement in Python:

```python
# Sample list of fruits
fruits = ["apple", "banana", "orange", "kiwi"]

# Check if "banana" is present in the list and "mango" is not present
if "banana" in fruits and "mango" not in fruits:
    print("I love bananas, but I don't like mangoes.")
else:
    print("Either banana is not in the list or mango is in the list.")
```

In the above code snippet, we have a list of `fruits` that contains various fruit names. We are evaluating a conditional statement that checks if "banana" is present in the list using the `in` operator. Additionally, we use the `not in` operator to verify that "mango" is not present in the list. If both conditions are satisfied, the statement inside the `if` block will be executed; otherwise, the code inside the `else` block will run.

This approach allows us to create more complex conditions by combining membership operators. We can add as many operators as needed in order to create the desired condition.

Remember, membership operators work with various data structures in Python, such as lists, tuples, sets, and even strings. So, you can apply these techniques to different scenarios based on your specific requirements.

# Conclusion

Membership operators `in` and `not in` are powerful tools in Python that allow you to test whether a value or variable is present in a sequence. By combining multiple membership operators, you can create more complex conditional statements to suit your needs.

#hashtags: #Python #ConditionalStatements