#!/usr/bin/env python3
"""
Insert document in mongo db using python
"""


def insert_school(mongo_collection, **kwargs):
    """
    @mongo_collection: pymongo object
    @kwargs: attributes to be set
    """

    new = mongo_collection.insert_one(kwargs)
    return new.inserted_id