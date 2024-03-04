import json
import os
from googleapiclient.discovery import build, Resource


class Channel:
    """Класс для ютуб-канала"""

    # YT_API_KEY скопирован из гугла и вставлен в переменные окружения
    api_key: str = os.getenv('YT_API_KEY')

    # создать специальный объект для работы с API
    youtube: Resource = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.url = os.path.join('https://www.youtube.com/channel/', channel_id)

        self.channel = Channel.youtube.channels().list(id=channel_id, part='snippet,statistics').execute()

        root_branch = self.channel['items'][0]
        self.title = root_branch['snippet']['title']
        self.description = root_branch['snippet']['description']

        self.subscriber_cnt = int(root_branch['statistics']['subscriberCount'])
        self.video_cnt = int(root_branch['statistics']['videoCount'])
        self.view_cnt = int(root_branch['statistics']['viewCount'])

    def __str__(self):
        return f"{self.title} ({self.url})"

    def __repr__(self):
        return f"{__class__.__name__}(channel_id='{self.__channel_id}')"

    def __add__(self, other):
        if isinstance(other, Channel):
            return self.subscriber_cnt + other.subscriber_cnt

    def __sub__(self, other):
        if isinstance(other, Channel):
            return self.subscriber_cnt - other.subscriber_cnt

    def __eq__ (self, other):
        if isinstance(other, Channel):
            return self.subscriber_cnt == other.subscriber_cnt

    def __ne__(self, other):
        if isinstance(other, Channel):
            return self.subscriber_cnt != other.subscriber_cnt

    def __gt__(self, other):
        if isinstance(other, Channel):
            return self.subscriber_cnt > other.subscriber_cnt

    def __ge__(self, other):
        if isinstance(other, Channel):
            return self.subscriber_cnt >= other.subscriber_cnt

    def __lt__(self, other):
        if isinstance(other, Channel):
            return self.subscriber_cnt < other.subscriber_cnt

    def __le__(self, other):
        if isinstance(other, Channel):
            return self.subscriber_cnt <= other.subscriber_cnt

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls) -> Resource:
        """Возвращает объект для работы с YouTube API"""
        return Channel.youtube

    def to_json(self, file_name):
        """Cохраняет в файл значения атрибутов экземпляра Channel"""
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(self.__dict__, f, indent=4)

    @property
    def channel_id(self):
        """Геттер атрибуты channel_id"""
        return self.__channel_id

