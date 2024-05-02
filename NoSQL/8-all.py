#!/usr/bin/env python3
from pymongo import MongoClient


def list_all(mongo_collection):
    """
    List all documents in the specified MongoDB collection.

    :param mongo_collection: PyMongo collection object
    :return: List of documents, or an empty list if no documents are found
    """
    documents = list(mongo_collection.find())
    return documents
