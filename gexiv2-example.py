#!/bin/env python

from sys import argv, exit

try:
    from gi.repository import GExiv2
except ImportError:
    exit('You need to install gexiv2 first.')

if len(argv) < 2:
    exit('Please specify an image on the commandline.')

# Note, these are equivalent:
# metadata = GExiv2.Metadata()
# metadata.open_path(argv[-1])
metadata = GExiv2.Metadata(argv[-1])

# Currently, the Metadata class can be thought of as a dict mapping strings to strings.
# Here are some examples of getting and setting strings from photo tags:

tag = 'Exif.Image.Model'

if tag in metadata:
    print('Your camera is a:', metadata[tag])
else:
    print('Your camera is unknown.')

city = 'Tuktuyaaqtuuq'
metadata['Iptc.Application2.City'] = city
if metadata['Iptc.Application2.City'] == city:
    print('I just set the city to %s.' % city)
    print("Don't worry, I won't save it. ;-)")
else:
    print('There was a problem setting the IPTC city tag.')

# Like a dict, the `get` method returns None instead of raising KeyError.
print("Don't raise a KeyError:", metadata.get('Invalid Tag', 'default') == 'default')

print('This photo has %d tags.' % len(metadata))

# The GExiv2 API provides some alternate methods when you want something nicer
# than just some strings to play with though. Here's some examples:

# Returns three floats, longitude first, then latitude, then altitude
print('Photo taken at:', metadata.get_gps_info())

# Returns a fractions.Fraction
print('Altitude:', metadata.get_exif_tag_rational('Exif.GPSInfo.GPSAltitude'))

# Another fractions.Fraction
print('Exposure time: %s s' % metadata.get_exposure_time())

# Returns a datetime.datetime
print('Timestamp:', metadata.get_date_time())

# ints
print('Dimensions: %s by %s' % (metadata.get_pixel_width(), metadata.get_metadata_pixel_height()))

# int
print('Rating: %s' % metadata.get_rating())

# GExiv2.Orientation instance, you can see how to compare it here
print('Normal orientation:', metadata.get_orientation() is GExiv2.Orientation.NORMAL)

# GExiv2.PreviewProperties instance
props = metadata.get_preview_properties()[0]
print(props)

image = metadata.get_preview_image(props)
print(image)

print('Preview: %s bytes' % len(image.get_data()))

# Raw thumbnail data, usually JPEG format I guess
print('Thumbnail: %s bytes.' % len(metadata.get_exif_thumbnail()))

# If you wanted to save your changes, call save_file:
#metadata.save_file()
