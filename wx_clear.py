#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/3/18 13:24
# @Author  : qizai
# @File    : wx_clear.py
# @Software: PyCharm

from wxpy import *
import time
import random

bot = Bot(console_qr=1)  # Linux环境console_qr=2  windows环境console_qr=1
all_friends = bot.friends()
myself = bot.self
print('----------------BEGIN----------------')
print("检测到你联系人共计: " + str(len(all_friends)) + " 人")
myself.send("检测到你联系人共计: " + str(len(all_friends)) + " 人")
myself.send("下面开始逐个测试，大概500个好友要半个钟，依次类推，请耐心等候...")

index = 1
for user in all_friends:
    time.sleep(random.randint(0, 9))
    try:
        if user != myself:
            print("["+str(index)+"/"+str(len(all_friends))+"] " + user.name)
            user.send('能看到我发的吗 జ్ఞా ')
    except ResponseError as e:
        print("异常", e.err_code, e.err_msg)
        myself.send("*好友：%s. 01出现异常:" % user.name, e.err_code, e.err_msg)
    except Exception as e:
        print("异常", e)
        myself.send("#好友：%s. 02出现异常:" % user.name, e)
    index += 1

print("检测已执行完毕请到手机微信app中处理")
print('----------------END----------------')
myself.send("检测已执行完毕请到手机微信app中处理")


