---
layout: post
title: "Creating a calculator in WXPython"
description: " "
date: 2023-10-01
tags: [wxpython]
comments: true
share: true
---

Calculator applications are a common project for beginners learning GUI programming. In this blog post, we will walk through the process of creating a simple calculator using the WXPython library.

## Installing WXPython

Before we get started, we need to make sure that WXPython is installed on our system. To install it, you can use pip:

```python
pip install wxpython
```

## Setting up the Calculator Window

The first step is to import the necessary modules and create a new application object and main window:

```python
import wx

class Calculator(wx.Frame):
    def __init__(self, parent, title):
        super(Calculator, self).__init__(parent, title=title, size=(300, 400))
        
        self.InitUI()
        
    def InitUI(self):
        panel = wx.Panel(self)
        
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        # Place widgets here
        
        panel.SetSizer(vbox)

        self.Centre()
        self.Show(True)

if __name__ == '__main__':
    app = wx.App()
    Calculator(None, title='Calculator')
    app.MainLoop()
```

In the above code, we define a `Calculator` class which extends `wx.Frame` and represents the main window of our calculator application. The `InitUI` method initializes the UI components. We create a panel for holding the widgets and a vertical box sizer, `vbox`, for organizing them.

## Adding Buttons and Text Control

Next, let's add the buttons and text control to our calculator window:

```python
def InitUI(self):
    panel = wx.Panel(self)
    vbox = wx.BoxSizer(wx.VERTICAL)

    self.text_ctrl = wx.TextCtrl(panel, style=wx.TE_RIGHT)
    vbox.Add(self.text_ctrl, proportion=1, flag=wx.EXPAND | wx.TOP | wx.BOTTOM, border=4)
    
    gs = wx.GridSizer(4, 4, 5, 5)
    
    gs.AddMany([
        (wx.Button(panel, label='7'), 0, wx.EXPAND),
        (wx.Button(panel, label='8'), 0, wx.EXPAND),
        (wx.Button(panel, label='9'), 0, wx.EXPAND),
        (wx.Button(panel, label='/'), 0, wx.EXPAND),
        (wx.Button(panel, label='4'), 0, wx.EXPAND),
        (wx.Button(panel, label='5'), 0, wx.EXPAND),
        (wx.Button(panel, label='6'), 0, wx.EXPAND),
        (wx.Button(panel, label='*'), 0, wx.EXPAND),
        (wx.Button(panel, label='1'), 0, wx.EXPAND),
        (wx.Button(panel, label='2'), 0, wx.EXPAND),
        (wx.Button(panel, label='3'), 0, wx.EXPAND),
        (wx.Button(panel, label='-'), 0, wx.EXPAND),
        (wx.Button(panel, label='.'), 0, wx.EXPAND),
        (wx.Button(panel, label='0'), 0, wx.EXPAND),
        (wx.Button(panel, label='='), 0, wx.EXPAND),
        (wx.Button(panel, label='+'), 0, wx.EXPAND),
    ])
    
    vbox.Add(gs, proportion=2, flag=wx.EXPAND)
    panel.SetSizer(vbox)
```

In the `InitUI` method, we create a text control widget to display the calculator input and result. We add it to the vertical box sizer with `proportion=1` to make sure it expands vertically while taking up minimum horizontal space.

Next, we create a grid sizer, `gs`, for organizing the calculator buttons. We use the `wx.GridSizer` class with 4 rows, 4 columns, and a 5-pixel gap between each cell.

We use the `AddMany` method to add buttons to the grid sizer. The button labels are set accordingly and will trigger respective actions when clicked.

Finally, we add the grid sizer to the vertical box sizer with `proportion=2` to make it expand and take up more vertical space.

## Handling Button Clicks and Evaluating Expressions

Now, let's implement the button event handlers and write the logic for evaluating expressions:

```python
def InitUI(self):
    # ...

    for btn in panel.GetChildren():
        if isinstance(btn, wx.Button):
            btn.Bind(wx.EVT_BUTTON, self.OnButtonClick)
            
def OnButtonClick(self, event):
    label = event.GetEventObject().GetLabel()
    
    if label == '=':
        try:
            result = eval(self.text_ctrl.GetValue())
            self.text_ctrl.SetValue(str(result))
        except:
            wx.MessageBox('Invalid expression!', 'Error', wx.OK | wx.ICON_ERROR)
    else:
        self.text_ctrl.AppendText(label)
```

In the `InitUI` method, we iterate through all child widgets of the panel and bind the `wx.EVT_BUTTON` event to the `OnButtonClick` method for button widgets.

In the `OnButtonClick` method, we handle the button click event. We get the label of the clicked button and perform the respective action. If the label is `'='`, we evaluate the expression using `eval` and display the result in the text control. If an exception occurs during the evaluation, we show an error message box. Otherwise, for any other button, we append the label to the text control.

## Running the Calculator


To run the calculator application, execute the script:

```python
if __name__ == '__main__':
    app = wx.App()
    Calculator(None, title='Calculator')
    app.MainLoop()
```

When you run the script, the calculator window should appear with buttons for digits, operators, and an input/output text control. You can use the buttons to perform calculations and see the result in the text control.

With this basic example, you can further enhance the calculator by adding more functionality such as handling decimal numbers, parentheses, and additional mathematical operations.

#python #wxpython