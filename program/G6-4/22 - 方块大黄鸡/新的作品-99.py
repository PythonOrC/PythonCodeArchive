from vpython import *

body = box(size=vec(665, 498, 665),color=color.yellow)
face = box(pos=vec(0, 0, 665 / 2), size=vec(665, 498, 0.1), texture="face.png")
tape = box(size=vec(700,120,700), pos=vec(0,120/2+498/2,0),color = vec(155/255,101/255,85/255))
cockpit = box(size=vec(665, 80, 665), pos=vec(0, 120/2+498/2+120/2+80/2,0),color =vec(193/255,183/255,183/255))
eyeglass_left = box(size=vec(273,169,20), texture = {"file":'glass.png',"bumpmap":"glass_bumpmap.png"},pos = vec(-150,60+498/2,700/2+10))
eyeglass_right = eyeglass_left.clone(pos=vec(150, 60+498/2, 700/2+10))
wing_left = box(size=vec(300,150,500), pos = vec(0-665/2-300/2,0,0),color=color.yellow)
wing_right = wing_left.clone(pos=vec(665/2+300/2, 0, 0))
