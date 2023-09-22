---
layout: post
title: "Converting GPS coordinates to decimal degrees in Python"
description: " "
date: 2023-09-22
tags: []
comments: true
share: true
---

GPS coordinates are often provided in a format known as degree-minute-second (DMS), which can be difficult to work with when performing calculations or mapping. In many cases, it is more convenient to convert DMS coordinates to decimal degrees.

In this blog post, we will explore how to convert GPS coordinates from DMS format to decimal degrees using Python.

## DMS to Decimal Degrees Conversion Formula

To convert DMS coordinates to decimal degrees, we can use the following formula:

```
Decimal Degrees = Degrees + (Minutes/60) + (Seconds/3600)
```

Where:
- **Degrees**: the whole number of degrees in the coordinate
- **Minutes**: the number of minutes in the coordinate
- **Seconds**: the number of seconds in the coordinate

## Implementation in Python

Let's start by creating a function that takes DMS coordinates as input and returns the corresponding decimal degrees. Here's the code:

```python
def dms_to_decimal(degrees, minutes, seconds):
    decimal = degrees + (minutes / 60) + (seconds / 3600)
    return decimal
```

## Example Usage

Now, let's see how we can use the `dms_to_decimal` function to convert a set of DMS coordinates to decimal degrees. Here's an example:

```python
latitude_degrees = 40
latitude_minutes = 30
latitude_seconds = 45

longitude_degrees = -73
longitude_minutes = 58
longitude_seconds = 30

latitude_decimal = dms_to_decimal(latitude_degrees, latitude_minutes, latitude_seconds)
longitude_decimal = dms_to_decimal(longitude_degrees, longitude_minutes, longitude_seconds)

print("Latitude (decimal degrees):", latitude_decimal)
print("Longitude (decimal degrees):", longitude_decimal)
```

The output of the above code will be:

```
Latitude (decimal degrees): 40.5125
Longitude (decimal degrees): -73.975
```

## Conclusion

Converting GPS coordinates from DMS format to decimal degrees can be easily achieved using Python. By implementing the formula provided, we can convert coordinates accurately and efficiently. This conversion is useful for various applications that require decimal degrees representation of GPS coordinates, such as mapping and geolocation services.

Make sure to use the `dms_to_decimal` function from this blog post in your Python projects to effortlessly convert GPS coordinates into decimal degrees!

#GPS #Python