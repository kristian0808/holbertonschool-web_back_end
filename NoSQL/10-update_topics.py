#!/usr/bin/env python3
"""
Module to update topics in MongoDB documents.
"""


def update_topics(mongo_collection, name, topics):
    """
    Updates the topics of a school document based on the school name.

    Args:
    mongo_collection: pymongo collection object
    name (str): the school name to update
    topics (list of str): the list of topics approached in the school
    """
    query = {"name": name}
    new_values = {"$set": {"topics": topics}}
    mongo_collection.update_many(query, new_values)
