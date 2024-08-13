"""https://ya.ru/video/preview/1524250325107953379"""  # видеоурок получение access token
#  Python version 3.12
from config_bot import TOKEN, GROUP_ID
import random
from dotenv import load_dotenv
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType, VkBotEvent
import logging

logger = logging.getLogger('bot')


def configure_logger():
    stream_handler = logging.StreamHandler()
    file_handler = logging.FileHandler('bot.log')
    stream_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)
    stream_handler.setLevel(logging.INFO)
    logger.setLevel(logging.DEBUG)


configure_logger()


class Bot():
    """echo bot for VK"""

    def __init__(self, group_id, token):
        """принимает параметры group_id: id группы из ВК, token: секретный ключ доступа к группе"""
        self.group_id = group_id
        self.token = token
        self.vk = vk_api.VkApi(token=token)
        self.longpoll = VkBotLongPoll(self.vk, self.group_id)
        self.api = self.vk.get_api()

    def run(self):
        for event in self.longpoll.listen():
            try:
                self.on_event(event)
            except Exception as exception:
                logger.exception("Exception %s", exception)

    def on_event(self, event: VkBotEvent):
        """Обработчик события сообщения от бота"""
        if event.type == VkBotEventType.MESSAGE_NEW:
            # print(event.type)
            logger.info("Event got %s", event)
            logger.info("We received an event %s", event.type)
            peer_id = event.message.peer_id
            random_id = random.randint(0, 2 ** 20)
            text_message = str(event.message.text)
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
