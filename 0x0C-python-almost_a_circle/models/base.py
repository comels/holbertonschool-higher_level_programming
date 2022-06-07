#!/usr/bin/python3
"""the Base class"""
import json
import os


class Base:
    """the Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """function that create a instance of Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """that returns the JSON string representation of list_dictionaries"""
        return "[]" if list_dictionaries is None \
            else json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """that writes the JSON string representation of list_objs to a file"""
        filename = f"{cls.__name__}.json"
        liste = []
        liste.extend(i.to_dictionary() for i in list_objs)
        str = cls.to_json_string(liste)
        with open(filename, "w", encoding="utf-8") as file:
            return file.write(str)

    @staticmethod
    def from_json_string(json_string):
        """that returns the list of the JSON string
        representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """function that return instance with all attributes set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = f"{cls.__name__}.json"
        if os.path.exists(filename) is False:
            return []
        with open(filename, "r") as file:
            liste = cls.from_json_string(file.read())
            for i in range(len(liste)):
                liste[i] = cls.create(**liste[i])
        return liste