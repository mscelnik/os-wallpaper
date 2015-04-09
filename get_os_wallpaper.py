#!/usr/bin/env python3
""" Script to download the monthly wallpaper from the Ordnance Survey
"""

__author__ = 'Matthew Celnik'
__copyright__ = 'Matthew Celnik'
__licence__ = 'All rights reserved'
__maintainer__ = 'Matthew Celnik'
__email__ = 'matthew@celnik.co.uk'
__status__ = 'Prototype'

# import urllib
import re
from xml.dom.minidom import parseString

# The main URL you visit to download the wallpapers from a web browser.  We want
# to download the page and search it for the current month and year.
# url = 'http://www.ordnancesurvey.co.uk/resources/wallpaper.html'

# page = urllib.request.urlopen(url)
# html = str(page.read())
# page.close()

page = open('os.html')
html = str(page.read())
page.close()

# html = '<p><p class="desc">December 2014 wallpaper</p></p>'

# Use regular expressions to find the current month and year.
# pattern = r'(?<=>).+[0-9]+(?= wallpaper</p>)'
pattern = '(?<=(<p class="desc">)).+'
matches = re.search(pattern, html)

print(matches)
if matches:
    print(matches.group(0))
    date = matches.group(0).split(' ')
    print(date)


# This is the URL directory containing all the wallpapers.  The wallpapers are
# identical but different sizes.
wp_dir = 'http://www.ordnancesurvey.co.uk/docs/wallpaper-images/'

# List of image sizes to download.
reqd_sizes = ('1920x1200.jpg')
