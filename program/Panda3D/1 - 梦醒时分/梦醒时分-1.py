from panda3d.core import *
from direct.showbase.ShowBase import ShowBase
ShowBase()

window = WindowProperties()
window.setTitle('Fly To the Universe')
window.setSize(1200,900)
base.win.requestProperties(window)
base.setBackgroundColor(0,128/255,1)

schoolKey = loader.loadModel('school')

schoolKey.reparentTo(render)

spaceKey = loader.loadModel('space')
spaceKey.reparentTo(render)
spaceKey.setScale(0.7)
spaceKey.setPos(0,-500,0)
base.run()
