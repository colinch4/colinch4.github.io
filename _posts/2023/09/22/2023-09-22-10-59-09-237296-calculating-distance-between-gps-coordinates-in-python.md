---
layout: post
title: "Calculating distance between GPS coordinates in Python"
description: " "
date: 2023-09-22
tags: [geolocation]
comments: true
share: true
---

To get started, make sure you have `geopy` installed. You can do this by running the following command in your terminal or command prompt:

```python
pip install geopy
```

Once `geopy` is installed, you can begin by importing the necessary modules:

```python
from geopy.distance import geodesic
from geopy.point import Point
```

Next, define the coordinates for both locations:

```python
# Coordinates for location 1
lat1 = 51.5074
lon1 = -0.1278

# Coordinates for location 2
lat2 = 40.7128
lon2 = -74.0060
```

Now, create `Point` objects for each location using the latitude and longitude coordinates:

```python
point1 = Point(lat1, lon1)
point2 = Point(lat2, lon2)
```

Now that you have the `Point` objects, you can use the `geodesic` function from the `geopy.distance` module to calculate the distance between the two locations:

```python
distance = geodesic(point1, point2).miles
```

In this example, we used the `miles` attribute to get the distance in miles. However, you can also use other units such as `kilometers` or `nautical miles` depending on your preference.

Finally, print the calculated distance:

```python
print(f"The distance between the two locations is {distance} miles.")
```

And that's it! You now have a function that can calculate the distance between GPS coordinates in Python using the `geopy` library. You can use this code snippet to build location-based applications or perform distance calculations for other purposes.

Remember to import the necessary modules and provide valid coordinates for your particular use case. Happy coding!

#python #geolocation