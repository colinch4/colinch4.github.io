---
layout: post
title: "Conditional statement with multiple elif statements in Python"
description: " "
date: 2023-09-21
tags: []
comments: true
share: true
---

The syntax for using multiple elif statements is as follows:

```python
if condition1:
    # code block 1
elif condition2:
    # code block 2
elif condition3:
    # code block 3
else:
    # code block if none of the above conditions are met
```

Here's an example to demonstrate the usage of multiple elif statements:

```python
day = input("Enter a day of the week: ")

if day == "Monday":
    print("It's the beginning of the week.")
elif day == "Tuesday" or day == "Wednesday":
    print("It's the middle of the week.")
elif day == "Thursday":
    print("It's almost the weekend.")
elif day == "Friday":
    print("It's finally Friday!")
else:
    print("It's the weekend!")
```

In the above code, the user is prompted to enter a day of the week. Depending on the input, the program will print a corresponding message. If the input matches one of the days in the if, elif, or else statements, the respective code block will be executed. If none of the conditions match, the code block within the else statement will be executed. 

Using multiple elif statements allows you to handle multiple scenarios efficiently and create more complex conditional logic in your Python programs. Remember to **indent** the code within each block properly to ensure correct execution.