# 寻找到 Clear Items
import time

from pywinauto import Application, mouse

# 连接 sublime Text 进程
app=Application(backend="uia").connect(process=10296)
# 定位窗口
win=app.window(title_re=".*Sublime Text.*")
# win.wait("visible") 这个表示当前窗口必须可见
win.wait("exists")
# win.print_control_identifiers()

# 定位到应用程序窗口了
menu=win['应用程序']
# print(menu.children())

item1=menu.item_by_path("File->Open Recent")
# print(item1)
item1_point=item1.rectangle().mid_point()
mouse.move(coords=(item1_point.x,item1_point.y))
time.sleep(3)