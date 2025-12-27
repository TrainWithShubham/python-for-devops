"""
Packages:
 are python functions that can be imported 
 in some other code file
"""
import json

def read_file(filename):
    with open(filename, "r") as file:
        return file.readlines()
    
def write_json(filename,json_object):
    with open(filename, "w+") as file:
        json.dump(json_object,file)

