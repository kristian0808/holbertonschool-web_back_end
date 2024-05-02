#!/usr/bin/env python3
"""Returns stats about Nginx logs stored in MongoDB."""

import pymongo


def log_stats(mongo_collection):
    """
    Returns stats about Nginx logs stored in MongoDB.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection object.

    Returns:
        None
    """
    total_logs = mongo_collection.count_documents({})
    print(f"{total_logs} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = mongo_collection.count_documents({"method": method})
        print(f"    method {method}: {count}")

    status_checks = mongo_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_checks} status check")


if __name__ == "__main__":
    client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
    db = client["logs"]
    collection = db["nginx"]

    log_stats(collection)
