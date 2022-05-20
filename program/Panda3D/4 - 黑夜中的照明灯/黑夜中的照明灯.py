# 直接启动，创建全局ShowBase实例
import direct.directbase.DirectStart
# 导入窗体属性功能模块
from panda3d.core import *

state = {'lamp':False}
# 创建窗体属性
window = WindowProperties()
# 设置窗体标题
window.setTitle('lamp')
# 设置窗体大小
window.setSize(1200, 800)
# 将属性传递给主窗体
base.win.requestProperties(window)
# 设置窗体的背景颜色
base.setBackgroundColor(100/255, 150/255, 180/255)

# 加载场景模型
scene = loader.loadModel('scene')
# 添加场景模型至渲染列表
scene.reparentTo(render)
# 加载房子模型
house = loader.loadModel('house')
# 添加房子模型至渲染列表
house.reparentTo(render)
# 设置房子位置
house.setPos(-650, 1100, 0)
# 设置房子旋转
house.setHpr(45, 0, 0)

# 设置相机位置
base.cam.setPos(0, -8000, 5000)
# 设置相机角度
base.cam.setHpr(0, -30, 0)
# 禁用鼠标
base.disableMouse()

# 加载太阳
sun = loader.loadModel('sun')
sun.setScale(200)
sun.setPos(0, -1600, 3000)
# 设置太阳颜色
sun.setColor((255/255, 255/255, 100/255, 1))

# 创建定向光源
directional_light = DirectionalLight('sun')
# 添加光源
sun_light = sun.attachNewNode(directional_light)
# 设置光源
scene.setLight(sun_light)
# 显示光源示意辅助线
# directional_light.show_frustum()
# 设置光源角度
sun_light.setHpr(-90, -45, 0)
house.setLight(sun_light)
# 设置光源颜色
directional_light.setColor((255/255, 255/255, 100/255, 1))

# 太阳旋转
sun_node = render.attachNewNode('change')
sun.reparentTo(sun_node)
sun_node.hprInterval(40, (0, 0, 360)).loop()

# 设置启动阴影效果
directional_light.setShadowCaster(True)
# 显示阴影效果
scene.setShaderAuto()
# 设置胶片尺寸
directional_light.getLens().setFilmSize(50, 60)
house.setShaderAuto()

lamp = loader.loadModel('lamp')
lamp.reparentTo(render)

lamp.setPos(-700,500,0)
lamp.setHpr(-90,0,0)

point_light = PointLight('lamp')
lamp_light = lamp.attachNewNode(point_light)

scene.setLight(lamp_light)
lamp_light.setPos(0,150,400)
house.setLight(lamp_light)
lamp.setLight(lamp_light)
lamp.setLight(sun_light)
# 运行主程序

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
base.run()
