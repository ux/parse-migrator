stackmob-parse-migrator
============

A simple python script to add exported Parse data to StackMob

# Setup
* Install pip (`brew install python` works on mac)
* `pip install requests`
* `pip install python-dateutil`
* `pip install stackmob-parse-migrator` or clone this repo
* Create an app on [StackMob](stackmob.com)
* If you're importing geopoints, create schema with geopoint fields using the same names you had on Parse. All other schema types can be inferred and you don't need to worry about them.
* Get your api key and secret from [the dashboard](https://dashboard.stackmob.com)
* Unzip the parse export zip to somewhere on your harddrive

# Usage
stackmob-parse-migrator --api_key=MY_KEY --api_secret=MY_SECRET --path=/path/to/unzipped/folder --verbose 1

# Supported Import types
* Primitives data types
* Arrays
* ID fields
* Overriding createddate/lastmoddate
* Geopoints
* Dates
* Relations
* Subobjects
* Pointers

# Futures
* Binary Files

# Limitations
* Mixed type arrays are not allowed (this is a feature)
* Subobjects greater than 1 level deep can't be migrated
* StackMob doesn't support actual subobjects. Subobjects will be split off into separate relations, which can be joined together by using the expand feature
* StackMob doesn't have a date format. Dates are stored as longs in unix time
* This script loads all the objects for each collection into memory. This could lead to OOM with sufficiently large datasets
