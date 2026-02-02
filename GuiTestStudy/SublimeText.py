# 寻找到 Clear Items
import time

from pywinauto import Application, mouse

# 连接 sublime Text 进程
app=Application(backend="uia").connect(process=38680)
# 定位窗口
win=app.window(title_re=".*Sublime Text.*")
# win.wait("visible") 这个表示当前窗口必须可见
win.wait("exists")
# win.print_control_identifiers()

# 定位到应用程序窗口了
menu=win['应用程序']
# print(menu.children())
# print(menu.items())

# 会定位但是不会点击
file_menu=menu.child_window(title="File", control_type="MenuItem")
time.sleep(1)
# 会定位点击到相应的控件--调起到open recent窗口
menu_item1=menu.item_by_path("File->Open Recent").click_input()
time.sleep(1)
# 定位Open Recent窗口
new_menu=win.child_window(title="Open Recent", control_type="Menu")
# new_menu.wait("visible")
new_menu.item_by_path("Clear Items").click_input()
# menu_item1.item_by_path("Clear Items")
time.sleep(1)
# # file_menu.print_control_identifiers()
# win.print_control_identifiers()


# openRecent_win = file_menu.child_window(title="Open Recent",control_type="Window")


# openRecent_win.wait("exists")
# #定位Open Recent窗⼝Clear Items菜单项
# openRecent_menu = openRecent_win.child_window(title="Open Recent",control_type="Menu")
# time.sleep(3)
# print(item1)
# item1_point=item1.rectangle().mid_point()
# mouse.click(coords=(item1_point.x,item1_point.y))
# time.sleep(3)
