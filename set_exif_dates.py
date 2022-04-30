import os
import re

re_month = '(0[1-9]|[12][0-9]|3[01])'
re_day = '([0-2][0-9]|3[01])'
re_year = '[0-9]{4}'
re_hour = '([01][0-9]|2[0-4])'
re_minute = '[0-5][0-9]'
re_ending = '(?<!original)$'

regex = f'^{re_year}.{re_month}.{re_day}.{re_hour}.{re_minute}'

no_match_warning = ("Filename does not match pattern 'YYYY.MM.DD.HH.MM*'\n"
                    "'.' represents any single character.\n"
                    "'*' represents 0 or more of any character.\n"
                    "Skipping file...\n")

directory = os.getcwd()
count = 0

for file in sorted(os.listdir(directory)):
    filename = os.fsdecode(file)
    
    print(f"-----\nCurrent file: '{filename}'")
    if not re.search(regex, filename) or filename.endswith('_original'):
        print(no_match_warning)
        continue
        
    count += 1
    year = filename[0:4]
    month = filename[5:7]
    day = filename[8:10]
    hour = filename[11:13]
    minute = filename[14:16]
    
    print(f"Editing file...")
    os.system(f'exiftool -CreateDate="{year}:{month}:{day} {hour}:{minute}:00" {filename}\n')

print(f'=====\nFinished!\nEdited {count} of {len(os.listdir(directory))} files.')