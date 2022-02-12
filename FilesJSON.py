# # JSON JavaScript Object Notation is a format for structuring data.
# # It is mainly used for storing and transferring data between the browser and the server.
# # Python too supports JSON with a built-in package called json.
# # This package provides all the necessary tools for working with JSON Objects including parsing,
# # serializing, deserializing, and many more. Let’s see a simple example where we convert
# # the JSON objects to Python objects and vice-versa.
#
# #Example 1
# import json
#
# # JSON string
# employee = '{"id":"09", "name": "John", "department":"HR"}'
#
# # Convert string to Python dict
# employee_dict = json.loads(employee)
# print(employee_dict)
# print(type(employee_dict))
# print("\n")

# # Convert Python dict to JSON
# json_object = json.dumps(employee_dict, indent=4)
# print(json_object)
# print(type(json_object))
#
# # The full form of JSON is JavaScript Object Notation.
# # It means that a script (executable) file which is made of text
# # in a programming language, is used to store and transfer the data.
# # Python supports JSON through a built-in package called JSON.
# # To use this feature, we import the JSON package in Python script.
# # The text in JSON is done through quoted-string which contains
# # the value in key-value mapping within { }. It is similar to the dictionary in Python.
#
# #Example 2
# # Python program showing
# # use of json package
#
# import json
#
# # {key:value mapping}
# a ={"name":"John",
#     "age":31,
# 	"Salary":25000}
#
# # conversion to JSON done by dumps() function
# b = json.dumps(a)
#
# # printing the output
# print(repr(b))
# print(type(b))
#
# #Example 3
# # Python program showing that
# # json support different primitive
# # types
# #PYTHON OBJECT TO JSON OBJECT
# import json
#
# # list conversion to Array
# print(json.dumps(['Welcome', "to", "JSON"]))
#
# # tuple conversion to Array
# print(json.dumps(("Welcome", "to", "JSON")))
#
# # string conversion to String
# print(json.dumps("Hi"))
#
# # int conversion to Number
# print(json.dumps(123))
#
# # float conversion to Number
# print(json.dumps(23.572))
#
# # Boolean conversion to their respective values
# print(json.dumps(True))
# print(json.dumps(False))
#
# # None value to null
# print(json.dumps(None))

# Serializing JSON :
# The process of encoding JSON is usually called serialization.
# This term refers to the transformation of data into a series of bytes
# hence serial) to be stored or transmitted across a network.
# To handle the data flow in a file, the JSON library in Python uses dump()
# function to convert the Python objects into their respective JSON object,
# so it makes easy to write data to files.
#
# Deserializing JSON :
# Deserialization is the opposite of Serialization, i.e. conversion of JSON objects
# into their respective Python objects. The load() method is used for it.
# If you have used JSON data from another program or obtained it as a string format of JSON,
# then it can easily be deserialized with load(), which is usually used to load from string,
# otherwise, the root object is in a list or dict.

#Example 4
# import json
# var = {
#       "Subjects": {
#                   "Maths":85,
#                   "English":90
#                    }
#       }
# with open("arraySample.json", "w") as p:
# 	json.dump(var, p)


# Python program to read
# json file

# import json
#
# # Opening JSON file
# f = open('data.json','r')
#
# # returns JSON object as
# # a dictionary
# data = json.load(f)
# #
#
# # # Iterating through the json
# # # list
# for i in data['employee']:
# 	print(i)
#
# # Closing file
# f.close()
# # Python program to write JSON
# # to a file


import json

# Data to be written
dictionary ={
         "id": "05",
         "name": "Nancy",
         "department": "Sales"
      }

with open("data.json", "a") as outfile:
	json.dump(dictionary, outfile,indent = 4)






