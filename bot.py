import json as JSON
import re

# 发送私聊消息
def sendPrivateMessage(server, client, user_id, message):
    msg=JSON.dumps({
        "action": "send_private_msg",
        "params": {
            "user_id": user_id,
            "message": message
        }
    })
    server.send_message(client, msg)

# 发送群消息
def sendGroupMessage(server, client, group_id, message):
    msg=JSON.dumps({
        "action": "send_group_msg",
        "params": {
            "group_id": group_id,
            "message": message
        }
    })
    server.send_message(client, msg)
