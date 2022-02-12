#json.loads(): json.loads() function is present in python built-in ‘json’ module.
# This function is used to parse the JSON string.
#json.dumps(): json.dumps() function is present in python built-in ‘json’ module.
# This function is used to convert Python object into JSON string.


#Example 1
# import json
#
# with open('Sample.json') as f:
#    data = json.load(f)
#
# print(data)

#Example 2
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

#Example 3
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

#Example 4
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

#Example 5
#Python pretty print JSON
# import json
#
# person_string = '{"name": "Bob", "languages": "English", "numbers": [2, 1.6, null]}'
#
# # Getting dictionary
# person_dict = json.loads(person_string)
#
# # Pretty Printing JSON string back
# print(json.dumps(person_dict, indent = 4))

#Example 6
# Python program to update JSON
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

#Example 7
# Python program to update JSON

import json
# function to add to JSON
def write_json(new_data, filename='data.json'):
    with open(filename, 'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["employee"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent=4, sort_keys=True)

# python object to be appended
y = {
         "id": "04",
         "name": "JKTE",
         "department": "HR"
      }

write_json(y)

#Example 8
#json.dump() method can be used for writing to JSON file. Write data to a file-like object in json format.

# import module
# import json
#
# # Data to be written
# data = {
# 	"user": {
# 		"name": "John",
# 		"age": 21,
# 		"Place": "Bangalore",
# 		"Blood group": "O+"
# 	}
# }
#
# # Serializing json and
# # Writing json file
# with open( "datafile.json" , "w" ) as write:
# 	json.dump( data , write )

#Example 9
#json.dumps()
#json.dumps() method can convert a Python object into a JSON string.

# import module
# import json
#
# # Data to be written
# data = {
# 	"user": {
# 		"name": "Peter",
# 		"age": 21,
# 		"Place": "Hyderabad",
# 		"Blood group": "B+"
# 	}
# }
#
# # Serializing json
# res = json.dumps( data )
# print( res )
