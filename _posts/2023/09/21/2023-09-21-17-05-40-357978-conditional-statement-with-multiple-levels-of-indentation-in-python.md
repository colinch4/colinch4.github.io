---
layout: post
title: "Conditional statement with multiple levels of indentation in Python"
description: " "
date: 2023-09-21
tags: [python, conditionalstatements, code]
comments: true
share: true
---
# Conditional statement with multiple levels of indentation in Python

In Python, you can use conditional statements to control the flow of your code based on certain conditions. These conditions can be simple or complex, and sometimes you may need multiple levels of indentation to express them correctly.

Let's say you want to check if a student has passed their exams based on their scores in different subjects. You can use nested if statements to achieve this.

Here's an example:

```python
# Student's scores
math_score = 75
english_score = 80
science_score = 90

# Checking if the student has passed
if math_score >= 50:
    if english_score >= 50:
        if science_score >= 50:
            print("Congratulations! You passed all subjects!")
        else:
            print("Sorry, you failed in Science.")
    else:
        print("Sorry, you failed in English.")
else:
    print("Sorry, you failed in Math.")
```

In this example, each if statement is nested within the previous one. This allows us to check the scores for each subject one by one. If any subject's score is below the passing threshold of 50, the code will execute the appropriate `else` block.

Nested if statements can be used to handle increasingly complex conditions, making your code more flexible and powerful. However, it's important to keep your code readable and maintainable. If you find yourself nesting too deeply, consider refactoring your code or using alternative approaches, like logical operators (`and`, `or`) or data structures (lists, dictionaries).

Remember to use proper indentation when writing nested if statements, as Python uses indentation to determine code blocks. Consistent indentation makes your code more readable and less prone to syntax errors.

#python #conditionalstatements #code
```

By using proper indentation and organizing your code, you can create complex conditional statements that handle multiple levels of conditions.