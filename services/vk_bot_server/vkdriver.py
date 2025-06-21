import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id

def main():
    vk_session = vk_api.VkApi(token='vk1.a.p3TgoZp739CxuIey-kh87vj-OnfTbRNCtinIqAtDSrydtq70gS7tZ340onZOBitaTIaDmXYBfdbr9rJ8tCEDEbgmy4TH3Dyn3Kd1ziGcaTKtY4dPpzrM67ZddJ5IgS2eVoPg5g8nmWB1I7NC0upMa3U6JE7jJx-LNV9rXRsYr1z1Sbs79AgHEgJo7lKHLmIrBsKsWeivSJ2InjaQ6m4RzQ')
    vk = vk_session.get_api()