from websocket_server import WebsocketServer
import json as JSON
import requests
import bot
from random import randint

class CoinGame(object):
    def __init__(self,server,client):
        self.status=0
        self.map=[[0,0,0],[0,0,0],[0,0,0]]
        self.players={}
        self.choices=0
        self.server=server
        self.client=client

    def addPlayer(self,id,name):
        if not id in self.players:
            self.players[id]={
                "name": name,
                "select": None,
                "score": 0
                "position": None}

    def setPosition(self):
        # 随机打乱顺序
        pos=[[1,0],[0,1],[1,2],[2,1]]
        for i in range(4):
            m=randint(0,3)
            n=randint(0,3)
            [pos[m],pos[n]]=[pos[n],pos[m]]
        # 位置保存到玩家数据和地图里
        i=0
        for id,data in self.players:
            data.position=pos[i]
            self.map[pos[0]][pos[1]]=id
            i+=1

    def checkDirection(self,player,dir):
        if (dir=="W" or dir=="w") and player.position[0]==0:
            return False
        if (dir=="S" or dir=="s") and player.position[0]==2:
            return False
        if (dir=="A" or dir=="a") and player.position[1]==0:
            return False
        if (dir=="D" or dir=="d") and player.position[1]==2:
            return False
        return True

    def move(self):
        for player in self.players:

    def parseMessage(self,msg):
        if self.status==0:
            if msg["message"]=="查看":
                pass
        elif self.status==1:
            if msg["message"]=="加入":
                self.addPlayer(id,name)
                if len(self.players)==4:
                    self.status=2
        elif self.status==2:
            # 如果发消息的是玩家
            if :
                # 处理非法的移动方向
                if re.match("[WASDwasd]",msg["message"]) and self.checkDirection():
                    self.players[id]=msg["message"]
                    self.choices+=1
                    # 如果所有玩家都做出了选择 计算得分
                    if self.choices==4:
                        self.move()
                else:
                    bot.sendGroupMessage(server,client)

def message_received(client, server, message):
    data=JSON.loads(message.encode("iso-8859-1").decode())
    print(data)
    if "retcode" in data:
        print("消息发送成功")
        return
    # 如果收到了私聊消息
    if data["message_type"]=="private":
        # sendPrivateMessage(server, client, data["sender"]["user_id"], data["message"])
        pass
    elif data["message_type"]=="group":
        # sendGroupMessage(server, client, data["group_id"], msg)
        pass

server = WebsocketServer(1149, host='127.0.0.1')
server.set_fn_message_received(message_received)
server.run_forever()
