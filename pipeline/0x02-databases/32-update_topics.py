#!/usr/bin/env python3
"""
Update colllection using pymongo
"""


def update_topics(mongo_collection, name, topics):
    """
    @mongo_collection: pymongo object
    @name: string, name of the school
    @topics: list
    """
    mongo_collection.update_many({"name": name}, {"$set" :{"topics": topics}})
