---
layout: post
title: "Real-time vehicle tracking using GPS data in Python"
description: " "
date: 2023-09-22
tags: []
comments: true
share: true
---

With the advancement in global positioning system (GPS) technology, real-time vehicle tracking has become easier and more accessible than ever before. By leveraging GPS data and Python programming, we can develop a robust solution for tracking vehicles in real-time. In this blog post, we will explore how to implement real-time vehicle tracking using GPS data in Python.

## Installing Required Packages

To get started, we need to install the necessary packages in Python. The two essential packages for this project are:

1. **`gpsd-py3`**: A Python library that provides access to GPS data through the gpsd service.
2. **`geopy`**: A Python library for geocoding and calculating distance between locations.

To install these packages, simply run the following command:

```python
pip install gpsd-py3 geopy
```

## Setting Up GPSD Service

GPSD is a service daemon that provides access to GPS receivers. We need to set up the GPSD service on our system to retrieve GPS data. Follow the below steps to install and configure GPSD:

1. Install GPSD by running the following command:

```shell
sudo apt-get install gpsd gpsd-clients
```

2. Next, edit the GPSD configuration file by running:

```shell
sudo nano /etc/default/gpsd
```

3. Uncomment the line that begins with `DEVICES=` and set it to the port where your GPS receiver is connected. It should look something like this:

```shell
DEVICES="/dev/ttyUSB0"
```

4. Save the file and exit nano.

5. Restart the GPSD service by running:

```shell
sudo systemctl restart gpsd
```

## Retrieving GPS Data in Python

Now that we have the GPSD service set up, we can start retrieving GPS data using the `gpsd-py3` Python library. Here's an example code snippet to get real-time GPS data in Python:

```python
import gpsd

# Connect to the local GPSD service
gpsd.connect()

# Main loop to continuously retrieve GPS data
while True:
    packet = gpsd.get_current()
    if packet.mode >= 2:
        latitude = packet.position()[0]
        longitude = packet.position()[1]
        speed = packet.speed()
        heading = packet.track()
        # Process the GPS data as required
```

In the above code, we import the `gpsd` module and establish a connection to the local GPSD service using the `connect()` function. We then enter a loop to continuously retrieve the GPS data using the `get_current()` function.

We check if the GPS fix mode is at least 2, indicating a valid GPS fix. If the fix mode is sufficient, we extract the latitude, longitude, speed, and heading from the GPS data packet. These values can be further processed or displayed as needed.

## Displaying the Real-Time Location on a Map

To visualize the real-time location of the tracked vehicle on a map, we can use the `geopy` package. Here's an example code snippet to display the location on a map:

```python
from geopy.geocoders import Nominatim
import folium

# Initialize geocoder
geolocator = Nominatim(user_agent="vehicle_tracking")

# Get the current location
location = geolocator.reverse((latitude, longitude))

# Create Map object centered at the current location
map = folium.Map(location=[latitude, longitude], zoom_start=15)

# Add a marker at the current location
folium.Marker([latitude, longitude], popup=location.address).add_to(map)

# Save the map as an HTML file
map.save("realtime_tracking.html")
```

In the above code, we use the `Nominatim` geocoder from the `geopy` package to convert the latitude and longitude into an address. We then create a `folium` map object centered at the current location and add a marker with the address as a popup. Finally, we save the map as an HTML file for easy viewing.

## Conclusion

In this blog post, we have explored how to implement real-time vehicle tracking using GPS data in Python. By leveraging the `gpsd-py3` library and the `geopy` package, we can easily retrieve real-time GPS data and display the tracked vehicle's location on a map. This opens up possibilities for various applications, such as fleet management and logistics tracking.