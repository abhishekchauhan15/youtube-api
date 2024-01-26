from datetime import datetime

class Video:
    def __init__(self, video_id, title, description, published_datetime, thumbnails, channel_id, channel_title):
        self.video_id = video_id
        self.title = title
        self.description = description
        self.published_datetime = published_datetime
        self.thumbnails = thumbnails
        self.channel_id = channel_id
        self.channel_title = channel_title

    def to_dict(self):
        return {
            'video_id': self.video_id,
            'title': self.title,
            'description': self.description,
            'published_datetime': self.published_datetime,
            'thumbnails': self.thumbnails,
            'channel_id': self.channel_id,
            'channel_title': self.channel_title,
        }
