#!/usr/bin/env python3
"""Returns a list of schools that have a specific topic."""


def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of schools that have a specific topic.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection object.
        topic (str): The topic to search for.

    Returns:
        list: A list of school documents that have the specified topic.
    """
    return list(mongo_collection.find({"topics": topic}))
