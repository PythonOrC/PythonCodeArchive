'''
import os

os.chdir(r"C:\Pyblock\resources\app\Python-win32")
# print(os.system("python.exe -m pip uninstall pillow"))
print(os.system("python.exe -m pip install pillow==5.4.0"))
print('安装pillow库成功')

# os.chdir(r"C:\Pyblock\resources\app\Python-win32")
# print(os.system("python.exe -m pip uninstall lml"))
# print(os.system("python.exe -m pip install lml==0.0.2"))
# print('安装lml库成功')
'''
import PIL
print(PIL.__version__)