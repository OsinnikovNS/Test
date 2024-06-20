"""https://ya.ru/video/preview/1524250325107953379""" # получение access token
from config import TOKEN_GROUP_ID
import random
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll
import logging

logger = logging.getLogger('bot')
def configure_logger():
    stream_handler = logging.StreamHandler()
    file_handler = logging.FileHandler('bot_log.log')
    stream_handler.setFormatter(logging.Formatter('%(asctime)s %(levellname)s %(message)s'))
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levellname)s %(message)s'))
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)
    stream_handler = set.Level(logging.INFO)
    logger.set.Level(logging.DEBUG)
configure_logger()
# logging.DEBUG
# logging.INFO
# logging.WARNING
# logging.ERROR
# logging.CRITICAL


class Bot():
    def __init__(self, group_id, token):
        self.group_id = group_id
        self.token = token
        self.vk = vk_api.VkApi(token=token)
        self.longpoll = VkBotLongPoll(self.vk, self.group_id)
        self.api = self.vk.get_api()

def on_event(self, event: VkBotLongPoll):
    if event.type == VkBotEventType.MESSAGE_NEW:
        # print(event.type)
        logger.info("Event got %s", event)
        logger.info("We reccieved an event %s", event.type)
        peer_id = event.message.peer_id
        random_id = random.randint(0, 2**20)
        text_message = str(even.message.text)
        try:
            self.api.messages.send(peer_id=peer_id, message=text_message, random_id=random_id)
        except Exception as exception:
            logger.exception('Exception %s', exception)
            # print("Exception:", exception)






    else:
        print('Мы не знаем как отрабатывать эти сообщения', event.type)
        logger.debug('Мы не знаем как отрабатывать эти сообщения %s', event.type)



if __name__ == '__main__':
    bot = Bot(GROUP_ID, TOKEN)
    bot.run()
