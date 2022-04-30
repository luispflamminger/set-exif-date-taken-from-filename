# set-exif-date-taken-from-filename
Python script that uses exiftool to change the date/time created/taken attributes of photos and videos using the date specified in the filename.

## Prerequesites
- [exiftool](https://exiftool.org/) needs to be available on the system (either in the current directory or on PATH)
- Filenames need to be structured like this: "YYYY-MM-DD-HH-MM*" (hyphens represent any single character, e.g. _ or :)

## Usage
1. Create a directory with all files you want to have edited.
1. Execute the script in that folder.
1. The script will edit all files in the directory it is executed in.  
   A backup of each file is created before editing, ending in "\_original".

## Development
This script is very basic at the moment. Pull requests are welcome.
- Regex is very rudimentary, could be improved.
- There is no handling of exiftool errors.
- Support for other date/time formats would be nice.
