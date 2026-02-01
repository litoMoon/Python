from pywinauto import Application

# 通过进程号连接到当前这个软件
app=Application(backend="uia").connect(process=10296)
# 定位到窗口
# 方法一：best_match
# 方法二：通过title 使用正则表达式 进行定位
win=app.window(title_re=".*Sublime Text.*")
win.wait("exists")

