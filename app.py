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



if __name__ == '__main__':
    app.run(debug=True)
