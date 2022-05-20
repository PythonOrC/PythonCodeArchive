from vpython import *
scene.background = color.white
head = sphere(pos=vec(0, 0, 0), radius=5, emissive=True)
body = sphere(pos=vec(0, -13, 0), radius=9, emissive=True)
eye_left = sphere(size=vec(0.8, 1, 0.8),
                  pos=vec(-2, 0, 4.5), color=color.black)
eye_right = eye_left.clone(pos=vec(2, 0, 4.5))
nose = cone(pos=vec(0, -1, 0), axis=vec(0, 0, 8),
            radius=1.5, color=vec(243/255, 101/255, 62/255))
earmuff_left = cylinder(pos=vec(-5, 0, 0), axis=vec(-1,
                        0, 0), radius=2, color=color.orange)
earmuff_right = earmuff_left.clone(pos=vec(6, 0, 0))
arc_shape = shapes.arc(radius=6, angle1=0, angle2=pi)
head_band = extrusion(shape=arc_shape, path=[vec(0,0,1),vec(0,0,-1)],color=color.black)