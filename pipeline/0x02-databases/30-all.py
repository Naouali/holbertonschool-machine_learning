#!/usr/bin/env python3
"""
List all document in a mongo db
"""


def list_all(mongo_collection):
    """
    @mongo_ccollection: pymono collection object
    """
    return mongo_collection.find()