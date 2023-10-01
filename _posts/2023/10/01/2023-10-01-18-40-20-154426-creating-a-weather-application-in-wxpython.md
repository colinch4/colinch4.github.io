---
layout: post
title: "Creating a weather application in WXPython"
description: " "
date: 2023-10-01
tags: [weatherapp, wxpython]
comments: true
share: true
---

In this tutorial, we will learn how to create a simple weather application using the Python programming language and the WXPython library. With WXPython, we can build cross-platform desktop applications with a native look and feel.

## Prerequisites

Before we proceed, make sure you have the following installed on your system:

- Python (version 3.6 or above)
- WXPython (install using `pip install wxpython`)

## Getting Started

Let's start by creating a new Python file named `weather_app.py` and import the necessary modules:

```python
import wx
import requests
```

Next, create a new class to represent our weather application:

```python
class WeatherApp(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Weather App")
        
        self.panel = wx.Panel(self)
        self.label = wx.StaticText(self.panel, label="Enter City Name:")
        self.text = wx.TextCtrl(self.panel)
        self.button = wx.Button(self.panel, label="Get Weather")
        
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.label, 0, wx.ALL, 5)
        self.sizer.Add(self.text, 0, wx.ALL, 5)
        self.sizer.Add(self.button, 0, wx.ALL, 5)
        
        self.panel.SetSizer(self.sizer)
        self.Bind(wx.EVT_BUTTON, self.on_button_click, self.button)
        
    def on_button_click(self, event):
        city_name = self.text.GetValue()
        weather_data = self.get_weather_data(city_name)
        wx.MessageBox(weather_data, "Weather", wx.OK)
        
    def get_weather_data(self, city_name):
        # Make an API request to get the weather data for the given city
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=YOUR_API_KEY")
        
        if response.status_code == 200:
            data = response.json()
            description = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            return f"Current weather in {city_name}: {description}, Temperature: {temperature} K"
        else:
            return "Failed to retrieve weather data."
```

In the above code, we defined a class `WeatherApp` that inherits from `wx.Frame`. In the constructor `__init__`, we create UI components like `StaticText`, `TextCtrl`, and `Button`, and add them to a `BoxSizer` for layout.

The `on_button_click` method is called when the button is clicked. It extracts the city name from the text input and calls the `get_weather_data` method to retrieve the weather information using the OpenWeatherMap API.

Finally, we create an instance of the `WeatherApp` class and start the main event loop:

```python
if __name__ == "__main__":
    app = wx.App()
    frame = WeatherApp()
    frame.Show()
    app.MainLoop()
```

## Running the Application

Save the file and run it using the Python interpreter:

```bash
python weather_app.py
```

You should see a window with a text input and a button. Enter a city name and click the "Get Weather" button. A message box will appear displaying the current weather information for the specified city.

That's it! You have successfully created a weather application using WXPython. Feel free to enhance it by adding more features like forecasting, graphical representation, or using different APIs.

#weatherapp #wxpython