---
layout: post
title: "Command Processor pattern in Python"
description: " "
date: 2023-10-04
tags: []
comments: true
share: true
---

The Command Processor pattern is a behavioral design pattern that decouples the sender and receiver of a command by encapsulating a request as an object. It allows commands to be parameterized, queued, or logged, and supports undoable operations.

## How it works

At a high level, the Command Processor pattern involves the following components:

- **Command**: This is the interface that declares the method(s) that need to be implemented by concrete command objects. It typically includes an `execute` method that defines the action to be performed.

- **Concrete Command**: This class implements the `Command` interface and defines the specific behavior of the command. It contains a reference to the receiver and invokes the corresponding operation on the receiver when the `execute` method is called.

- **Receiver**: The receiver is the object that actually performs the desired action when a command is executed. It contains the business logic for the operation.

- **Invoker**: The invoker is responsible for invoking the command and managing the execution of commands. It maintains a reference to the command object and calls its `execute` method.

- **Client**: The client creates the command objects and configures them with the appropriate receivers. It also associates the commands with the invoker.

## Example Implementation

Let's consider an example of a command processor to manage a simple text editor. We will have two commands: `InsertCommand` and `DeleteCommand`. The `InsertCommand` inserts a given string at a specific position, while the `DeleteCommand` deletes a portion of the text.

```python
# Command interface
class Command:
    def execute(self):
        pass

# Concrete command: InsertCommand
class InsertCommand(Command):
    def __init__(self, receiver, position, text):
        self.receiver = receiver
        self.position = position
        self.text = text

    def execute(self):
        self.receiver.insert_text(self.position, self.text)

# Concrete command: DeleteCommand
class DeleteCommand(Command):
    def __init__(self, receiver, position, length):
        self.receiver = receiver
        self.position = position
        self.length = length
        self.deleted_text = ""

    def execute(self):
        self.deleted_text = self.receiver.get_text(self.position, self.length)
        self.receiver.delete_text(self.position, self.length)

# Receiver: TextEditor
class TextEditor:
    def __init__(self):
        self.text = ""

    def insert_text(self, position, text):
        self.text = self.text[:position] + text + self.text[position:]

    def delete_text(self, position, length):
        self.text = self.text[:position] + self.text[position+length:]

    def get_text(self, position, length):
        return self.text[position:position+length]

# Invoker
class Invoker:
    def __init__(self):
        self.commands = []

    def set_command(self, command):
        self.commands.append(command)

    def execute_commands(self):
        for command in self.commands:
            command.execute()

# Client
if __name__ == "__main__":
    text_editor = TextEditor()
    invoker = Invoker()

    insert_command = InsertCommand(text_editor, 0, "Hello, ")
    delete_command = DeleteCommand(text_editor, 0, 7)

    invoker.set_command(insert_command)
    invoker.set_command(delete_command)

    invoker.execute_commands()

    print(text_editor.text)  # Output: "World!"
```

In the above example, the `TextEditor` class acts as the receiver, which holds the content of the text. The `InsertCommand` and `DeleteCommand` classes inherit from the `Command` interface and execute the specific actions on the `TextEditor` when their `execute` methods are called.

The `Invoker` class manages a list of commands and can execute them in a sequential order. In this example, we create an `Invoker` instance, set the required commands, and then call `execute_commands` to execute them.

By using the Command Processor pattern, you can easily add new commands and decouple the sender from the receiver, ensuring more flexibility and maintainability in your codebase.

# Conclusion

The Command Processor pattern is a powerful design pattern that decouples the sender and receiver of a command by encapsulating requests as objects. It provides a flexible way to parameterize, queue, and log operations. Additionally, it supports undoing and redoing actions and enables the easy addition of new commands without modifying existing code.