import os
import sys
import turtle

install_dict = {'pyecharts': ['pyecharts==0.5.10', 'pyecharts-snapshot==0.1.8'],
                'pyecharts-snapshot': ['pyecharts==0.5.10', 'pyecharts-snapshot==0.1.8'], 'pillow': ['pillow==6.1.0'],
                'matplotlib': ['matplotlib==3.1.2'], 'pyside2': ['PySide2==5.13.0'], 'arcade': ['arcade==2.0.9'],
                'dataclasses': ['dataclasses==0.7'], 'snownlp': ['snownlp==0.12.3'], 'nltk': ['nltk==3.4.5'],
                'echarts-countries-pypkg': ['echarts-countries-pypkg==0.1.6'], 'jieba': ['jieba==0.39'],
                'reportlab': ['reportlab==3.5.23'], 'wordcloud': ['wordcloud==1.5.0'], 'imageio': ['imageio==2.5.0'],
                'pygame': ['pygame==1.9.6'], 'sympy': ['sympy==1.4'], 'vpython': ['vpython==7.5.2'],
                'requests': ['requests==2.18.1'], 'psutil': ['psutil==5.6.7'],
                'opencv-python': ['opencv-python==4.1.2'],
                'beautifulsoup4': ['beautifulsoup4==4.8.1'], 'numpy': ['numpy==1.17.2'], 'pandas': ['pandas==0.25.1'],
                'seaborn': ['seaborn==0.9.0'], 'scikit-learn': ['scikit-learn==0.22'], 'torch': ['torch'],
                'torchvision': ['torchvision']}
# python.exe路径
python_path = os.path.dirname(sys.executable)
print("您当前的python.exe路径为：", python_path)

turtle.setup(width=360, height=300, startx=500, starty=200)
turtle.hideturtle()
turtle.penup()
turtle.goto(-120, 0)

Input = turtle.textinput("安装:", "请输入要安装的库名").lower().strip()
turtle.write("正在安装，请稍等....", True, font=("", 20))
os.chdir(python_path)
result = False

for i in install_dict:
    if Input == i:
        result = True
        for install in install_dict[i]:
            print("开始安装：{}...".format(install))
            os.system(
                "python.exe -m pip install {} -i https://pypi.douban.com/simple ".format(install))
            print("{}安装结束...".format(install))
if not result:
    for i in install_dict:
        if Input in i:
            result = True
            for install in install_dict[i]:
                print("开始安装：{}...".format(install))
                os.system(
                    "python.exe -m pip install {} -i https://pypi.douban.com/simple ".format(install))
                print("{}安装结束...".format(install))

if not result:
    print("开始安装：{}...".format(Input))
    os.system(
        "python.exe -m pip install {} -i https://pypi.douban.com/simple ".format(Input))
    print("{}安装结束...".format(Input))

print("安装结束...")
