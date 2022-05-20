from panda3d.core import *
from direct.showbase.ShowBase import ShowBase
ShowBase()

window = WindowProperties()
window.setTitle('New Galaxy')
window.setSize(1600,1000)
base.win.requestProperties(window)

virtual_planet_2 = render.attachNewNode('planet_2')
virtual_planet_3 = render.attachNewNode('planet_3')
virtual_planet_4 = render.attachNewNode('planet_4')
virtual_planet_5 = render.attachNewNode('planet_5')

space = loader.loadModel('space_sky')
space.reparentTo(render)
planet_1 = loader.loadModel('planet1')
planet_1.reparentTo(render)
planet_2 = loader.loadModel('planet2')
planet_2.reparentTo(virtual_planet_2)
planet_2.setPos(600, 0, 0)
planet_3 = loader.loadModel('planet3')
planet_3.reparentTo(virtual_planet_3)
planet_3.setPos(-900, 0, 0)
planet_4 = loader.loadModel('planet4')
planet_4.reparentTo(virtual_planet_4)
planet_4.setPos(1200, 0, 0)
planet_5 = loader.loadModel('planet5')
planet_5.reparentTo(virtual_planet_5)
planet_5.setPos(1600, 0, 0)
virtual_planet_6 = planet_4.attachNewNode('planet_6')
planet_6 = loader.loadModel('planet6')
planet_6.reparentTo(virtual_planet_6)
planet_6.setPos(200, 150, 0)


planet_1.hprInterval(8,(360,0,0)).loop()
planet_2.hprInterval(7, (360, 0, 0)).loop()
planet_3.hprInterval(6, (360, 0, 0)).loop()
planet_4.hprInterval(5,(360,0,0)).loop()
planet_5.hprInterval(4, (360, 0, 0)).loop()
planet_6.hprInterval(5, (360, 0, 0)).loop()
virtual_planet_2.hprInterval(7,(360,0,0)).loop()
virtual_planet_3.hprInterval(6, (360, 0, 0)).loop()
virtual_planet_4.hprInterval(5, (360, 0, 0)).loop()
virtual_planet_5.hprInterval(4, (360, 0, 0)).loop()
virtual_planet_6.hprInterval(5, (360, 0, 0)).loop()
base.run()
