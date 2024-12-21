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

class RenderRR(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.render_rr"
    bl_label = "Render the RR"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        # Check output dir
        #check if the output dir string ends with a slash or a backslash
        #if context.scene.output_dir_prop[-1] != "/" and context.scene.output_dir_prop[-1] != "\\":
        
        # Check if the number of divisions is valid
        if context.scene.div_num_prop < 1:
            print("The number of divisions must be at least 1")
        
        scene = bpy.data.scenes['Scene']

        bpy.context.scene.render.filepath = bpy.context.scene.output_dir_prop+"/render.png"
        scene.render.use_border = True
        scene.render.use_crop_to_border = False
        bpy.ops.render.render(write_still=True)
        return {'FINISHED'}

class RenderAll(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.render_all"
    bl_label = "Render All"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        # Check output dir
        #check if the output dir string ends with a slash or a backslash
        #if context.scene.output_dir_prop[-1] != "/" and context.scene.output_dir_prop[-1] != "\\":
            
        # Check if the number of divisions is valid
        if context.scene.div_num_prop < 1:
            print("The number of divisions must be at least 1")

        scene = bpy.data.scenes['Scene']

        scene.render.use_border = True
        scene.render.use_crop_to_border = False
        all_blocks = context.scene.div_num_prop * context.scene.div_num_prop
        for i in range(1, all_blocks+1):
            print(f"Rendering block: {i}")
            row, col = editRR.setRR(context.scene.div_num_prop, i)
            bpy.context.scene.render.filepath = f"{bpy.context.scene.output_dir_prop}/c{col}r{row}.png"
            bpy.ops.render.render(write_still=True)
        return {'FINISHED'}
    
def menu_func(self, context):
    self.layout.operator(SimpleOperator.bl_idname, text=SimpleOperator.bl_label)


def register():
    bpy.utils.register_class(SimpleOperator)
    bpy.utils.register_class(PrintDiv)
    bpy.utils.register_class(SelectRR)
    bpy.utils.register_class(RenderRR)
    bpy.utils.register_class(RenderAll)
    bpy.types.VIEW3D_MT_object.append(menu_func)


def unregister():
    bpy.utils.unregister_class(SimpleOperator)
    bpy.utils.unregister_class(PrintDiv)
    bpy.utils.unregister_class(SelectRR)
    bpy.utils.unregister_class(RenderRR)
    bpy.utils.unregister_class(RenderAll)
    bpy.types.VIEW3D_MT_object.remove(menu_func)