import direct.directbase.DirectStart
from panda3d.core import *
from direct.actor.Actor import Actor

window = WindowProperties()
window.setTitle('Celebration')
window.setSize(1200, 800)
base.win.requestProperties(window)

stage = loader.loadModel('stage')
stage.reparentTo(render)

base.cam.setPos(0, -2000, 600)
base.cam.setHpr(0, -12, 0)


def spotlight(color, size, pos, Hpr):
    spotlight = Spotlight('light')
    spotlight.setColor(color)
    lens = PerspectiveLens()
    lens.setFov(size)
    spot_light = render.attachNewNode(spotlight)
    render.setLight(spot_light)
    spot_light.setPos(pos[0], pos[1], pos[2])
    spot_light.setHpr(Hpr[0], Hpr[1], Hpr[2])
    return spot_light


spotlight_1 = spotlight((50/255, 200/255, 180/255, 1),
                        20, (400, -420, 400), (10, -30, 0))
spotlight_2 = spotlight((255/255, 50/255, 190/255, 1),
                        20, (200, -420, 400), (10, -30, 0))
spotlight_3 = spotlight((150/255, 200/255, 130/255, 1),
                        20, (-200, -420, 400), (-10, -30, 0))
spotlight_4 = spotlight((160/255, 190/255, 180/255, 1),
                        20, (-400, -420, 400), (-10, -30, 0))

spotlight_1.hprInterval(1.3, (30, -10, 0)).loop()
spotlight_2.hprInterval(1.2, (-30, -20, 0)).loop()
spotlight_3.hprInterval(1.5, (40, -40, 0)).loop()
spotlight_4.hprInterval(1.1, (-40, -20, 0)).loop()

light = AmbientLight('lightNode')
light.setColor((0.3,0.3,0.3,1))
Ambient_light = render.attachNewNode(light)
render.setLight(Ambient_light)

codemao = Actor('codemao', {'d1': 'codemao_dance1', 'd2': 'codemao_dance2'})
codemao.reparentTo(render)
codemao.setPos(0,0,100)
codemao.loop('d2')
line = NodePath('codemao_line')
for i in range(-300, 310, 200):
    line_node = line.attachNewNode('codemao')
    codemao.instanceTo(line_node)
    line_node.setPos(i,150,0)
line.reparentTo(render)
music = loader.loadSfx('music.mp3')
music.setLoop(True)
music.play()

def play_music(task):
    d1_control = codemao.getAnimControl('d1')
    d2_control = codemao.getAnimControl('d2')
    if music.getTime() < 13 and not d1_control.isPlaying():
        codemao.loop('d1')
    elif music.getTime() >= 13 and not d2_control.isPlaying():
        codemao.loop('d2')
    return task.cont
taskMgr.add(play_music)

base.run()
