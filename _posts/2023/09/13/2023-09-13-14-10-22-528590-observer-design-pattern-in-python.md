---
layout: post
title: "Observer design pattern in Python"
description: " "
date: 2023-09-13
tags: []
comments: true
share: true
---

The Observer design pattern is a behavioral design pattern that allows objects (observers) to subscribe and receive updates from a subject (observable) whenever there is a change in its state. This pattern promotes loose coupling between objects and enhances modularity and extensibility in the system.

## Implementation in Python

To demonstrate the implementation of the Observer design pattern in Python, let's consider a scenario where we have a weather station that broadcasts weather updates to multiple display devices. We'll have a `WeatherStation` class as the subject and `DisplayDevice` classes as observers. Whenever the weather changes, the weather station will notify all the display devices.

```python
class WeatherStation:
    def __init__(self):
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0
        self.observers = []

    def register_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)

    def set_measurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.notify_observers()


class DisplayDevice:
    def __init__(self, name):
        self.name = name

    def update(self, temperature, humidity, pressure):
        print(f'{self.name} received update:')
        print(f'Temperature: {temperature}°C')
        print(f'Humidity: {humidity}%')
        print(f'Pressure: {pressure}hPa')
        print()


# Usage example
weather_station = WeatherStation()

display_device1 = DisplayDevice("Device 1")
weather_station.register_observer(display_device1)

display_device2 = DisplayDevice("Device 2")
weather_station.register_observer(display_device2)

# Simulating weather updates
weather_station.set_measurements(25, 70, 1013)
weather_station.set_measurements(20, 60, 1015)

weather_station.remove_observer(display_device2)

weather_station.set_measurements(30, 75, 1010)
```

In the above example, we have defined a `WeatherStation` class which acts as the subject. It maintains the state of temperature, humidity, and pressure and provides methods to register, remove, and notify observers. 

The `DisplayDevice` class represents the observers. Each `DisplayDevice` instance has an `update` method that is called by the weather station when there is a change in the weather conditions.

To use the observer pattern, we create a `WeatherStation` instance and register the `DisplayDevice` instances as observers. Whenever the weather conditions change, the weather station notifies all the registered observers by calling their `update` method.

## Conclusion

The Observer design pattern is a powerful tool for building systems where there is a need to decouple the subject and observers. It provides flexibility and extensibility by allowing multiple observers to receive updates from a subject. By implementing the Observer design pattern in Python, we can easily manage and notify observers when there is a change in the state of a subject.