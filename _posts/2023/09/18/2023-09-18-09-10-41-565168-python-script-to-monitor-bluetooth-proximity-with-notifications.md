---
layout: post
title: "Python script to monitor Bluetooth proximity with notifications"
description: " "
date: 2023-09-18
tags: [Bluetooth]
comments: true
share: true
---

Are you tired of constantly checking if your Bluetooth device is within range? With the help of Python, you can create a script that automatically monitors the proximity of your Bluetooth device and sends notifications when it goes out of range. In this blog post, we will walk through the steps to accomplish this task.

## Prerequisites
To follow along with this tutorial, make sure you have the following:

- Python installed on your system
- The `pybluez` library installed (you can install it using `pip install pybluez`)
- A Bluetooth device that you want to monitor

## Steps

### Step 1: Import the necessary libraries
First, we need to import the required libraries to work with Bluetooth and send notifications. Add the following code to your Python script:

```python
import bluetooth
from plyer import notification
```

### Step 2: Define the Bluetooth device details
Next, we need to define the details of the Bluetooth device we want to monitor. Replace `DEVICE_NAME` with the name of your device and `DEVICE_ADDRESS` with its MAC address:

```python
DEVICE_NAME = "Your Device Name"
DEVICE_ADDRESS = "XX:XX:XX:XX:XX:XX"
```

### Step 3: Monitor Bluetooth proximity
Now we can write the main logic to monitor the Bluetooth proximity. We will continuously check the device's availability and send a notification when it goes out of range:

```python
def monitor_proximity():
    while True:
        try:
            result = bluetooth.lookup_name(DEVICE_ADDRESS, timeout=5)
            if result is None:
                notification.notify(
                    title="Bluetooth Proximity",
                    message=f"{DEVICE_NAME} is out of range",
                    timeout=10
                )
            else:
                print(f"{DEVICE_NAME} is in range")
        except bluetooth.btcommon.BluetoothError as e:
            print(f"Error: {e}")
```

### Step 4: Run the script
To start monitoring the Bluetooth proximity, add the following code at the end of your script:

```python
if __name__ == "__main__":
    monitor_proximity()
```

### Step 5: Customize notifications (optional)
You can customize the appearance and behavior of the notifications by modifying the `notify()` function arguments in the `monitor_proximity()` function.

## Conclusion
With just a few lines of Python code, you can create a script to monitor the Bluetooth proximity of your device and receive notifications when it goes out of range. This can be helpful in various scenarios, such as keeping track of your valuable belongings or ensuring your Bluetooth headset is always within reach. Experiment with the code and customize it further to suit your needs.

Remember, you can run this script in the background or as a scheduled task to continuously monitor Bluetooth proximity and never miss important notifications.

#Python #Bluetooth #Proximity