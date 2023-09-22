---
layout: post
title: "Reverse geocoding multiple GPS coordinates in Python"
description: " "
date: 2023-09-22
tags: []
comments: true
share: true
---

Reverse geocoding is a process that takes GPS coordinates as input and returns the corresponding address or location information. In this tutorial, we will explore how to perform reverse geocoding on multiple GPS coordinates using Python.

## Prerequisites

To follow along with this tutorial, you will need the following:
- Python installed on your machine
- `geopy` library installed. You can install it using pip by running `pip install geopy`

## Step 1: Import Required Libraries

We will begin by importing the necessary libraries for reverse geocoding:

```python
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
```

## Step 2: Define Function for Reverse Geocoding

Next, we will define a function that takes the GPS coordinates and returns the corresponding address using the Nominatim geocoder. This function will handle cases when the geocoding service times out:

```python
def reverse_geocode(latitude, longitude):
    geolocator = Nominatim(user_agent='reverse_geocode')
    location = None
    try:
        location = geolocator.reverse(f"{latitude}, {longitude}", exactly_one=True)
    except GeocoderTimedOut:
        return reverse_geocode(latitude, longitude)
    return location
```

## Step 3: Prepare the GPS Coordinates

Now, let's define a list of GPS coordinates that we want to reverse geocode:

```python
coordinates = [
    (48.8566, 2.3522),
    (51.5074, -0.1278),
    (40.7128, -74.0060)
]
```

## Step 4: Reverse Geocode the Coordinates

Using a `for` loop, we will iterate over each GPS coordinate and apply the `reverse_geocode` function to get the address for that location:

```python
for coordinate in coordinates:
    latitude, longitude = coordinate
    location = reverse_geocode(latitude, longitude)
    address = location.address
    print(f"GPS coordinates: {latitude}, {longitude}")
    print(f"Address: {address}")
    print("---------")
```

## Step 5: Run the Program

Save the file with a `.py` extension and run it using the Python interpreter. You should see the address corresponding to each GPS coordinate printed on the console:

```
GPS coordinates: 48.8566, 2.3522
Address: Rue de Rivoli, Châtelet - Les Halles, Le Louvre, Paris, Île-de-France, France métropolitaine, 75001, France
---------
GPS coordinates: 51.5074, -0.1278
Address: Trafalgar Square, St. James's, City of Westminster, London, Greater London, England, SW1A 2JL, United Kingdom
---------
GPS coordinates: 40.7128, -74.0060
Address: Broadway, Lower Manhattan, Manhattan, New York County, New York, 10007, United States
---------
```

## Conclusion

In this tutorial, we learned how to perform reverse geocoding on multiple GPS coordinates using Python. By leveraging the `geopy` library and the Nominatim geocoding service, we can easily obtain the address or location information for a given set of coordinates. This can be useful in various applications like mapping, location-based services, and data analysis.