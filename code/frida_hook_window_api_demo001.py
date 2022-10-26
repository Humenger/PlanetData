# coding=utf-8
import frida
import sys


def on_message(message, data):
    type = message["type"]
    msg = message
    if type == "send":
        msg = message["payload"]
    elif type == 'error':
        msg = message['stack']
    else:
        msg = message
    print(msg)

#输出frida版本
print('frida version:'+frida.__version__)
# 获取设备
device = frida.get_local_device()
# 注入进程
process=device.attach("powershell.exe")
# 创建脚本
js = open("frida_hook_window_api_demo001.js").read()
script = process.create_script(js)
# 绑定函数
script.on('message', on_message)
# 加载脚本
script.load()
print("FridaDebugTool running....")
# 执行脚本
sys.stdin.read()









