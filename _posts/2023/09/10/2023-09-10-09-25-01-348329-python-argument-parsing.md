---
layout: post
title: "[Python] Argument parsing"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

In Python, **argument parsing** refers to the process of extracting information or data from the command line when running a Python script. It allows you to pass values or options to your script, controlling its behavior and functionality.

The **argparse** module in Python provides an easy way to parse command-line arguments and options. It can handle various types of arguments, such as **positional arguments**, **optional arguments**, and **flags**.

Let's dive into some examples to learn how to use `argparse` effectively.

## Basic Argument Parsing

```python
import argparse

# Create the parser
parser = argparse.ArgumentParser(description='Process some integers.')

# Add a positional argument
parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')

# Parse the arguments
args = parser.parse_args()
print(args.integers)
```

In this example, we create an `argparse.ArgumentParser` object and define a positional argument `integers`. The `metavar` parameter is used to specify the name shown in the help messages. The `nargs` parameter is set to `'+'`, which means the argument takes one or more values.

When running the script, we can provide one or more integer values as arguments:

```bash
$ python script.py 1 2 3
[1, 2, 3]
```

## Optional Arguments

```python
import argparse

# Create the parser
parser = argparse.ArgumentParser(description='Process some numbers.')

# Add optional arguments
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max, help='sum the numbers (default: find the max)')

# Parse the arguments
args = parser.parse_args()
print(args.accumulate(args.integers))
```

In this example, we introduce an optional argument `--sum`. The `store_const` action is used to store the value `sum` in the `accumulate` attribute of the `args` object if the `--sum` option is provided. Otherwise, it defaults to the `max` function.

```bash
$ python script.py 1 2 3 --sum
6
$ python script.py 1 2 3
3
```

## Flags

```python
import argparse

# Create the parser
parser = argparse.ArgumentParser()

# Add a flag
parser.add_argument('--verbose', action='store_true', help='increase output verbosity')

# Parse the arguments
args = parser.parse_args()
if args.verbose:
    print('Verbose mode activated.')
```

In this example, we add a flag `--verbose`. The `store_true` action is used to set the value of the `args.verbose` attribute to `True` when the flag is provided.

```bash
$ python script.py --verbose
Verbose mode activated.
```

## Conclusion

Using the `argparse` module in Python, you can easily handle argument parsing in your scripts. It provides a convenient and standardized way to extract information from the command line, making your scripts more flexible and user-friendly.

Remember to import the `argparse` module and follow its syntax to define and parse the arguments. This will help you create robust and versatile Python scripts.