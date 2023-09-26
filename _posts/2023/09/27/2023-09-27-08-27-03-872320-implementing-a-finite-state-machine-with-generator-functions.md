---
layout: post
title: "Implementing a finite state machine with generator functions"
description: " "
date: 2023-09-27
tags: [Python]
comments: true
share: true
---

Finite state machines (FSMs) are powerful tools for modeling and controlling systems with discrete states. Traditionally, FSMs are implemented using imperative programming techniques. However, with the introduction of generator functions in modern programming languages, we can now implement FSMs in a more elegant and concise way.

In this blog post, we will explore how to implement a finite state machine using generator functions in Python.

## What is a Finite State Machine?

A finite state machine is a mathematical model used to describe the behavior of a system with a finite number of states and transitions between those states. It can be represented as a directed graph, where each node represents a state and each edge represents a transition.

## Generator Functions in Python

Python introduced the concept of generator functions, which allow us to define a function that behaves like an iterator. Unlike regular functions that return a value and exit, generator functions can *yield* multiple values over time, pausing execution each time a value is yielded.

Generator functions are denoted by the `yield` keyword instead of `return` keyword. When a generator function is called, it returns a generator object. We can iterate over the generator object to obtain the values yielded by the function.

## Implementing a Finite State Machine with Generator Functions

To implement a finite state machine using generator functions, we can define each state and transition as a separate generator function. Each transition function can yield the next state, effectively controlling the flow of execution.

Here's an example implementation of a simple FSM that models a light switch:

```python
def fsm():
    while True:
        state = yield  # the state is yielded to the caller

        if state == 'off':
            print("The light is off")
            state = yield 'on'  # transition to the 'on' state
        elif state == 'on':
            print("The light is on")
            state = yield 'off'  # transition to the 'off' state
```

In the example above, the `fsm` generator function defines two states: 'off' and 'on'. Depending on the current state, it prints a corresponding message, and then yields the next state as the result of the `yield` statement. The yielded state is received by the caller and passed back into the generator function on the next iteration.

We can use the FSM by creating a generator object from the `fsm` function and iterating over it. Each time we call `send`, the current state is passed into the generator function, and the yielded state is returned.

```python
fsm_generator = fsm()
current_state = next(fsm_generator)  # initialize the generator
print(current_state)  # prints 'None'

current_state = fsm_generator.send('off')  # transition to the 'on' state
print(current_state)  # prints 'on'

current_state = fsm_generator.send('on')  # transition to the 'off' state
print(current_state)  # prints 'off'
```

The example above demonstrates how we can control the FSM by sending input values to the generator function and obtaining the resulting states.

## Conclusion

Generator functions present a concise and expressive way to implement finite state machines. By leveraging the power of generators, we can model complex state-based systems in a more readable and maintainable manner.

Finite state machines implemented with generator functions are not only easier to understand, but they also provide better control flow and flexibility. They can be used in various domains, such as game development, natural language processing, and event-driven systems.

With this approach, you can efficiently implement and maintain finite state machines in your projects, achieving clean and modular code.

# Programming #Python #FSM