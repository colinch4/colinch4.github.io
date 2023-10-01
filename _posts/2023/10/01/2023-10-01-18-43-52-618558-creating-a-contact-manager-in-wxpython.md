---
layout: post
title: "Creating a contact manager in WXPython"
description: " "
date: 2023-10-01
tags: [python, wxpython]
comments: true
share: true
---

In this tutorial, we will walk through the process of creating a contact manager using the WXPython library. WXPython is a Python wrapper for the popular cross-platform GUI toolkit, wxWidgets. By the end of this tutorial, you will have a basic contact manager application with functionality to add, delete, and view contacts.

## Prerequisites
Before we start, make sure you have the following installed on your machine:

- Python 3.x
- WXPython library

## Setting up the Project
1. Create a new Python file and import the necessary modules:

   ```python
   import wx
   import json
   ```

2. Create a class to represent the main frame of the application:

   ```python
   class ContactManagerFrame(wx.Frame):
       def __init__(self, parent):
           super().__init__(parent, title="Contact Manager", size=(400, 300))
           self.panel = wx.Panel(self)

           # Initialize the contact list
           self.contact_list = []

           # Create UI elements
           self.create_ui()

           # Load contacts from a file
           self.load_contacts()
   ```

## Building the User Interface
Now let's start building the user interface for our contact manager:

1. Create a method called `create_ui()` inside the `ContactManagerFrame` class:

   ```python
   def create_ui(self):
       # Create the contact list control
       self.contact_list_ctrl = wx.ListBox(self.panel)

       # Create buttons for add and delete actions
       self.button_add = wx.Button(self.panel, label="Add")
       self.button_delete = wx.Button(self.panel, label="Delete")

       # Bind events to button actions
       self.button_add.Bind(wx.EVT_BUTTON, self.on_add)
       self.button_delete.Bind(wx.EVT_BUTTON, self.on_delete)

       # Create the sizer to organize the UI elements
       sizer = wx.BoxSizer(wx.VERTICAL)
       sizer.Add(self.contact_list_ctrl, 1, wx.EXPAND|wx.ALL, 10)
       sizer.Add(self.button_add, 0, wx.ALL, 10)
       sizer.Add(self.button_delete, 0, wx.ALL, 10)

       # Set the main sizer for the panel
       self.panel.SetSizer(sizer)
   ```

2. Add the event handlers for the button actions:

   ```python
   def on_add(self, event):
       dialog = wx.TextEntryDialog(self.panel, "Enter contact name", "Add Contact")
       if dialog.ShowModal() == wx.ID_OK:
           contact_name = dialog.GetValue()
           self.contact_list.append(contact_name)
           self.refresh_contact_list()
       dialog.Destroy()

   def on_delete(self, event):
       selected_contact = self.contact_list_ctrl.GetSelection()
       if selected_contact != wx.NOT_FOUND:
           self.contact_list.pop(selected_contact)
           self.refresh_contact_list()
   ```

3. Implement methods to load and refresh the contact list:

   ```python
   def load_contacts(self):
       try:
           with open("contacts.json") as file:
               self.contact_list = json.load(file)
       except FileNotFoundError:
           pass
       self.refresh_contact_list()

   def refresh_contact_list(self):
       self.contact_list_ctrl.Clear()
       for contact in self.contact_list:
           self.contact_list_ctrl.Append(contact)
   ```

4. Finally, create an instance of the `ContactManagerFrame` class and run the application:

   ```python
   app = wx.App()
   frame = ContactManagerFrame(None)
   frame.Show()
   app.MainLoop()
   ```

## Conclusion
In this tutorial, you have learned how to create a basic contact manager using WXPython. We built the user interface with a contact list control and buttons for adding and deleting contacts. We also implemented functionality to load and save the contacts from a JSON file. Feel free to enhance the application by adding more features like editing contacts or searching for specific contacts.

#python #wxpython