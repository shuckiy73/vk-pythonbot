import datetime
import time
import logging
import VKbot
import config
import vk_api
import threading

VKbot.log(False, "Script started")

def bots():
    VKbot.log(False, "Started listening longpull server")
    VKbot.debug_array['start_time'] = time.time()
    for event in VKbot.MyVkLongPoll.listen(VKbot.longpoll):
        try:
            if event.type == VKbot.VkBotEventType.MESSAGE_NEW:
                log_msg = 
                f'[MESSAGE] #{event.message.conversation_message_id}
                  in peer {event.message.peer_id}, by id{event.message.from_id}'
                if event.message.action:
                    log_msg += (
                        ', action: '
                        + event.message.action["type"]
                        + ', user id in action: '
                        + str(event.message.action["member_id"])
                    )

                if event.message.text != "":
                    log_msg += f', text: "{event.message.text}"'
                if event.message.attachments:
                    atch = ', attachments: '
                    for i in event.message.attachments:
                        if i['type'] == "sticker":
                            atch += f"sticker_id{i[i['type']]['sticker_id']}"
                        elif i['type'] == "wall":
                            atch += i['type'] + str(i[i['type']]['from_id']) + \
                                "_" + str(i[i['type']]['id']) + " "
                        elif i['type'] == "link":
                            atch +=  i['type'] + " " + i[i['type']]['title'] + " "
                        else:
                            atch += i['type'] + str(i[i['type']]['owner_id']) + \
                                "_" + str(i[i['type']]['id']) + " "
                    log_msg += atch
                VKbot.log(False, log_msg)
                VKbot.debug_array['messages_get'] += 1
                if event.message.peer_id not in VKbot.bot:
                    u = VKbot.db.get_all_users()
                    if str(event.message.peer_id) not in u:
                        VKbot.bot[user_id] = VKbot.VkBot(event.message.peer_id) # type: ignore
                    else:
                        i = VKbot.db.get_from_users(event.message.peer_id)
                        VKbot.bot[event.message.peer_id] = VKbot.VkBot(event.message.peer_id)
                VKbot.bot[event.message.peer_id].get_message(event)
            elif event.type == VKbot.VkBotEventType.WALL_POST_NEW:
                if event.object.post_type == "post":
                    VKbot.log(False, f"[NEW_POST] id{event.object.id}")
                    users = VKbot.db.get_all_users()
                    for i in users:
                        VKbot.bot[int(i)].event("post", event.object)
                else:
                    VKbot.log(False, f"[NEW_OFFER] id{event.object.id}")
            elif event.type == VKbot.VkBotEventType.MESSAGE_DENY:
                VKbot.log(False,
                    f"User {event.object.user_id} deny messages from that group")
                del VKbot.bot[int(event.object.user_id)]
                VKbot.db.delete_user(event.object.user_id)
            else:
                VKbot.log(False, f"Event {str(event.type)} happend")
        except Exception as kek:
            VKbot.log(True, f"Беды с ботом: {str(kek)}")
            VKbot.debug_array['bot_warnings'] += 1
            continue


def midnight():
    while True:
        current_time = time.time()+10800
        if int(current_time) % 86400 == 0:
            VKbot.log(False, "[EVENT_STARTED] \"Midnight\"")
            users = VKbot.db.get_all_users()
            for i in users:
                VKbot.bot[int(i)].event("midnight")
            VKbot.log(False, "[EVENT_ENDED] \"Midnight\"")
            time.sleep(1)
        else:
            time.sleep(0.50)


VKbot.SPAMMER_LIST = VKbot.db.read_spammers()
tread_bots = threading.Thread(target=bots)
tread_midnight = threading.Thread(target=midnight, daemon=True)
tread_bots.start()
tread_midnight.start()
