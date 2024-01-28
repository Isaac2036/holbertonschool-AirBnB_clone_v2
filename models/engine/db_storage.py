#!/usr/bin/python3
"""Module to create a mysql engine"""

import os
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker


class DBStorage:
    """This class creates the engine for a mysql database
    storage system"""

    all_classes = {"BaseModel": BaseModel, "User": User, "State": State,
                   "City": City, "Amenity": Amenity, "Place": Place,
                   "Review": Review}
    __engine = None
    __session = None

    def __init__(self):
        hbnb_user = getenv("HBNB_MYSQL_USER")
        hbnb_pass = getenv("HBNB_MYSQL_PWD")
        hbnb_host = getenv("HBNB_MYSQL_HOST")
        hbnb_db = getenv("HBNB_MYSQL_DB")
        hbnb_env = getenv("HBNB_ENV")

        # Configure the engine with environment variable values
        self.__engine = create_engine(
            f"mysql+mysqldb://{hbnb_user}:{hbnb_pass}@{hbnb_host}:\
                    3306/{hbnb_db}",
            pool_pre_ping=True
        )

        # Drop all tables if environment variable HBNB_ENV equals test
        if hbnb_env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all objects for curent session based on class name"""
        obj_dict = {}
        cls = self.all_classes[cls]
        if cls is not None:
            objects = self.__session.query(cls).all()
        else:
            objects = self.__session.query(
                State, City, User, Amenity, Place, Review)
        for obj in objects:
            key = obj.__class__.__name__ + '.' + obj.id
            value = obj
            obj_dict[key] = value
        return obj_dict

    def new(self, obj):
        """Add object to current database session"""
        self.__session.add(obj)
        self.__session.flush()

    def save(self):
        """Commit changes to the current databases session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete object from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and initialize a session."""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)
        
    def close(self):
        """ call close on private session. """
        self.__Session.close()
