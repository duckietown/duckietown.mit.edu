#!usr/bin/env python
import os, yaml, glob, sys
sys.path.append("../../")
from generate_lectures import read_yaml_dict

yaml_files = glob.glob( "images/*.yaml")

people = {
        'training' : {},
        'operations' : {},
        'sponsors' : {},
        'management': {},
        'special-ops':{},
        'advisory':{},
    }

for filename in yaml_files:
    
    person = read_yaml_dict(filename)
    name = filename.strip(".yaml").strip("images/")
    person_jpg = name +".jpg"
    person_full_name = person["name"]
    tag = None
    for tag_type in people.keys():
        if tag_type in person["tags"]:
            tag = tag_type
    if tag == None: print name; continue

    people[tag][person_full_name] = person_jpg

sorted_people = {}
for tag in people:
    names = people[tag].keys()
    names.sort()
    sorted_people[tag] = [(name, people[tag][name]) for name in names]
    print sorted_people[tag]
    raw_input()

