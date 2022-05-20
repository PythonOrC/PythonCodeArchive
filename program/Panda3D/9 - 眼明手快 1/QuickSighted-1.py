#导入直接启动、窗体属性设置模块
import direct.directbase.DirectStart
from panda3d.core import *
from direct.interval.IntervalGlobal import *
from direct.task import Task
import random
#创建窗体属性容器，并修改标题、尺寸等属性
window = WindowProperties()
window.setTitle("Agility Training")
window.setSize(1200, 800)
#将属性传递给主窗体
base.win.requestProperties(window)
#加载并显示场景模型文件
scene = loader.loadModel("woodland")
scene.reparentTo(render)
#设置镜头位置及角度
base.cam.setPos(0, -1200, 1200)
base.cam.setHpr(0, -45, 0)
base.disableMouse()
#设置窗体背景色
base.setBackgroundColor(0/255, 128/255, 255/255)

alien = []
alien_sequence = []
def load_alien(model_name):
    model = loader.loadModel(model_name)
    model.reparentTo(render)
    model.setTransparency(True)
    hide = model.colorInterval(5, (1, 1, 1, 0), (1, 1, 1, 1))
    appear = model.colorInterval(5, (1, 1, 1, 1), (1, 1, 1, 0))
    color_sequence = Sequence(appear, Wait(3), hide)
    alien_sequence.append(color_sequence)
    alien.append(model)

load_alien('alien_1')
load_alien('alien_2')
load_alien('alien_3')
alien[0].setPos(-100,0,0)
alien[1].setPos(100,0,0)

def move_task(task):
    for i in range(0,3):
        if alien_sequence[i].isStopped():
            alien[i].setPos(random.randint(-320,320), random.randint(-240,240),0)
            alien_sequence[i].start()
    return task.cont

taskMgr.add(move_task)
#运行主程序
base.run()
