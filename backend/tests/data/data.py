import os
import json

from crud import Models


def get_people():
    with open(os.path.join(os.path.dirname(__file__), '..','data\\valid\\people.json'), 'r') as f:
        return [Models.Person(**data) for data in json.load(f)]


def get_ratings():
    with open(os.path.join(os.path.dirname(__file__), '..','data\\valid\\ratings.json'), 'r') as f:
        return [Models.Rating(**data) for data in json.load(f)]


def get_users():
    with open(os.path.join(os.path.dirname(__file__), '..','data\\valid\\users.json'), 'r') as f:
        return [Models.User(**data) for data in json.load(f)]
