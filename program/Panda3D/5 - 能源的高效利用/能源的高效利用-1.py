# 导入功能模块
import direct.directbase.DirectStart
from panda3d.core import *
from  direct.task import Task
# 窗体创建及显示设置
window = WindowProperties()
window.setTitle("Energy_saving")
window.setSize(1200, 800)
base.win.requestProperties(window)
base.setBackgroundColor(100/255, 150/255, 180/255)
# 设置相机位置及角度
base.cam.setPos(0, -8000, 5000)
base.cam.setHpr(0, -30, 0)
# 禁用鼠标
base.disableMouse()
# 加载模型函数


def load_model(path, pos, hpr):
    model = loader.loadModel(path)
    model.reparentTo(render)
    model.setPos(pos[0], pos[1], pos[2])
    model.setHpr(hpr[0], hpr[1], hpr[2])
    return model


# 场景环境及房子
scene = load_model("scene", (0, 0, 0), (0, 0, 0))
house = load_model('house', (-650, 1500, 0), (45, 0, 0))
# 太阳及太阳光
sun_light_node = render.attachNewNode("change")
sun = loader.loadModel("sun")
sun.setColor((255/255, 255/255, 100/255, 1))
sun.setScale(200)
sun.setPos(-3000, -1600, 0)
sun.reparentTo(sun_light_node)
sun_light = sun.attachNewNode(DirectionalLight("SUN"))
sun_light.setHpr(-90, 0, 0)
sun_light.node().setColor((255/255, 255/255, 100/255, 1))
sun_light.setPos(1, 0, 0)
sun_light.node().setShadowCaster(True, 2024, 2024)
sun_light.node().getLens().setFilmSize(60, 80)
sun_light_node.hprInterval(40, (0, 0, 360)).loop()
render.setShaderAuto(True)
house.setLight(sun_light)
scene.setLight(sun_light)
# 照明灯设置
lamp = load_model("lamp", (-800, 800, 0), (-90, 0, 0))
lamp_light = lamp.attachNewNode(PointLight("lamp"))
lamp_light.setPos(0, 150, 400)
lamp_light.node().setColor((1, 1, 1, 1))
lamp_light.node().setShadowCaster(True, 2024, 2024)
lamp.setLight(sun_light)
# 定义按键开关事件
state = {"lamp": True}


def change_state(name):
    if state[name]:
        print('Turn On')
        house.setLight(lamp_light)
        scene.setLight(lamp_light)
        lamp.setLight(lamp_light)
        state[name] = False
    else:
        print('Turn Off')
        house.setLightOff(lamp_light)
        scene.setLightOff(lamp_light)
        lamp.setLightOff(lamp_light)
        state[name] = True


base.accept('l', change_state, ['lamp'])
# 照明灯的自动控制
def auto_light(task):
    if (sun_light_node.getR() > 9.95 and sun_light_node.getR() < 10.09) or (sun_light_node.getR() > 169.95 and sun_light_node.getR() < 170.05):
        change_state('lamp')

    return task.cont

taskMgr.add(auto_light)

shelf = load_model('shelf',(-1800,-900,0),(90,0,0))
solar_panel = load_model('solar_panel', (-1800, -900, 100), (90, -90, 0))
solar_panel.hprInterval(40,(90,270,0)).loop()
shelf.setLight(sun_light)
solar_panel.setLight(sun_light)
shelf.setLight(lamp_light)
solar_panel.setLight(lamp_light)
base.run()
