---
layout: post
title: "Memento pattern in Python"
description: " "
date: 2023-10-04
tags: [programming]
comments: true
share: true
---

In software development, the Memento pattern is a behavioral design pattern that provides the ability to restore an object to its previous state. This pattern allows the capturing and saving of the internal state of an object without exposing its implementation details, and later restoring the object to that state.

## Understanding the Memento Pattern

The Memento pattern consists of three main components:

1. **Originator**: The object for which we want to save and restore the state.
2. **Memento**: A representation of the saved state of the originator.
3. **Caretaker**: The object responsible for handling the mementos and their storage.

The Memento pattern is useful in scenarios where we need to maintain the state history of an object or implement undo/redo functionality.

## Implementation in Python

Let's illustrate the Memento pattern with a simple example. Consider a text editor that allows users to type text and undo/redo their changes. We can implement this functionality using the Memento pattern.

First, let's define the `Originator` class, which represents the text editor:

```python
class TextEditor:
    def __init__(self):
        self.content = ""

    def write(self, text):
        self.content += text

    def save(self):
        return TextEditorMemento(self.content)

    def restore(self, memento):
        self.content = memento.get_saved_content()
      
    def __str__(self):
        return self.content
```

Next, let's define the `Memento` class, which represents the saved state of the text editor:

```python
class TextEditorMemento:
    def __init__(self, content):
        self.content = content

    def get_saved_content(self):
        return self.content
```

Finally, let's define the `Caretaker` class, which handles the mementos and their storage:

```python
class TextEditorCaretaker:
    def __init__(self):
        self.mementos = []

    def save_memento(self, memento):
        self.mementos.append(memento)

    def get_latest_memento(self):
        if self.mementos:
            return self.mementos[-1]
        else:
            return None
```

## Usage Example

We can now use the implemented Memento pattern to save and restore the state of the text editor:

```python
# Create a TextEditor instance
editor = TextEditor()

# Type some text
editor.write("Hello, ")
editor.write("World!")

# Save the current state
saved_state = editor.save()

# Type more text
editor.write(" This is a memento pattern example.")

# Print the current content
print(editor)  # Output: Hello, World! This is a memento pattern example.

# Restore the previous state
editor.restore(saved_state)

# Print the restored content
print(editor)  # Output: Hello, World!

```

In the example above, we save the state of the `TextEditor` instance using the `save()` method, which returns a `TextEditorMemento`. Later, we can restore the state using the `restore()` method, passing the saved state as a parameter.

## Conclusion

The Memento pattern is a powerful tool for implementing undo/redo functionality or maintaining state history in software applications. It allows objects to save and restore their internal state without exposing implementation details.

By using the Memento pattern, developers can easily implement features like undo/redo, which can greatly improve the user experience of an application.

#programming #python