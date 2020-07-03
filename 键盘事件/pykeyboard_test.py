import pykeyboard
import random
import time

print(pykeyboard.reply_keyboard)
k = PyKeyboard()
b = 0
for num in range(1,100):
    a = random.uniform(1.5,2.5)
    time.sleep(a)
    k.tap_key(13)
    b += 1
    print(a)