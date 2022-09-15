### 1.安装pyinstaller
pip install pyinstaller

### 2.打包
打开cmd，切换到需要打包的文件(demo.py)目录.执行
pyinstaller -F -w demo.py
生成的exe文件就在子目录dist中。-F表示指定打包后只生成一个exe格式的文件，-w表示窗口，无控制台。

### 3.修改exe图标
-i icon.ico 或者 --icon=icon.ico
图标文件放在要打包的文件同目录中。