import platform
from ctypes import *

def get_encrypt_value(data):
    system = platform.system()
    cpu = platform.architecture()[0]
    if syetem == "Darwin" and cpu == "64bit":
        cur = cdll.LoadLibrary("./bestV8_mac_intel.dylib")
    elif syetem == "Darwin" and cpu == "arm64":
        cur = cdll.LoadLibrary("./bestV8_mac_m.dylib")
    elif system == "Linux":
        cur = cdll.LoadLibrary("./bestV8_x64.so")
    elif system == "Windows":
        cur = cdll.LoadLibrary("./bestV8_win64.dll")
    else:
        raise Exception("unknown system or cpu!")

    result = bytes(20000)
    cur.runJs.argtypes = (c_char_p, c_char_p)
    for x in range(1):
        cur.runJs(create_string_buffer(data.encode('utf8')), result)
        print(result.rstrip(b"\x00"))

data = open("demo.js","r").read()
get_encrypt_value(data)

