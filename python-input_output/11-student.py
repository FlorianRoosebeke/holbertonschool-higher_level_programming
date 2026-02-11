#!/usr/bin/python3

class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):

            obj_dict = vars(self)
            dict_sort = {}

            for keys in attrs:
                if keys in obj_dict:
                    dict_sort[keys] = obj_dict[keys]
            return dict_sort

        else:
            return vars(self)


    def reload_from_json(self, json):
        for key in json:
            self.__dict__[key] = json[key]
