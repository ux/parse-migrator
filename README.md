<a href="https://github.com/stackmob/stackmob-parse-migrator">stackmob-parse-migrator</a>
============

<a href="https://www.stackmob.com/parse/">&larr; Back to Migrate from Parse</a> | Visit the <a href="https://github.com/stackmob/stackmob-parse-migrator">Open Source GitHub Repo for stackmob-parse-migrator</a>

# What is this?

A simple python script to add exported Parse zipped json data to StackMob.

By running this python script against the Parse json export files, your schemas will automatically be created in StackMob, and your data will be populated to the datastores.  Subobjects are created with their own schemas so that they have their own collection - this is a StackMob implementation of relationships where we don't store subobjects within objects.  We store references to subojects by id and do a pseudo "join" on them to return it to you.

After you run this script, your schemas and data should be in StackMob and you can then <a href="https://developer.stackmob.com/tutorials">get started with the SDKs!</a>



# Setup

* Install pip (`brew install python` works on mac)
* `pip install stackmob-parse-migrator` or clone this repo
* Create an app on [StackMob](https://www.stackmob.com)
* If you're importing geopoints, create schema with geopoint fields using the same names you had on Parse. All other schema types can be inferred and you don't need to worry about them.
* Get your api key and secret from [the dashboard](https://dashboard.stackmob.com/settings)
* Unzip the parse export zip to somewhere on your harddrive
* Windows only: Rename any relation JSON files (see Windows Caveats below)

# Usage

```js
stackmob-parse-migrator --api_key=YOUR PUBLIC KEY --api_secret=YOUR PRIVATE KEY --path=/path/to/unzipped-json/folder --verbose 1
```

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

## Python isn't installed

Please visit http://www.python.org/getit/ to download a Python distribution for your Windows platform. We have tested this script successfully on Windows 7 using ActivePython 2.7.2.

## Bad filenames

If your application uses relations in its schemas, then the zip archive you downloaded from Parse has files of the form `_Join:<relationName>:_<schemaName>.json`. Windows handles this badly, and some zip clients do too.  We recommend that you rename these files after unarchiving to the form `_Join#<relationName>#_<schemaName>.json`

## Can't find the migrator script

Windows may not be able to find `stackmob-parse-migrator` at the command prompt. If you installed the script using `pip`, then it should reside in `C:\Python27\Scripts`, or wherever your Python installation lives. Navigate to that directory, and execute the script directly from there, e.g. `python .\stackmob-parse-migrator --api_key=...`

# Contributing

This project is open source!  You are welcome to modify this and improve it as you come along.  There's such a variety of data out there that we hope we've covered, but just in case you find any corner cases, we and other developers would truly be grateful for your contributions :)  Thanks, and happy coding!
