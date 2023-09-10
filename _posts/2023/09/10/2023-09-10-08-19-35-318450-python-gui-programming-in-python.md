---
layout: post
title: "[Python] GUI programming in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

Graphical User Interface (GUI) programming allows developers to create interactive and user-friendly applications. In Python, there are several libraries available that make GUI programming a breeze. In this blog post, we will explore some of the popular libraries and demonstrate how to create GUI applications in Python.

## Tkinter

**Tkinter** is the standard GUI toolkit for Python. It provides a set of modules that allows developers to create desktop applications with a rich set of GUI components. Tkinter is included with standard Python distributions, so there's no need to install any extra packages.

To get started with Tkinter, first, import the `tkinter` module:

```python
import tkinter as tk
```

Next, create an instance of the main `Tk` class, which represents the main window of the application:

```python
root = tk.Tk()
```

After creating the main window, you can add various widgets like buttons, labels, text boxes, etc., to the window using different layout managers. For example, to add a button widget:

```python
button = tk.Button(root, text="Click Me!")
button.pack()
```

Finally, start the GUI event loop, which listens for user interactions:

```python
root.mainloop()
```

### Example: Hello World!

Here's a simple example that demonstrates a Hello World GUI application using Tkinter:

```python
import tkinter as tk

def say_hello():
    print("Hello, GUI!")

root = tk.Tk()

button = tk.Button(root, text="Click Me!", command=say_hello)
button.pack()

root.mainloop()
```

When you run this program, it will display a window with a button. When you click the button, it will print "Hello, GUI!" in the console.

## PyQt

**PyQt** is a set of Python bindings for the popular Qt application framework. It provides a rich set of widgets, events, and other features for building cross-platform GUI applications. PyQt is not included with Python by default, so you will need to install it separately using `pip`:

```bash
pip install pyqt5
```

Here's an example of a simple Hello World application using PyQt:

```python
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow

def say_hello():
    print("Hello, GUI!")

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Hello World!")

label = QLabel("Hello, PyQt!", parent=window)
label.setGeometry(100, 100, 200, 50)

window.show()

sys.exit(app.exec_())
```

In this example, we create a `QMainWindow` instance, set its title, and add a `QLabel` widget that displays "Hello, PyQt!". When the application is run, it will show the window with the label.

## Conclusion

Python provides several options for GUI programming, but Tkinter and PyQt are two popular choices. Tkinter is lightweight and included with Python, making it great for simple applications. On the other hand, PyQt offers a more robust toolkit with advanced features for building complex and cross-platform applications.

Whether you choose Tkinter or PyQt, GUI programming in Python can be a rewarding experience, allowing you to create beautiful and intuitive interfaces for your applications. So go ahead, dive in, and start building your own GUI applications with Python!