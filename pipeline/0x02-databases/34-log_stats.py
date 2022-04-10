#!/usr/bin/env python3
""" 
print logs
"""

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.logs.nginx
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print(f'{school_collection.count_documents({})} logs')
    print('Methods:')
    for m in methods:
        print('\tmethod {}: {}'.format(
            m, school_collection.count_documents({'method': m})))
    print('{} status check'.format(school_collection.count_documents(
        {'method': 'GET', 'path': '/status'})))