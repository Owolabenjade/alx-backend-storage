#!/usr/bin/env python3
"""
Provides stats about Nginx logs stored in MongoDB with additional IP stats
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    
    # Count logs
    logs_count = nginx_collection.count_documents({})
    print(f"{logs_count} logs")
    
    # Methods stats
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"    method {method}: {count}")
    
    # Status check
    status_check_count = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_check_count} status check")
    
    # Top 10 IPs
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    
    top_ips = nginx_collection.aggregate(pipeline)
    
    print("IPs:")
    for ip_info in top_ips:
        print(f"    {ip_info.get('_id')}: {ip_info.get('count')}")