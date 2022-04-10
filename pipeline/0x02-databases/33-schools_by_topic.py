#!/usr/bin/env python3
"""
Filter by topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    @mango_collection: pymongo object
    @topic: string
    """

    return [subject for subject in mongo_collection.find({"topics":topic})]