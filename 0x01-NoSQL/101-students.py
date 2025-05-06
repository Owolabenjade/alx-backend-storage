#!/usr/bin/env python3
"""
Module for calculating top students by average score in MongoDB
"""


def top_students(mongo_collection):
    """
    Returns all students sorted by average score
    
    Args:
        mongo_collection: pymongo collection object
        
    Returns:
        List of students sorted by average score in descending order
    """
    # Use the MongoDB aggregation pipeline
    pipeline = [
        {
            "$project": {
                "name": 1,
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ]
    
    return list(mongo_collection.aggregate(pipeline))