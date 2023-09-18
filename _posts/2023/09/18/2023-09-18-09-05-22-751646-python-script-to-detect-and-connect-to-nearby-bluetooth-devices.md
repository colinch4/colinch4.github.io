---
layout: post
title: "Python script to detect and connect to nearby Bluetooth devices"
description: " "
date: 2023-09-18
tags: [Bluetooth, Python]
comments: true
share: true
---

Bluetooth is a wireless technology that allows for short-range communication between devices. With Python's `pybluez` library, we can easily detect and connect to nearby Bluetooth devices. In this blog post, we will walk through an example script that accomplishes this task.

## Prerequisites

Before we begin, make sure you have the following:

- A computer with Bluetooth capabilities
- Python 3.x installed
- `pybluez` library installed (you can install it using `pip install pybluez`)

## Script Overview

Our script will perform the following steps:

1. Import the necessary libraries.
2. Create a Bluetooth discovery agent.
3. Start scanning for nearby devices.
4. Print the discovered device's name and address.
5. Prompt the user to select a device to connect to.
6. Connect to the selected device.
7. Perform any desired actions with the connected device.
8. Close the Bluetooth connection.

## Example Code

Here's an example script that accomplishes the above steps:

```python
import bluetooth

def scan_bluetooth_devices():
    print("Scanning for nearby Bluetooth devices...")
    nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=True, flush_cache=True)

    print("Discovered devices:")
    for address, name in nearby_devices:
        print(f"{name} ({address})")

    return nearby_devices

def connect_to_device(device_address):
    print(f"Connecting to device {device_address}...")
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((device_address, 1))
    print("Connected!")

    # Perform actions with the connected device here

    sock.close()
    print("Connection closed.")

if __name__ == "__main__":
    devices = scan_bluetooth_devices()

    if devices:
        selection = input("Enter the number of the device to connect to (1, 2, etc.): ")
        selected_device = devices[int(selection) - 1]

        connect_to_device(selected_device[0])
    else:
        print("No Bluetooth devices found.")
```

## Running the Script

To run the script, follow these steps:

1. Save the script to a file with a `.py` extension (e.g., `bluetooth_connect.py`).
2. Open a terminal or command prompt and navigate to the directory where the script is located.
3. Run the script using the command `python bluetooth_connect.py`.
4. Follow the prompts to scan and connect to a nearby Bluetooth device.

## Conclusion

With the help of Python and the `pybluez` library, we can easily detect and connect to nearby Bluetooth devices. This capability opens up numerous possibilities for creating applications that interact with Bluetooth-enabled devices. Feel free to modify and expand upon the example script to fit your specific needs.

#Bluetooth #Python