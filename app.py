# app.py
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from apscheduler.schedulers.background import BackgroundScheduler
from pymongo import MongoClient
from bson import json_util
from src.config import MONGO_URI, API_KEYS, SEARCH_QUERY
from src.models import Video
from src.youtube import fetch_videos_from_youtube, store_videos_in_mongodb

app = Flask(__name__)
app.config["MONGO_URI"] = MONGO_URI
mongo = PyMongo(app)

# Background job to fetch and store videos
def fetch_and_store_videos():
    print("Getting the new videos...")
    videos = fetch_videos_from_youtube(API_KEYS, SEARCH_QUERY)
    store_videos_in_mongodb(mongo, videos)

# indexing
if mongo.db is not None:
    mongo.db.videos.create_index([('published_datetime', -1)])
    mongo.db.videos.create_index([('video_id', 1)])

# API to test connection
@app.route('/hello', methods=['GET'])
def test_connection():
    return jsonify({'message': 'Hello!'})

# API to return paginated videos
@app.route('/videos', methods=['GET'])
def get_paginated_videos():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    if mongo.db is not None:
        videos = mongo.db.videos.find().sort('published_datetime', -1).skip((page - 1) * per_page).limit(per_page)
        videos_list = json_util.loads(json_util.dumps(videos, default=lambda x: x.__dict__))

        return jsonify({'videos': videos_list})
    else:
        return jsonify({'error': 'MongoDB connection not established'})


def create_video_list_response(videos):
    """
    Create a response for paginated videos.
    """
    return [{
        'title': video['title'],
        'description': video['description'],
        'published_datetime': video['published_datetime'].isoformat(),
        'thumbnails': video['thumbnails'],
        'video_id': video['video_id'],
    } for video in videos]
    

if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(fetch_and_store_videos, 'interval', seconds=10)
    scheduler.start()
    app.run(debug=True)
