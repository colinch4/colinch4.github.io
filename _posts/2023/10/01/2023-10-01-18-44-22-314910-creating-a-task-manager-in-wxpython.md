---
layout: post
title: "Creating a task manager in WXPython"
description: " "
date: 2023-10-01
tags: [WXPython, TaskManager]
comments: true
share: true
---

In this tutorial, we will learn how to create a simple task manager using the WXPython library. Task managers are essential tools for organizing and tracking tasks, making them a great project for practicing GUI programming with WXPython.

## Getting Started

First, we need to install WXPython. You can do this by running the following command:

```shell
pip install wxPython
```

## GUI Layout

Our task manager will have a simple GUI layout consisting of a list of tasks and buttons to add, edit, and delete tasks. Let's start by creating the main window and adding the necessary components.

```python
import wx

class TaskManager(wx.Frame):
    def __init__(self, parent, title):
        super(TaskManager, self).__init__(parent, title=title, size=(400, 300))
        
        self.tasks = []
        self.init_ui()
    
    def init_ui(self):
        panel = wx.Panel(self)

        self.task_list = wx.ListBox(panel, size=(300, 200), choices=self.tasks)
        add_btn = wx.Button(panel, label="Add Task")
        edit_btn = wx.Button(panel, label="Edit Task")
        delete_btn = wx.Button(panel, label="Delete Task")
        
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.task_list, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.Add(add_btn, flag=wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, border=5)
        vbox.Add(edit_btn, flag=wx.ALIGN_CENTER | wx.BOTTOM, border=5)
        vbox.Add(delete_btn, flag=wx.ALIGN_CENTER)
        
        panel.SetSizer(vbox)
        
        self.Centre()
        self.Show()

if __name__ == '__main__':
    app = wx.App()
    TaskManager(None, title='Task Manager')
    app.MainLoop()
```

In the above code, we create a `TaskManager` class inheriting from `wx.Frame`. We initialize the main window with a specific size and an empty list of tasks. Inside the `init_ui` method, we create a `wx.Panel` and add a `wx.ListBox` to display the tasks. We also add three buttons: "Add Task", "Edit Task", and "Delete Task". These buttons will be used to perform corresponding actions on the task list.

## Adding Functionality

Now that we have the basic GUI layout set up, let's add functionality to the buttons.

```python
# ...

class TaskManager(wx.Frame):
    # ...

    def init_ui(self):
        # ...

        add_btn.Bind(wx.EVT_BUTTON, self.on_add_task)
        edit_btn.Bind(wx.EVT_BUTTON, self.on_edit_task)
        delete_btn.Bind(wx.EVT_BUTTON, self.on_delete_task)
        
        # ...
    
    def on_add_task(self, event):
        dlg = wx.TextEntryDialog(self, "Enter new task:", "Add Task")
        if dlg.ShowModal() == wx.ID_OK:
            task = dlg.GetValue()
            self.tasks.append(task)
            self.task_list.Append(task)
        dlg.Destroy()
    
    def on_edit_task(self, event):
        selected_task = self.task_list.GetSelection()
        if selected_task != wx.NOT_FOUND:
            dlg = wx.TextEntryDialog(self, "Enter updated task:", "Edit Task")
            dlg.SetValue(self.tasks[selected_task])
            if dlg.ShowModal() == wx.ID_OK:
                updated_task = dlg.GetValue()
                self.tasks[selected_task] = updated_task
                self.task_list.SetString(selected_task, updated_task)
            dlg.Destroy()
    
    def on_delete_task(self, event):
        selected_task = self.task_list.GetSelection()
        if selected_task != wx.NOT_FOUND:
            del self.tasks[selected_task]
            self.task_list.Delete(selected_task)

# ...
```

In the code above, we bind each button to their respective event handlers (`on_add_task`, `on_edit_task`, `on_delete_task`). When the "Add Task" button is clicked, a text entry dialog is shown, allowing the user to enter a new task. If the user clicks "OK", the task is added to the list and displayed in the `wx.ListBox`.

Similarly, when the "Edit Task" button is clicked, a text entry dialog is shown with the selected task already filled in. If the user modifies the task and clicks "OK", the task is updated in the list and the `wx.ListBox` is updated with the new task.

Finally, when the "Delete Task" button is clicked, the selected task is deleted from the list and removed from the `wx.ListBox`.

## Conclusion

In this tutorial, we learned how to create a simple task manager using the WXPython library. We created a basic GUI layout with a list of tasks and buttons to add, edit, and delete tasks. We also added functionality to these buttons by handling their respective events. With this foundation, you can expand the task manager by adding additional features and improving the user interface.

#WXPython #TaskManager