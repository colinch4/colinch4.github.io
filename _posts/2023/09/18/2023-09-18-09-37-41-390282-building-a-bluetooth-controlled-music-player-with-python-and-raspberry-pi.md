---
layout: post
title: "Building a Bluetooth-controlled music player with Python and Raspberry Pi"
description: " "
date: 2023-09-18
tags: [raspberrypi]
comments: true
share: true
---

In this tutorial, we will explore how to build a Bluetooth-controlled music player using Python and Raspberry Pi. With this project, you will be able to control your music player wirelessly from your smartphone, tablet, or any Bluetooth-enabled device.

## Prerequisites

Before we start, make sure you have the following:

- A Raspberry Pi running a compatible operating system (such as Raspbian).
- A Bluetooth dongle (if your Raspberry Pi doesn't have built-in Bluetooth).
- A speaker or headphones connected to the Raspberry Pi.

## Step 1: Installing Dependencies

First, we need to install the necessary dependencies. Open a terminal on your Raspberry Pi and run the following commands:

```bash
sudo apt-get update
sudo apt-get install python-bluez python-gobject
```

These commands will update the package lists and install `python-bluez` and `python-gobject`, which are required for Bluetooth communication.

## Step 2: Pairing with Your Bluetooth Device

Next, we need to pair our Raspberry Pi with the Bluetooth device (e.g., your smartphone) you want to use to control the music player.

1. Enable Bluetooth on your Raspberry Pi by running `sudo bluetoothctl` in the terminal.
2. Turn on your Bluetooth device and put it into pairing mode.
3. In the `bluetoothctl` prompt, type `power on` to ensure Bluetooth is enabled.
4. Type `pairable on` to make your Raspberry Pi discoverable.
5. Type `scan on` to scan for nearby Bluetooth devices.
6. When your device appears in the list, note down its MAC address (e.g., `00:11:22:33:AA:BB`).
7. Type `pair [MAC_ADDRESS]` (replace `[MAC_ADDRESS]` with the actual MAC address) to initiate the pairing process.
8. Follow the on-screen instructions to complete the pairing process.

## Step 3: Building the Music Player

Now, let's write some Python code to control the music player. Create a new Python script called `music_player.py` and open it in your favorite text editor.

```python
import dbus
import dbus.mainloop.glib
from gi.repository import GLib

def on_property_changed(interface, changed, invalidated):
    if interface != 'org.bluez.MediaPlayer1':
        return

    if 'Status' in changed:
        status = changed['Status']
        if status == 'playing':
            print("Music playing...")
        elif status == 'paused':
            print("Music paused.")
        elif status == 'stopped':
            print("Music stopped.")

def main():
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    bus = dbus.SystemBus()

    manager = dbus.Interface(bus.get_object('org.bluez', '/'), 'org.freedesktop.DBus.ObjectManager')
    for path, _ in manager.GetManagedObjects().items():
        if 'org.bluez.MediaPlayer1' in _.keys():
            player = dbus.Interface(bus.get_object('org.bluez', path), 'org.bluez.MediaPlayer1')
            player.onPropertiesChanged = on_property_changed

    mainloop = GLib.MainLoop()
    mainloop.run()

if __name__ == '__main__':
    main()

```

This code initializes the D-Bus system, gets the list of managed objects, and checks if any of them are Bluetooth media players. It then registers a callback function `on_property_changed` to handle the changes in the player's status.

## Step 4: Running the Music Player

Save the script and run it using the following command:

```bash
python music_player.py
```

You should now see the status of your music player whenever it changes. Feel free to modify the `on_property_changed` function to perform custom actions based on the player's status.

## Conclusion

In this tutorial, we learned how to build a Bluetooth-controlled music player using Python and Raspberry Pi. Now you can control your music wirelessly and enjoy the convenience of remote playback control.

#python #raspberrypi