import json 
import os

file_name = 'students.json'

if not os.path.exists(file_name) or os.path.getsize(file_name) == 0:
    with open(file_name, 'w') as f:
        json.dump({}, f)

with open(file_name, 'r') as f:
    obj = json.load(f)

obj['key'] = 'value'

with open(file_name, 'w') as f:
    json.dump(obj, f, indent=4)

print("successfully updated the file")