#!/usr/bin/env python3
"""insert"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in a collection based on kwargs.

    Args:
      mongo_collection: pymongo collection object.
      **kwargs: Keyword arguments representing the document fields and values.

    Returns:
      The _id of the newly inserted document.
    """
    # Insert the document with the provided kwargs
    result = mongo_collection.insert_one(kwargs)

    # Return the _id of the newly inserted document
    return result.inserted_id
