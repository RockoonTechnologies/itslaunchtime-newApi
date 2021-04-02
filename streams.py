# coded by the superior cameron
# aka ZegesMenden

import requests
from bs4 import BeautifulSoup
import json

streams = {
    "SpaceX": "https://www.youtube-nocookie.com/embed/live_stream?channel=UCtI0Hodo5o5dUb67FeUjDeA&autoplay=1",
    "NASASpaceflight": "https://www.youtube-nocookie.com/embed/live_stream?channel=UCSUu1lih2RifWkKtDOJdsBA&autoplay=1",
    "Everyday Astronaut": "https://www.youtube-nocookie.com/embed/live_stream?channel=UC6uKrU_WqJ1R2HMTY3LIx5Q&autoplay=1",
    "LabPadre": "https://www.youtube-nocookie.com/embed/live_stream?channel=UCFwMITSkc1Fms6PoJoh1OUQ&autoplay=1",
    "Overlook Horizon": "https://www.youtube-nocookie.com/embed/live_stream?channel=UCdxb3hRFmbaMCo8OZc6OCuQ&autoplay=1",
    "The Launch Pad": "https://www.youtube-nocookie.com/embed/live_stream?channel=UCGCndz0n0NHmLHfd64FRjIA&autoplay=1"
}

stream_json = {
    "SpaceX": False,
    "LabPadre": False,
    "NASASpaceflight": False,
    "Everyday Astronaut": False,
    "Overlook Horizon": False,
    "The Launch Pad": False
}


def get_streams():
    for stream in stream_json:
        URL = streams[stream]

        r = requests.get(URL)

        soup = BeautifulSoup(r.content, 'html5lib')

        table = soup.find('div', attrs={'class': 'submessage'})

        if not table.a:
            stream_json[stream] = False
        else:
            stream_json[stream] = True

    return stream_json