---
layout: post
title: "Working with radio buttons in WXPython"
description: " "
date: 2023-10-01
tags: [WXPython, RadioButton]
comments: true
share: true
---

WXPython is a popular GUI toolkit for Python that allows you to create graphical user interfaces for desktop applications. One of the common UI elements used in many applications is radio buttons. In this tutorial, we will explore how to work with radio buttons using WXPython.

## Creating radio buttons

To create radio buttons in WXPython, you need to use the `wx.RadioButton` class. Here's an example of how to create two radio buttons:

```python
import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title)

        panel = wx.Panel(self)
        
        self.rb1 = wx.RadioButton(panel, label="Option 1", pos=(10, 10))
        self.rb2 = wx.RadioButton(panel, label="Option 2", pos=(10, 30))
        
        self.Bind(wx.EVT_RADIOBUTTON, self.on_radio_button)

        self.Center()
    
    def on_radio_button(self, event):
        rb = event.GetEventObject()
        print(f"Selected option: {rb.GetLabel()}")

app = wx.App()
frame = MyFrame(None, "Radio Button Example")
frame.Show()
app.MainLoop()
```

In this example, we create two radio buttons with labels "Option 1" and "Option 2" and position them within a `wx.Panel`. We also bind the `wx.EVT_RADIOBUTTON` event to the `on_radio_button` method, which will be called when a radio button is selected. The `event.GetEventObject()` method is used to get the selected radio button, and `event.GetLabel()` returns the label of the selected button.

## Working with radio button groups

In some cases, you may want to group radio buttons together so that only one option can be selected at a time. To achieve this, you need to use the `wx.RadioButton` constructor's `style` parameter and set it to `wx.RB_GROUP`. Here's an example:

```python
import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title)

        panel = wx.Panel(self)
        
        # Create radio buttons with RB_GROUP style
        self.rb1 = wx.RadioButton(panel, label="Option 1", pos=(10, 10), style=wx.RB_GROUP)
        self.rb2 = wx.RadioButton(panel, label="Option 2", pos=(10, 30))
        self.rb3 = wx.RadioButton(panel, label="Option 3", pos=(10, 50))
        
        self.Bind(wx.EVT_RADIOBUTTON, self.on_radio_button)

        self.Center()
    
    def on_radio_button(self, event):
        rb = event.GetEventObject()
        print(f"Selected option: {rb.GetLabel()}")

app = wx.App()
frame = MyFrame(None, "Radio Button Example")
frame.Show()
app.MainLoop()
```

In this example, we have three radio buttons, but the first one has the `wx.RB_GROUP` style. This ensures that only one option in the group can be selected at a time.

## Conclusion

In this tutorial, we have learned how to work with radio buttons in WXPython. We covered how to create radio buttons, bind events to handle button selection, and how to create radio button groups. Radio buttons are an essential UI element for users to make selections in applications, and WXPython provides an easy and flexible way to work with them.

#WXPython #RadioButton #GUIProgramming