#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """
    DBStorage class provides a simple interface for interacting with
    a MySQL database
    using SQLAlchemy. It includes methods for querying, adding,
    saving, and deleting
    objects in the database.
    """
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
        """Query all objects from the db session based on class name"""
        classes = [User, State, City, Amenity, Place, Review]
        result_dict = {}

        if cls:
            classes = [cls]

        for class_obj in classes:
            objects = self.__session.query(class_obj).all()
            for obj in objects:
                key = f"{obj.__class__.__name__}.{obj.id}"
                result_dict[key] = obj
        return result_dict

    def new(self, obj):
        """Add the object to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete the object from the current database session."""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and initialize a session."""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def close(self):
        self.__session.close()
