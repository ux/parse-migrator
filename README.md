stackmob-parse-migrator
============

A simple python script to add exported Parse data to StackMob

# Setup
* Install pip (`brew install python` works on mac)
* `pip install requests`
* `pip install python-dateutil`
* `pip install stackmob-parse-migrator` or clone this repo
* Create an app on [StackMob](https://www.stackmob.com)
* If you're importing geopoints, create schema with geopoint fields using the same names you had on Parse. All other schema types can be inferred and you don't need to worry about them.
* Get your api key and secret from [the dashboard](https://dashboard.stackmob.com/settings)
* Unzip the parse export zip to somewhere on your harddrive
* Windows only: Rename any relation JSON files (see Windows Caveats below)

# Usage

`stackmob-parse-migrator --api_key=MY_KEY --api_secret=MY_SECRET --path=/path/to/unzipped/folder --verbose 1`

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

# Windows Caveats

## Bad filenames

If your application uses relations in its schemas, then the zip archive you downloaded from Parse has these stored with filenames in a format similar to `_Join:<relationName>:_<schemaName>.json`. Neither OS X nor Windows can properly handle colons in filenames, though. OS X converts these to forward-slashes when you unarchive the zip, preserving a meaningful separator. Windows, however, converts these to underscores (and generates several error messages in the process), which loses the separator, as both Parse and StackMob support underscores in schema and relation names.

We recommend that you:
* Unarchive the zip file to a directory of your choosing
* Open the zip file in Windows Explorer or another archive viewer to see which files were affected
* Rename any affected files using a system-safe separator, e.g. `Join#<relationName>#_<schemaName>.json`

## Can't find the migrator script

Windows may not be able to find `stackmob-parse-migrator` at the command prompt. If you installed the script using `pip`, then it should reside in `C:\Python27\Scripts`, or wherever your Python installation lives. Navigate to that directory, and execute the script directly from there, e.g. `python .\stackmob-parse-migrator --api_key=...`
