from time import sleep

from pywinauto import Application
from pywinauto.keyboard import send_keys

# 连接到进程
app=Application(backend="uia").connect(process=38528)
# 定位窗口
win=app.window(title="啊喵(2360)")
win.wait("visible")
# win.print_control_identifiers()

# 输入信息
# win.type_keys("哎{ENTER}我在呢，宝宝{ENTER}")
# sleep(1)
# win.type_keys("给你看我新写的东西{ENTER}")
# win.type_keys("嗷嗷{ENTER}没事我测试一下我写的代码{ENTER}")

# send_keys("嘻嘻")

# 唤起对话框
for i in range(0,5):
    win.type_keys("你爸在家没{ENTER}",with_spaces=True)


