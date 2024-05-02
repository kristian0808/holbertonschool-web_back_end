#!/usr/bin/env python3
"""update_topics"""


def update_topics(mongo_collection, name, topics):
    """Updates the topics of a school document based on the name.

    Args:
      mongo_collection: The pymongo collection object.
      name (str): The name of the school to update.
      topics (list): The list of topics to set for the school.
    """
    # Update the document with the matching name
    mongo_collection.update_one({"name": name}, {"$set": {"topics": topics}})
