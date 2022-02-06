# import json
#
# with open('Sample.json') as f:
#    data = json.load(f)
#
# print(data)


#Python JSON to dict
# import json
#
# person = '{"name": "Bob", "languages": ["English", "French"]}'
# person_dict = json.loads(person)
#
# # Output: {'name': 'Bob', 'languages': ['English', 'French']}
# print( person_dict)
#
# # Output: ['English', 'French']
# print(person_dict['languages'])

#Convert dict to JSON

# import json
#
# person_dict = {'name': 'Bob',
# 'age': 12,
# 'children': None
# }
# person_json = json.dumps(person_dict)
#
# # Output: {"name": "Bob", "age": 12, "children": null}
# print(person_json)

#Writing JSON to a file

# import json
#
# person_dict = {"name": "Bob",
# "languages": ["English", "French"],
# "married": True,
# "age": 32
# }
#
# with open('person.txt', 'w') as json_file:
#   json.dump(person_dict, json_file)

#Python pretty print JSON
# import json
#
# person_string = '{"name": "Bob", "languages": "English", "numbers": [2, 1.6, null]}'
#
# # Getting dictionary
# person_dict = json.loads(person_string)
#
# # Pretty Printing JSON string back
# print(json.dumps(person_dict, indent = 4, sort_keys=True))

# Python program to update
# JSON
#
#
# import json
#
# # JSON data:
# x = '{ "organization":"JKTECH","city":"Bangalore","country":"India"}'
#
# # python object to be appended
# y = {"pin":110096}
#
# # parsing JSON string:
# z = json.loads(x)
#
# # appending the data
# z.update(y)
#
# # the result is a JSON string:
# print(json.dumps(z))

# Python program to update
# JSON

import json
# function to add to JSON
def write_json(new_data, filename='arraySample.json'):
    with open(filename, 'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["emp_details"].append(new_data)
        # Sets file's current position at offset.
        file.seek(1)
        # convert back to json.
        json.dump(file_data, file, indent=4)

    # python object to be appended


y = {"emp_name": "Jancy",
     "email": "Jancy@gmail.org",
     "job_profile": "Full Time"
     }

write_json(y)