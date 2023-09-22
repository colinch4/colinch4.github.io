---
layout: post
title: "Geo-tagging photos using GPS data in Python"
description: " "
date: 2023-09-22
tags: [geotagging]
comments: true
share: true
---

In today's digital age, most smartphones and cameras come equipped with GPS capabilities, allowing us to capture the location where a photo was taken. This information, known as GPS metadata, can be extremely useful when organizing and categorizing our photo collections. 

In this blog post, we will walk through a Python code example that demonstrates how to extract GPS data from photos and use it to geo-tag them.

## Required Libraries

To begin, we will need to install the `PIL` (Python Imaging Library) and `piexif` libraries to work with image files and their metadata. You can install these libraries using `pip`:

```bash
pip install Pillow piexif
```

## Extracting GPS Data

First, we need to extract the GPS metadata from the photo. 

```python
from PIL import Image
from PIL.ExifTags import TAGS

# Load the image
image = Image.open('photo.jpg')

# Extract the Exif data
exif_data = image._getexif()

# Iterate through the Exif data
for tag, value in exif_data.items():
    if TAGS.get(tag) == 'GPSInfo':
        gps_info = value
        break
```

In the above code, we use the `Image` class from the `PIL` library to open the image file. The `ExifTags` module provides a mapping between the Exif tag numbers and their human-readable names. By iterating through the Exif data, we can locate the GPS metadata and store it in the `gps_info` variable.

## Extracting GPS Coordinates

Next, we can extract the latitude and longitude coordinates from the GPS metadata.

```python
gps_latitude = gps_info[2]
gps_longitude = gps_info[4]

latitude = gps_latitude[0] + gps_latitude[1] / 60 + gps_latitude[2] / 3600
longitude = gps_longitude[0] + gps_longitude[1] / 60 + gps_longitude[2] / 3600

if gps_info[1] == 'S':
    latitude = -latitude

if gps_info[3] == 'W':
    longitude = -longitude

print(f"Latitude: {latitude}")
print(f"Longitude: {longitude}")
```

In the above code, we extract the latitude and longitude values from the GPS metadata using their respective indices in the `gps_info` array. We convert the coordinates from degrees, minutes, and seconds to decimal degrees by applying the appropriate conversion formulas. Lastly, we account for the southern and western hemispheres by negating the latitude and longitude values if necessary.

## Geo-tagging the Photo

Now that we have the GPS coordinates, let's see how we can use them to geo-tag the photo.

```python
from geopy.geocoders import Nominatim

# Create a geocoder instance
geolocator = Nominatim(user_agent='photo_geo_tagger')

# Reverse geocode the coordinates to get the location information
location = geolocator.reverse((latitude, longitude), exactly_one=True)

# Get the address from the location information
address = location.address

# Add the location information to the photo's metadata
exif_data['XPComment'] = address.encode()

# Save the modified image
image.save('photo_geo_tagged.jpg')

print("Geo-tagging complete!")
```

In the above code, we utilize the `geopy` library to perform reverse geocoding. By passing the latitude and longitude coordinates to the `reverse()` method, we can obtain the location information, such as the address, corresponding to those coordinates. We then add this information to the photo's metadata using the `XPComment` field. Finally, we save the modified image with the geo-tagged metadata.

## Conclusion

In this tutorial, we explored how to extract GPS metadata from photos and utilize it to geo-tag them using Python. Geo-tagging our photos allows us to organize and search for them based on location, providing a more immersive and personalized experience.

As always, feel free to experiment and adapt the code examples to suit your specific requirements. Happy coding!

#python #geotagging