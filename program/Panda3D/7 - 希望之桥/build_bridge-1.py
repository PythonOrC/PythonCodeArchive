#导入功能模块
import direct.directbase.DirectStart
from panda3d.core import *
from direct.actor.Actor import Actor
#设置窗体属性
window = WindowProperties()
window.setTitle("bridge")
window.setSize(1200, 800)
base.win.requestProperties(window)
base.setBackgroundColor(100/255, 150/255, 180/255)
#设置镜头参数
base.cam.setPos(-5800, -3750, 3300)
base.cam.setHpr(0, -46, 0)
#禁用鼠标控制
base.disableMouse()
#自定义加载模型函数


def load_model(path, pos, hpr):
    model = loader.loadModel(path)
    model.reparentTo(render)
    model.setPos(pos[0], pos[1], pos[2])
    model.setHpr(hpr[0], hpr[1], hpr[2])
    return model


#加载场景模型
scene = load_model("scene", (0, 0, 0), (0, 0, 0))
house = load_model("house", (-650, 1500, 0), (45, 0, 0))
lamp = load_model("lamp", (-800, 800, 0), (-90, 0, 0))
#加载太阳能汽车模型
car = Actor("car", {"run": "car_run"})
car.reparentTo(render)
car.setHpr(-90, 0, 0)
car.setPos(-4150, -450, 0)
#定义任务函数


def move(task):
    moving = False
    if car_state["forward"]:
        car.setY(car, -10)
        moving = True
    if car_state["turn_left"]:
        car.setH(car, 2)
    if car_state["turn_right"]:
        car.setH(car, -2)
    if moving:
        control = car.getAnimControl("run")
        if not control.isPlaying():
            car.loop("run")
    else:
        car.stop()
    return task.cont


taskMgr.add(move)

# 太阳能汽车的移动状态
car_state = {"forward": False, "turn_left": False, "turn_right": False}

#定义太阳能汽车控制事件函数


def change_car_state(direction, temp_state):
    car_state[direction] = temp_state


#定义键盘事件
base.accept("w", change_car_state, ["forward", True])
base.accept("w-up", change_car_state, ["forward", False])
base.accept("a", change_car_state, ["turn_left", True])
base.accept("a-up", change_car_state, ["turn_left", False])
base.accept("d", change_car_state, ["turn_right", True])
base.accept("d-up", change_car_state, ["turn_right", False])

cliff = loader.loadModel('cliff')
cliff.reparentTo(render)
bridge = loader.loadModel('bridge')
bridge.reparentTo(render)

capsule_down = CollisionCapsule(-6900,-680,0,-5100,-680,0,20)
collision_down_node = CollisionNode('bridge')
collision_down_node.addSolid(capsule_down)
capsule_down_collision = render.attachNewNode(collision_down_node)
capsule_down_collision.show()

capsule_up = CollisionCapsule(-6900, -160, 0, -5100, -160, 0, 20)
collision_up_node = CollisionNode('bridge')
collision_up_node.addSolid(capsule_up)
capsule_up_collision = render.attachNewNode(collision_up_node)
capsule_up_collision.show()

sphere_left = CollisionSphere(90,-125,30,30)
sphere_left_node = CollisionNode('car')
sphere_left_node.addSolid(sphere_left)
sphere_left_collision = car.attachNewNode(sphere_left_node)
sphere_left_collision.show()

sphere_right = CollisionSphere(-90, -125, 30, 30)
sphere_right_node = CollisionNode('car')
sphere_right_node.addSolid(sphere_right)
sphere_right_collision = car.attachNewNode(sphere_right_node)
sphere_right_collision.show()

pusher = CollisionHandlerPusher()
pusher.addCollider(sphere_left_collision, car)
base.cTrav = CollisionTraverser()
base.cTrav.addCollider(sphere_left_collision, pusher)
pusher.addCollider(sphere_right_collision, car)
base.cTrav.addCollider(sphere_right_collision, pusher)
pusher.setHorizontal(True)

#运行主函数
base.run()
