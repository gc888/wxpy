#!/usr/bin/env python3
# coding: utf-8

"""


登陆微信::

    # 导入模块
    from wxpy import *
    # 初始化机器人，扫码登陆
    bot = Bot()

找到好友::

    # 搜索名称含有 "游否" 的男性深圳好友
    my_friend = bot.friends().search('游否', sex=MALE, city="深圳")[0]

发送消息::

    # 发送文本给好友
    my_friend.send('Hello WeChat!')
    # 发送图片
    my_friend.send_image('my_picture.jpg')

自动响应各类消息::

    # 打印来自其他好友、群聊和公众号的消息
    @bot.register()
    def print_others(msg):
       print(msg)

    # 回复 `my_friend` 的消息 (优先匹配后注册的函数!)
    @bot.register(my_friend)
    def reply_my_friend(msg):
       return 'received: {} ({})'.format(msg.text, msg.type)

    # 开始监听和自动处理消息
    bot.start()


"""
import sys

from .bot import Bot
from .chats import Chat, Chats, Friend, Group, Groups, MP, Member, User
from .chats import FEMALE, MALE
from .exceptions import ResponseError
from .ext import Tuling
from .messages import ATTACHMENT, CARD, FRIENDS, MAP, NOTE, PICTURE, RECORDING, SHARING, SYSTEM, TEXT, VIDEO
from .messages import Message, Messages
from .utils import dont_raise_response_error, embed, ensure_one, mutual_friends

# 从 v0.2.0 版本起，Robot 改名为 Bot，因此使用别名方式兼容现有的用户代码
Robot = Bot

__title__ = 'wxpy'
__version__ = '0.2.0.mo3.1'
__author__ = 'Youfou'
__license__ = 'MIT'
__copyright__ = '2017, Youfou'

version_details = 'wxpy {ver} from {path} (python {pv.major}.{pv.minor}.{pv.micro})'.format(
    ver=__version__, path=__path__[0], pv=sys.version_info)
