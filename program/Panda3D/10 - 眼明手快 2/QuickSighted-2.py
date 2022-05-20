#导入直接启动、窗体属性设置模块
import direct.directbase.DirectStart
from panda3d.core import *
from direct.interval.IntervalGlobal import *
from direct.task import Task
import random
from TransformModel import model_position
from TextDisplay import *
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
#定义外星人存放列表
alien = []
alien_sequence = []
#定义加载游戏角色函数
def load_alien(model_name):
    model = loader.loadModel(model_name)
    model.reparentTo(render)
    model.setTransparency(True)
    #设置外星人逐渐隐身的效果
    hide = model.colorInterval(1, (1, 1, 1, 0), (1, 1, 1, 1))
    appear = model.colorInterval(0.5, (1, 1, 1, 1), (1, 1, 1, 0))
    #创建序列
    color_sequence = Sequence(appear, Wait(3),hide)
    alien_sequence.append(color_sequence)
    sphere = CollisionSphere(0,0,110,30)
    sphere_node = CollisionNode('alien')
    sphere_node.addSolid(sphere)
    model_collision = model.attachNewNode(sphere_node)
    alien.append(model)
#加载外星人
load_alien("alien_1")
load_alien("alien_2")
load_alien("alien_3")

hammer = loader.loadModel('hammer')
hammer.reparentTo(render)
sphere = CollisionSphere(-40, 0, 125, 25)
sphere_node = CollisionNode('hammer')
sphere_node.addSolid(sphere)
hammer_collision = hammer.attachNewNode(sphere_node)

base.cTrav = CollisionTraverser()
queue_handler = CollisionHandlerQueue()
base.cTrav.addCollider(hammer_collision, queue_handler)

score = 0
delay = 1
#定义移动任务函数
def move_task(task): 
    global score, delay
    delay-=0.01
    for i in range(0,3):   
        if alien_sequence[i].isStopped():              
            alien[i].setPos(random.randint(-320,320),random.randint(-240,240),0)
            alien_sequence[i][1] = Wait(random.uniform(0.5,3))
            alien_sequence[i].start()
    model_position(hammer)
    display('Score: '+str(score))
    if queue_handler.getNumEntries() > 0:
        queue_handler.sortEntries()
        if queue_handler.getEntry(0).getIntoNode().getName() == 'alien' and delay <=0:
            score += 1
            delay = 1
            
            queue_handler.getEntry(0).getIntoNodePath().getParent().setColor((1,1,1,0))
            queue_handler.getEntry(0).getIntoNodePath().getParent().setPos(-320,240,0)
            print(score)
    return task.cont
#将任务函数添加到任务管理器中
taskMgr.add(move_task)

def knock(left_button):
    status = left_button
    if status:
        hammer.setR(-60)
    else:
        hammer.setR(0)
base.accept('mouse1',knock,[True])
base.accept('mouse1-up', knock, [False])

#运行主程序
base.run()
