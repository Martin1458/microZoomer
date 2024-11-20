import bpy # type: ignore
import bpy_extras # type: ignore

def editRRfunc():
    # Setup
    scene = bpy.data.scenes['Scene']
    cam = bpy.data.objects['Camera']
    objs = bpy.data.objects


    scene.render.use_border = True
    scene.render.border_min_x = .3
    scene.render.border_min_y = .3
    scene.render.border_max_x = .7
    scene.render.border_max_y = .7

    print(scene.render.resolution_x)
    print(scene.render.resolution_y)

