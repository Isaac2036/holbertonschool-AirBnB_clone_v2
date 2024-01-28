#!/usr/bin/python3
"""This module instantiates an object of class FileStorage or class DBStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from os import getenv

hbnb_storage = getenv('HBNB_TYPE_STORAGE')

storage = DBStorage() if hbnb_storage == 'db' else FileStorage()
storage.reload()
