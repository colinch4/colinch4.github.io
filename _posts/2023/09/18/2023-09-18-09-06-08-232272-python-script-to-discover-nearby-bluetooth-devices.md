---
layout: post
title: "Python script to discover nearby Bluetooth devices"
description: " "
date: 2023-09-18
tags: [Python, Bluetooth]
comments: true
share: true
---
import bluetooth

# Discover nearby Bluetooth devices
# Make sure Bluetooth is enabled on your system

# Initialize the Bluetooth socket
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

# Set the Bluetooth device class to discover all devices
sock.setsockopt(bluetooth.SOL_HCI, bluetooth.HCI_FILTER, b"\xff\xff\xff\xff\xff\xff\xff\xff")

# Enable Bluetooth scanning mode
bluetooth.enable_discoverability()

# Start scanning for nearby devices
devices = bluetooth.discover_devices(duration=8, lookup_names=True, flush_cache=True)

# Print the discovered devices
if len(devices) > 0:
    print("Discovered devices:")
    for address, name in devices:
        print(f"Device Name: {name}")
        print(f"Device Address: {address}")
        print("---------------------------------")
else:
    print("No devices found nearby.")

# Close the Bluetooth socket
sock.close()
```

Hashtags: #Python #Bluetooth