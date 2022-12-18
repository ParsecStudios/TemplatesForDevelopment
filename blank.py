from ursina import *

game = Ursina()

sphere = Entity(model = 'sphere', color=color.blue)
def update():
    sphere.rotation_x += 0.3
    sphere.rotation_y += 0.7
update()

window.render_mode = 'wireframe'

cube = Entity(model = 'cube', color=color.yellow, position=Vec3(2,3,4))

game.run()