from src.channel import Channel

if __name__ == '__main__':
    moscow_python = Channel(channel_id='UC-OVMPlMA3-YCIeg4z5z23A')

    # получаем значения атрибутов
    print(moscow_python.title)  # MoscowPython
    print(moscow_python.video_cnt)  # 736 (может уже больше)
    print(moscow_python.url)  # https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A

    # менять не можем
    try:
        moscow_python.channel_id = 'Новое название'
    except Exception as error:
        print(error)

    # AttributeError: property 'channel_id' of 'Channel' object has no setter

    # можем получить объект для работы с API вне класса
    print(Channel.get_service())
    # <googleapiclient.discovery.Resource object at 0x000002B1E54F9750>

    # создаем файл 'moscow_python.json' в данными по каналу
    moscow_python.to_json('moscow_python.json')
