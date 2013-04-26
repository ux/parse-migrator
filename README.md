stackmob-parse-importer
============

A simple python script to add exported Parse data to StackMob

# Usage
python stackmob-parse-importer --api_key=MY_KEY --api_secret=MY_SECRET --path=/path/to/unzipped/folder --verbose 1

# Supported
* Primitives data types
* Arrays
* id fields
* createddate/lastmoddate

# For v1
* Relations
* Geopoints
* Pointers
* Dates
* Subobjects

# Futures
* Binary Files

# Never supported
* Mixed type arrays
* Subobjects greater than 1 level deep

# Quirks
* StackMob doesn't have a date format. Dates are stored in unix time
* StackMob doesn't support subobjects. Subobjects will be split off into separate relations, which can be joined together by using the expand feature

