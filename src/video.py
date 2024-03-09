from src.channel import Channel
import json
import os


class Video:
    def __init__(self, video_id):

        self.__video_id = video_id
        self.url = os.path.join('https://www.youtube.com/watch?v=', video_id)

        self.video = Channel.get_service().videos().list(part='snippet, statistics',
                                                         id=video_id).execute()
        video_info = self.video['items'][0]
        self.title = video_info['snippet']['title']
        self.likes_cnt = int(video_info['statistics']['likeCount'])
        self.view_cnt = int(video_info['statistics']['viewCount'])

    def __str__(self):
        return self.title

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.video, indent=2, ensure_ascii=False))


class PLVideo(Video):
    def __init__(self, video_id: str, playlist_id: str):
        super().__init__(video_id)
        self.playlist_id = playlist_id
