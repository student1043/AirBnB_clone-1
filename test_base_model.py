#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "Holberton"
my_model.my_number = 89
print(my_model)
my_model.save()

print("\n___\n")

print(my_model)

print("\n___\n")

my_model_json = my_model.to_dict()

print(my_model_json)

print("\n___\n")

print("JSON of my_model:")

print("\n___\n")


for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
