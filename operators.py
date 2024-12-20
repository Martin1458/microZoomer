import bpy # type: ignore
import bpy_extras # type: ignore
from . import editRR

class SimpleOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.simple_operator"
    bl_label = "Simple Object Operator"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        print("Im being executed :( final :)")
        editRR.editRRfunc()
        return {'FINISHED'}

class PrintDiv(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.print_div"
    bl_label = "Print the div"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        print(f"The value of Div: {context.scene.div_num_prop}")
        print(f"The value of Block: {context.scene.block_num_prop}")
        #editRR.setRR(context.scene.div_num_prop, context.scene.block_num_prop)
        return {'FINISHED'}

class SelectRR(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.select_rr"
    bl_label = "Select the RR"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        editRR.setRR(context.scene.div_num_prop, context.scene.block_num_prop)
        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(SimpleOperator.bl_idname, text=SimpleOperator.bl_label)


def register():
    bpy.utils.register_class(SimpleOperator)
    bpy.utils.register_class(PrintDiv)
    bpy.utils.register_class(SelectRR)
    bpy.types.VIEW3D_MT_object.append(menu_func)


def unregister():
    bpy.utils.unregister_class(SimpleOperator)
    bpy.utils.unregister_class(PrintDiv)
    bpy.utils.unregister_class(SelectRR)
    bpy.types.VIEW3D_MT_object.remove(menu_func)