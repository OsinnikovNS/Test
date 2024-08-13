
import vk_api
import config_bot
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType, VkBotEvent
import random

token = config_bot.TOKEN
group_id = config_bot.GROUP_ID


class Bot():
    def __init__(self, group_id, token):
        self.group_id = group_id
        self.token = token
        self.vk = vk_api.VkApi(token=token)
        self.longpoll = VkBotLongPoll(self.vk, self.group_id)
        self.api = self.vk.get_api()

    def run(self):
        for event in self.longpoll.listen():
            self.on_event(event)

    def on_event(self, event: VkBotEvent):
        if event.type == VkBotEventType.MESSAGE_NEW:
            print(event.type)
            print(event)
            peer_id = event.message.peer_id
            random_id = random.randint(0, 2 ** 20)
            text_message = str(event.message.text)
            self.api.messages.send(peer_id=peer_id, message=text_message, random_id=random_id)

        if event.type == VkBotEventType.WALL_POST_NEW:
            print(event.type)
            print(event)
            print(event.message)


if __name__ == '__main__':
    bot = Bot(group_id, token)
    bot.run()
