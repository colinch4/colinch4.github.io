---
layout: post
title: "Working with CSV data in WXPython"
description: " "
date: 2023-10-01
tags: []
comments: true
share: true
---

## Introduction
When building GUI applications with WXPython, it's quite common to need to work with CSV (Comma-Separated Values) files for importing or exporting data. In this blog post, we will explore how to read and write CSV files using WXPython, allowing us to easily manipulate and interact with data.

## Reading CSV Files
To read a CSV file in WXPython, we can use the `wx.grid.Grid` widget in combination with the `csv` module. Let's see an example:

```python
import csv
import wx 
import wx.grid

class MyGridFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title="CSV Viewer", size=(600, 400))
        
        # Create a grid widget
        self.grid = wx.grid.Grid(self)
        
        # Load the CSV data into the grid
        with open('data.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row_index, row in enumerate(reader):
                for col_index, value in enumerate(row):
                    self.grid.SetCellValue(row_index, col_index, value)
        
        # Auto-size columns
        self.grid.AutoSizeColumns()

# Create the application
app = wx.App()

# Create the main window
frame = MyGridFrame(None)

# Show the main window
frame.Show()

# Run the application
app.MainLoop()
```

In this example, we create a `MyGridFrame` class which inherits from `wx.Frame`. Inside the `__init__` method, we create a `wx.grid.Grid` widget and load CSV data into it. We use the `csv.reader` module to read the CSV file and iterate over the rows and columns, setting cell values in the grid.

## Writing CSV Files
To write data to a CSV file in WXPython, we can use the `csv` module together with user inputs from the GUI. Let's see an example:

```python
import csv
import wx

class CSVWriterFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title="CSV Writer", size=(300, 200))
        
        # Create a panel for layout
        panel = wx.Panel(self)
        
        # Create text controls for data input
        self.name_text = wx.TextCtrl(panel)
        self.age_text = wx.TextCtrl(panel)
        
        # Create a button for saving data
        save_button = wx.Button(panel, label="Save")
        save_button.Bind(wx.EVT_BUTTON, self.on_save)
        
        # Add controls to the panel
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(wx.StaticText(panel, label="Name"), 0, wx.ALL, 5)
        sizer.Add(self.name_text, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(wx.StaticText(panel, label="Age"), 0, wx.ALL, 5)
        sizer.Add(self.age_text, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(save_button, 0, wx.ALL | wx.ALIGN_CENTER, 5)
        
        panel.SetSizerAndFit(sizer)
        
    def on_save(self, event):
        # Get the input data
        name = self.name_text.GetValue()
        age = self.age_text.GetValue()
        
        # Open the CSV file in append mode
        with open('data.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([name, age])
        
        # Clear the input fields
        self.name_text.SetValue('')
        self.age_text.SetValue('')

# Create the application
app = wx.App()

# Create the main window
frame = CSVWriterFrame(None)

# Show the main window
frame.Show()

# Run the application
app.MainLoop()
```

In this example, we create a `CSVWriterFrame` class which inherits from `wx.Frame`. Inside the `__init__` method, we create text controls for user input and a button for saving data to the CSV file. The `on_save` method is called when the button is clicked, it gets the input data and uses the `csv.writer` module to write a new row to the CSV file.

## Conclusion
Working with CSV data in WXPython is straightforward, thanks to the built-in `csv` module. By combining it with WXPython's UI components, we can easily read and write CSV files, providing a more interactive experience for users.