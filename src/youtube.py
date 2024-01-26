from datetime import datetime
import requests

def fetch_videos_from_youtube(api_keys, search_query):
    videos = []
    for api_key in api_keys:
        try:
            response = requests.get('https://www.googleapis.com/youtube/v3/search', params={
                'part': 'snippet',
                'q': search_query,
                'type': 'video',
                'order': 'date',
                'maxResults': 10,
                'key': api_key,
            })
            data = response.json()
            items = data.get('items', [])

            for item in items:
                video_data = {
                    'title': item['snippet']['title'],
                    'description': item['snippet']['description'],
                    'published_datetime': datetime.strptime(item['snippet']['publishedAt'], "%Y-%m-%dT%H:%M:%SZ"),
                    'thumbnails': item['snippet']['thumbnails']['medium']['url'],
                    'video_id': item['id']['videoId'],
                }
                videos.append(video_data)

        except Exception as e:
            print(f"Error fetching videos: {e}")

    return videos

def store_videos_in_mongodb(mongo, videos):
    if mongo.db is not None:
        if videos:
            video_instances = [Video(**video) for video in videos]
            mongo.db.videos.insert_many([video.to_dict() for video in video_instances])
