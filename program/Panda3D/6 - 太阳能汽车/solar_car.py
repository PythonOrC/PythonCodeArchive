import direct.directbase.DirectStart
from panda3d.core import *
# 导入任务功能模块
from direct.task import Task
from direct.actor.Actor import Actor

# 窗体创建及显示设置
window = WindowProperties()
window.setTitle("car")
window.setSize(1200, 800)
base.win.requestProperties(window)
base.setBackgroundColor(100/255, 150/255, 180/255)
# 设置相机位置及角度
base.cam.setPos(450, -5850, 2000)
base.cam.setHpr(0, -16, 0)
# 禁用鼠标
base.disableMouse()


def load_model(path, pos, hpr):
    model = loader.loadModel(path)
    model.reparentTo(render)
    model.setPos(pos[0], pos[1], pos[2])
    model.setHpr(hpr[0], hpr[1], hpr[2])
    return model


# 场景环境及房子
scene = load_model("scene", (0, 0, 0), (0, 0, 0))
house = load_model('house', (-650, 1500, 0), (45, 0, 0))
# 太阳
sun = load_model("sun", (2500, 1000, 1500), (0, 0, 0))
sun.setColor((255/255, 255/255, 100/255, 1))
sun.setScale(100)

# 照明灯
lamp = load_model("lamp", (-800, 800, 0), (-90, 0, 0))

# 加载架子及太阳能电池板
shelf = load_model("shelf", (-1800, -900, 0), (90, 0, 0))
solar_panel = load_model("solar_panel", (-1800, -900, 120), (90, 60, 0))


car = Actor('car', {'run': 'car_run'})
car.reparentTo(render)
car.setPos(340, -2300, 0)
car.setHpr(90, 0, 0)
car.loop('run')
def move(task):
    moving = False
    if car_state['forward']:
        car.setY(car, -5)
        moving = True
    if car_state['left']:
        car.setH(car,2)
    if moving:
        control = car.getAnimControl('run')
        if not control.isPlaying():
            car.loop('run')
    else:
        car.stop()
    return task.cont

taskMgr.add(move)

car_state = {'forward':False,'left':False}

def change_car_state(direction,temp_state):
    car_state[direction] = temp_state

base.accept('w',change_car_state,['forward',True])
base.accept('w-up', change_car_state, ['forward', False])
base.accept('a', change_car_state, ['left', True])
base.accept('a-up', change_car_state, ['left', False])
base.run()
