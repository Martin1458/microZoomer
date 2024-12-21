import bpy # type: ignore
import bpy_extras # type: ignore

bl_info = {
    "name": "Micro Zoomer",
    "author": "Martin Trasak",
    "description": "",
    "blender": (2, 80, 0),
    "version": (0, 0, 1),
    "location": "",
    "warning": "",
    "category": "Generic",
}
from . import operators
from . import ui

def register():
    operators.register()
    ui.register()

def unregister():
    operators.unregister()
    ui.unregister()


if __name__ == "__main__":
    register()


#https://github.com/lunadigital/blender-addon-template/blob/master/__init__.py