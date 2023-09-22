---
layout: post
title: "Calculating cumulative distance traveled from GPS data in Python"
description: " "
date: 2023-09-22
tags: [python, distance]
comments: true
share: true
---

In this blog post, we will explore how to calculate the cumulative distance traveled using GPS data in Python. This can be useful for analyzing various scenarios such as tracking the distance traveled in a workout, measuring the distance traveled by a vehicle, or even assessing the total distance covered during a hiking trip.

## Gathering GPS Data

To begin, we need to have GPS data to work with. GPS data typically consists of latitude, longitude, and a timestamp for each location point. For the purpose of this example, let's assume we have a CSV file ('gps_data.csv') containing the following fields: 'latitude', 'longitude', and 'timestamp'.

## Calculating Distance

To calculate distance between two GPS points, we can make use of the Haversine formula. The Haversine formula calculates the great-circle distance between two points on a sphere given their longitudes and latitudes.

```python
import math

def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371  # Radius of the Earth in kilometers
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad

    a = math.sin(dlat/2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

    distance = R * c
    return distance
```

The `calculate_distance` function takes in the latitude and longitude values of two points and returns the distance between them in kilometers. 

## Calculating Cumulative Distance Traveled

Next, we'll read the GPS data from the CSV file and calculate the cumulative distance traveled. We'll assume that the GPS data is sorted by timestamp in ascending order.

```python
import csv

cumulative_distance = 0

with open('gps_data.csv', 'r') as file:
    reader = csv.reader(file)
    prev_lat, prev_lon = None, None

    for row in reader:
        lat, lon, _ = map(float, row)
        if prev_lat is not None and prev_lon is not None:
            distance = calculate_distance(prev_lat, prev_lon, lat, lon)
            cumulative_distance += distance

        prev_lat, prev_lon = lat, lon

print(f"Cumulative distance traveled: {cumulative_distance:.2f} km")
```

In the above code, we initialize the `cumulative_distance` variable to 0. Then, we iterate through each GPS point, calculate the distance between the current and previous points, and add it to the cumulative distance. Finally, we print out the total cumulative distance traveled.

## Conclusion

Tracking and calculating cumulative distance from GPS data can be done easily in Python using techniques like the Haversine formula. This information can be helpful for a variety of purposes, including fitness tracking, vehicle monitoring, or analyzing travel data. By understanding the concepts covered in this blog post, you can leverage GPS data to gain valuable insights. Happy coding!

#python #GPS #distance #tracking