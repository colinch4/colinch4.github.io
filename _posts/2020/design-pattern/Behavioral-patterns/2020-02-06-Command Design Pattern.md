---
layout: post
title: "[Design Pattern] Command"
description: "Command is a behavioral design pattern that turns a request into a stand-alone object that contains all information about the request. This transformation lets you parameterize methods with different requests, delay or queue a request’s execution, and support undoable operations."
date: 2020-02-06 14:02
tags: [디자인패턴]
comments: true
share: true
---

/  [Design Patterns](https://refactoring.guru/design-patterns)  /  [Behavioral Patterns](https://refactoring.guru/design-patterns/behavioral-patterns)

#### Also known as:  Action,­Transaction

## Intent

**Command**  is a behavioral design pattern that turns a request into a stand-alone object that contains all information about the request. This transformation lets you parameterize methods with different requests, delay or queue a request’s execution, and support undoable operations.

![Command design pattern](https://refactoring.guru/images/patterns/content/command/command.png)

## Problem

Imagine that you’re working on a new text-editor app. Your current task is to create a toolbar with a bunch of buttons for various operations of the editor. You created a very neat  `Button`  class that can be used for buttons on the toolbar, as well as for generic buttons in various dialogs.

![Problem solved by the Command pattern](https://refactoring.guru/images/patterns/diagrams/command/problem1.png)

All buttons of the app are derived from the same class.

While all of these buttons look similar, they’re all supposed to do different things. Where would you put the code for the various click handlers of these buttons? The simplest solution is to create tons of subclasses for each place where the button is used. These subclasses would contain the code that would have to be executed on a button click.

![Lots of button subclasses](https://refactoring.guru/images/patterns/diagrams/command/problem2.png)

Lots of button subclasses. What can go wrong?

Before long, you realize that this approach is deeply flawed. First, you have an enormous number of subclasses, and that would be okay if you weren’t risking breaking the code in these subclasses each time you modify the base  `Button`  class. Put simply, your GUI code has become awkwardly dependent on the volatile code of the business logic.

![Several classes implement the same functionality](https://refactoring.guru/images/patterns/diagrams/command/problem3.png)

Several classes implement the same functionality.

And here’s the ugliest part. Some operations, such as copying/pasting text, would need to be invoked from multiple places. For example, a user could click a small “Copy” button on the toolbar, or copy something via the context menu, or just hit  `Ctrl+C`  on the keyboard.

Initially, when our app only had the toolbar, it was okay to place the implementation of various operations into the button subclasses. In other words, having the code for copying text inside the  `CopyButton`  subclass was fine. But then, when you implement context menus, shortcuts, and other stuff, you have to either duplicate the operation’s code in many classes or make menus dependent on buttons, which is an even worse option.

## Solution

Good software design is often based on the principle of separation of concerns, which usually results in breaking an app into layers. The most common example: a layer for the graphical user interface and another layer for the business logic. The GUI layer is responsible for rendering a beautiful picture on the screen, capturing any input and showing results of what the user and the app are doing. However, when it comes to doing something important, like calculating the trajectory of the moon or composing an annual report, the GUI layer delegates the work to the underlying layer of business logic.

In the code it might look like this: a GUI object calls a method of a business logic object, passing it some arguments. This process is usually described as one object sending another a  _request_.

![The GUI layer may access the business logic layer directly](https://refactoring.guru/images/patterns/diagrams/command/solution1-en.png)

The GUI objects may access the business logic objects directly.

The Command pattern suggests that GUI objects shouldn’t send these requests directly. Instead, you should extract all of the request details, such as the object being called, the name of the method and the list of arguments into a separate  _command_  class with a single method that triggers this request.

Command objects serve as links between various GUI and business logic objects. From now on, the GUI object doesn’t need to know what business logic object will receive the request and how it’ll be processed. The GUI object just triggers the command, which handles all the details.

![Accessing the business logic layer via a command.](https://refactoring.guru/images/patterns/diagrams/command/solution2-en.png)

Accessing the business logic layer via a command.

The next step is to make your commands implement the same interface. Usually it has just a single execution method that takes no parameters. This interface lets you use various commands with the same request sender, without coupling it to concrete classes of commands. As a bonus, now you can switch command objects linked to the sender, effectively changing the sender’s behavior at runtime.

You might have noticed one missing piece of the puzzle, which is the request parameters. A GUI object might have supplied the business-layer object with some parameters. Since the command execution method doesn’t have any parameters, how would we pass the request details to the receiver? It turns out the command should be either pre-configured with this data, or capable of getting it on its own.

![The GUI objects delegate the work to commands](https://refactoring.guru/images/patterns/diagrams/command/solution3.png)

The GUI objects delegate the work to commands.

Let’s get back to our text editor. After we apply the Command pattern, we no longer need all those button subclasses to implement various click behaviors. It’s enough to put a single field into the base  `Button`  class that stores a reference to a command object and make the button execute that command on a click.

You’ll implement a bunch of command classes for every possible operation and link them with particular buttons, depending on the buttons’ intended behavior.

Other GUI elements, such as menus, shortcuts or entire dialogs, can be implemented in the same way. They’ll be linked to a command which gets executed when a user interacts with the GUI element. As you’ve probably guessed by now, the elements related to the same operations will be linked to the same commands, preventing any code duplication.

As a result, commands become a convenient middle layer that reduces coupling between the GUI and business logic layers. And that’s only a fraction of the benefits that the Command pattern can offer!

## Real-World Analogy

![Making an order in a restaurant](https://refactoring.guru/images/patterns/content/command/command-comic-1.png)

Making an order in a restaurant.

After a long walk through the city, you get to a nice restaurant and sit at the table by the window. A friendly waiter approaches you and quickly takes your order, writing it down on a piece of paper. The waiter goes to the kitchen and sticks the order on the wall. After a while, the order gets to the chef, who reads it and cooks the meal accordingly. The cook places the meal on a tray along with the order. The waiter discovers the tray, checks the order to make sure everything is as you wanted it, and brings everything to your table.

The paper order serves as a command. It remains in a queue until the chef is ready to serve it. The order contains all the relevant information required to cook the meal. It allows the chef to start cooking right away instead of running around clarifying the order details from you directly.

## Structure

![Structure of the Command design pattern](https://refactoring.guru/images/patterns/diagrams/command/structure.png)

1.  The  **Sender**  class (aka  _invoker_) is responsible for initiating requests. This class must have a field for storing a reference to a command object. The sender triggers that command instead of sending the request directly to the receiver. Note that the sender isn’t responsible for creating the command object. Usually, it gets a pre-created command from the client via the constructor.
    
2.  The  **Command**  interface usually declares just a single method for executing the command.
    
3.  **Concrete Commands**  implement various kinds of requests. A concrete command isn’t supposed to perform the work on its own, but rather to pass the call to one of the business logic objects. However, for the sake of simplifying the code, these classes can be merged.
    
    Parameters required to execute a method on a receiving object can be declared as fields in the concrete command. You can make command objects immutable by only allowing the initialization of these fields via the constructor.
    
4.  The  **Receiver**  class contains some business logic. Almost any object may act as a receiver. Most commands only handle the details of how a request is passed to the receiver, while the receiver itself does the actual work.
    
5.  The  **Client**  creates and configures concrete command objects. The client must pass all of the request parameters, including a receiver instance, into the command’s constructor. After that, the resulting command may be associated with one or multiple senders.
    

## Pseudocode

In this example, the  **Command**  pattern helps to track the history of executed operations and makes it possible to revert an operation if needed.

![Structure of the Command pattern example](https://refactoring.guru/images/patterns/diagrams/command/example.png)

Undoable operations in a text editor.

Commands which result in changing the state of the editor (e.g., cutting and pasting) make a backup copy of the editor’s state before executing an operation associated with the command. After a command is executed, it’s placed into the command history (a stack of command objects) along with the backup copy of the editor’s state at that point. Later, if the user needs to revert an operation, the app can take the most recent command from the history, read the associated backup of the editor’s state, and restore it.

The client code (GUI elements, command history, etc.) isn’t coupled to concrete command classes because it works with commands via the command interface. This approach lets you introduce new commands into the app without breaking any existing code.

```java
// The base command class defines the common interface for all
// concrete commands.
abstract class Command is
    protected field app: Application
    protected field editor: Editor
    protected field backup: text

    constructor Command(app: Application, editor: Editor) is
        this.app = app
        this.editor = editor

    // Make a backup of the editor's state.
    method saveBackup() is
        backup = editor.text

    // Restore the editor's state.
    method undo() is
        editor.text = backup

    // The execution method is declared abstract to force all
    // concrete commands to provide their own implementations.
    // The method must return true or false depending on whether
    // the command changes the editor's state.
    abstract method execute()

// The concrete commands go here.
class CopyCommand extends Command is
    // The copy command isn't saved to the history since it
    // doesn't change the editor's state.
    method execute() is
        app.clipboard = editor.getSelection()
        return false

class CutCommand extends Command is
    // The cut command does change the editor's state, therefore
    // it must be saved to the history. And it'll be saved as
    // long as the method returns true.
    method execute() is
        saveBackup()
        app.clipboard = editor.getSelection()
        editor.deleteSelection()
        return true

class PasteCommand extends Command is
    method execute() is
        saveBackup()
        editor.replaceSelection(app.clipboard)
        return true

// The undo operation is also a command.
class UndoCommand extends Command is
    method execute() is
        app.undo()
        return false

// The global command history is just a stack.
class CommandHistory is
    private field history: array of Command

    // Last in...
    method push(c: Command) is
        // Push the command to the end of the history array.

    // ...first out
    method pop():Command is
        // Get the most recent command from the history.

// The editor class has actual text editing operations. It plays
// the role of a receiver: all commands end up delegating
// execution to the editor's methods.
class Editor is
    field text: string

    method getSelection() is
        // Return selected text.

    method deleteSelection() is
        // Delete selected text.

    method replaceSelection(text) is
        // Insert the clipboard's contents at the current
        // position.

// The application class sets up object relations. It acts as a
// sender: when something needs to be done, it creates a command
// object and executes it.
class Application is
    field clipboard: string
    field editors: array of Editors
    field activeEditor: Editor
    field history: CommandHistory

    // The code which assigns commands to UI objects may look
    // like this.
    method createUI() is
        // ...
        copy = function() { executeCommand(
            new CopyCommand(this, activeEditor)) }
        copyButton.setCommand(copy)
        shortcuts.onKeyPress("Ctrl+C", copy)

        cut = function() { executeCommand(
            new CutCommand(this, activeEditor)) }
        cutButton.setCommand(cut)
        shortcuts.onKeyPress("Ctrl+X", cut)

        paste = function() { executeCommand(
            new PasteCommand(this, activeEditor)) }
        pasteButton.setCommand(paste)
        shortcuts.onKeyPress("Ctrl+V", paste)

        undo = function() { executeCommand(
            new UndoCommand(this, activeEditor)) }
        undoButton.setCommand(undo)
        shortcuts.onKeyPress("Ctrl+Z", undo)

    // Execute a command and check whether it has to be added to
    // the history.
    method executeCommand(command) is
        if (command.execute)
            history.push(command)

    // Take the most recent command from the history and run its
    // undo method. Note that we don't know the class of that
    // command. But we don't have to, since the command knows
    // how to undo its own action.
    method undo() is
        command = history.pop()
        if (command != null)
            command.undo()
```

## Applicability

Use the Command pattern when you want to parametrize objects with operations.

The Command pattern can turn a specific method call into a stand-alone object. This change opens up a lot of interesting uses: you can pass commands as method arguments, store them inside other objects, switch linked commands at runtime, etc.

Here’s an example: you’re developing a GUI component such as a context menu, and you want your users to be able to configure menu items that trigger operations when an end user clicks an item.

Use the Command pattern when you want to queue operations, schedule their execution, or execute them remotely.

As with any other object, a command can be serialized, which means converting it to a string that can be easily written to a file or a database. Later, the string can be restored as the initial command object. Thus, you can delay and schedule command execution. But there’s even more! In the same way, you can queue, log or send commands over the network.

Use the Command pattern when you want to implement reversible operations.

Although there are many ways to implement undo/redo, the Command pattern is perhaps the most popular of all.

To be able to revert operations, you need to implement the history of performed operations. The command history is a stack that contains all executed command objects along with related backups of the application’s state.

This method has two drawbacks. First, it isn’t that easy to save an application’s state because some of it can be private. This problem can be mitigated with the  [Memento](https://refactoring.guru/design-patterns/memento)  pattern.

Second, the state backups may consume quite a lot of RAM. Therefore, sometimes you can resort to an alternative implementation: instead of restoring the past state, the command performs the inverse operation. The reverse operation also has a price: it may turn out to be hard or even impossible to implement.

## How to Implement

1.  Declare the command interface with a single execution method.
    
2.  Start extracting requests into concrete command classes that implement the command interface. Each class must have a set of fields for storing the request arguments along with a reference to the actual receiver object. All these values must be initialized via the command’s constructor.
    
3.  Identify classes that will act as  _senders_. Add the fields for storing commands into these classes. Senders should communicate with their commands only via the command interface. Senders usually don’t create command objects on their own, but rather get them from the client code.
    
4.  Change the senders so they execute the command instead of sending a request to the receiver directly.
    
5.  The client should initialize objects in the following order:
    
    -   Create receivers.
    -   Create commands, and associate them with receivers if needed.
    -   Create senders, and associate them with specific commands.

## Pros and Cons

-   _Single Responsibility Principle_. You can decouple classes that invoke operations from classes that perform these operations.
-   _Open/Closed Principle_. You can introduce new commands into the app without breaking existing client code.
-   You can implement undo/redo.
-   You can implement deferred execution of operations.
-   You can assemble a set of simple commands into a complex one.

-   The code may become more complicated since you’re introducing a whole new layer between senders and receivers.

## Relations with Other Patterns

-   [Chain of Responsibility](https://refactoring.guru/design-patterns/chain-of-responsibility),  [Command](https://refactoring.guru/design-patterns/command),  [Mediator](https://refactoring.guru/design-patterns/mediator)  and  [Observer](https://refactoring.guru/design-patterns/observer)  address various ways of connecting senders and receivers of requests:
    
    -   _Chain of Responsibility_  passes a request sequentially along a dynamic chain of potential receivers until one of them handles it.
    -   _Command_  establishes unidirectional connections between senders and receivers.
    -   _Mediator_  eliminates direct connections between senders and receivers, forcing them to communicate indirectly via a mediator object.
    -   _Observer_  lets receivers dynamically subscribe to and unsubscribe from receiving requests.
-   Handlers in  [Chain of Responsibility](https://refactoring.guru/design-patterns/chain-of-responsibility)  can be implemented as  [Commands](https://refactoring.guru/design-patterns/command). In this case, you can execute a lot of different operations over the same context object, represented by a request.
    
    However, there’s another approach, where the request itself is a  _Command_  object. In this case, you can execute the same operation in a series of different contexts linked into a chain.
    
-   You can use  [Command](https://refactoring.guru/design-patterns/command)  and  [Memento](https://refactoring.guru/design-patterns/memento)  together when implementing “undo”. In this case, commands are responsible for performing various operations over a target object, while mementos save the state of that object just before a command gets executed.
    
-   [Command](https://refactoring.guru/design-patterns/command)  and  [Strategy](https://refactoring.guru/design-patterns/strategy)  may look similar because you can use both to parameterize an object with some action. However, they have very different intents.
    
    -   You can use  _Command_  to convert any operation into an object. The operation’s parameters become fields of that object. The conversion lets you defer execution of the operation, queue it, store the history of commands, send commands to remote services, etc.
        
    -   On the other hand,  _Strategy_  usually describes different ways of doing the same thing, letting you swap these algorithms within a single context class.
        
-   [Prototype](https://refactoring.guru/design-patterns/prototype)  can help when you need to save copies of  [Commands](https://refactoring.guru/design-patterns/command)  into history.
    
-   You can treat  [Visitor](https://refactoring.guru/design-patterns/visitor)  as a powerful version of the  [Command](https://refactoring.guru/design-patterns/command)  pattern. Its objects can execute operations over various objects of different classes.

## Code Example 
**Command**  is behavioral design pattern that converts requests or simple operations into objects.

The conversion allows deferred or remote execution of commands, storing command history, etc.

[Learn more about Command](https://refactoring.guru/design-patterns/command)

## Usage of the pattern in Java

**Complexity:**

**Popularity:**

**Usage examples:**  The Command pattern is pretty common in Java code. Most often it’s used as an alternative for callbacks to parameterizing UI elements with actions. It’s also used for queueing tasks, tracking operations history, etc.

Here are some examples of Commands in core Java libraries:

-   All implementations of  [`java.lang.Runnable`](http://docs.oracle.com/javase/8/docs/api/java/lang/Runnable.html)
    
-   All implemantations of  [`javax.swing.Action`](http://docs.oracle.com/javase/8/docs/api/javax/swing/Action.html)
    

**Identification:**  The Command pattern is recognizable by behavioral methods in an abstract/interface type (sender) which invokes a method in an implementation of a different abstract/interface type (receiver) which has been encapsulated by the command implementation during its creation. Command classes are usually limited to specific actions.

## Text editor commands and undo

The text editor in this example creates new command objects each time a user interacts with it. After executing its actions, a command is pushed to the history stack.

Now, to perform the undo operation, the application takes the last executed command from the history and either performs an inverse action or restores the past state of the editor, saved by that command.

## [](https://refactoring.guru/design-patterns/command/java/example#example-0--commands)**commands**

#### [](https://refactoring.guru/design-patterns/command/java/example#example-0--commands-Command-java)**commands/Command.java:**  Abstract base command
```java
package refactoring_guru.command.example.commands;

import refactoring_guru.command.example.editor.Editor;

public abstract class Command {
    public Editor editor;
    private String backup;

    Command(Editor editor) {
        this.editor = editor;
    }

    void backup() {
        backup = editor.textField.getText();
    }

    public void undo() {
        editor.textField.setText(backup);
    }

    public abstract boolean execute();
}
```
#### [](https://refactoring.guru/design-patterns/command/java/example#example-0--commands-CopyCommand-java)**commands/CopyCommand.java:**  Copy selected text to clipboard
```java
package refactoring_guru.command.example.commands;

import refactoring_guru.command.example.editor.Editor;

public class CopyCommand extends Command {

    public CopyCommand(Editor editor) {
        super(editor);
    }

    @Override
    public boolean execute() {
        editor.clipboard = editor.textField.getSelectedText();
        return false;
    }
}
```
#### [](https://refactoring.guru/design-patterns/command/java/example#example-0--commands-PasteCommand-java)**commands/PasteCommand.java:**  Paste text from clipboard
```java
package refactoring_guru.command.example.commands;

import refactoring_guru.command.example.editor.Editor;

public class PasteCommand extends Command {

    public PasteCommand(Editor editor) {
        super(editor);
    }

    @Override
    public boolean execute() {
        if (editor.clipboard == null || editor.clipboard.isEmpty()) return false;

        backup();
        editor.textField.insert(editor.clipboard, editor.textField.getCaretPosition());
        return true;
    }
}
```
#### [](https://refactoring.guru/design-patterns/command/java/example#example-0--commands-CutCommand-java)**commands/CutCommand.java:**  Cut text to clipboard
```java
package refactoring_guru.command.example.commands;

import refactoring_guru.command.example.editor.Editor;

public class CutCommand extends Command {

    public CutCommand(Editor editor) {
        super(editor);
    }

    @Override
    public boolean execute() {
        if (editor.textField.getSelectedText().isEmpty()) return false;

        backup();
        String source = editor.textField.getText();
        editor.clipboard = editor.textField.getSelectedText();
        editor.textField.setText(cutString(source));
        return true;
    }

    private String cutString(String source) {
        String start = source.substring(0, editor.textField.getSelectionStart());
        String end = source.substring(editor.textField.getSelectionEnd());
        return start + end;
    }
}
```
#### [](https://refactoring.guru/design-patterns/command/java/example#example-0--commands-CommandHistory-java)**commands/CommandHistory.java:**  Command history
```java
package refactoring_guru.command.example.commands;

import java.util.Stack;

public class CommandHistory {
    private Stack<Command> history = new Stack<>();

    public void push(Command c) {
        history.push(c);
    }

    public Command pop() {
        return history.pop();
    }

    public boolean isEmpty() { return history.isEmpty(); }
}
```
## [](https://refactoring.guru/design-patterns/command/java/example#example-0--editor)**editor**

#### [](https://refactoring.guru/design-patterns/command/java/example#example-0--editor-Editor-java)**editor/Editor.java:**  GUI of text editor
```java
package refactoring_guru.command.example.editor;

import refactoring_guru.command.example.commands.*;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Editor {
    public JTextArea textField;
    public String clipboard;
    private CommandHistory history = new CommandHistory();

    public void init() {
        JFrame frame = new JFrame("Text editor (type & use buttons, Luke!)");
        JPanel content = new JPanel();
        frame.setContentPane(content);
        frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        content.setLayout(new BoxLayout(content, BoxLayout.Y_AXIS));
        textField = new JTextArea();
        textField.setLineWrap(true);
        content.add(textField);
        JPanel buttons = new JPanel(new FlowLayout(FlowLayout.CENTER));
        JButton ctrlC = new JButton("Ctrl+C");
        JButton ctrlX = new JButton("Ctrl+X");
        JButton ctrlV = new JButton("Ctrl+V");
        JButton ctrlZ = new JButton("Ctrl+Z");
        Editor editor = this;
        ctrlC.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                executeCommand(new CopyCommand(editor));
            }
        });
        ctrlX.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                executeCommand(new CutCommand(editor));
            }
        });
        ctrlV.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                executeCommand(new PasteCommand(editor));
            }
        });
        ctrlZ.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                undo();
            }
        });
        buttons.add(ctrlC);
        buttons.add(ctrlX);
        buttons.add(ctrlV);
        buttons.add(ctrlZ);
        content.add(buttons);
        frame.setSize(450, 200);
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
    }

    private void executeCommand(Command command) {
        if (command.execute()) {
            history.push(command);
        }
    }

    private void undo() {
        if (history.isEmpty()) return;

        Command command = history.pop();
        if (command != null) {
            command.undo();
        }
    }
}
```
#### [](https://refactoring.guru/design-patterns/command/java/example#example-0--Demo-java)**Demo.java:**  Client code
```java
package refactoring_guru.command.example;

import refactoring_guru.command.example.editor.Editor;

public class Demo {
    public static void main(String[] args) {
        Editor editor = new Editor();
        editor.init();
    }
}
```
#### [](https://refactoring.guru/design-patterns/command/java/example#example-0--OutputDemo-png)**OutputDemo.png:**  Execution result

![](https://refactoring.guru/images/patterns/examples/java/command/OutputDemo.png)