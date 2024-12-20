import bpy # type: ignore
import bpy_extras # type: ignore

class VIEW3D_PT_my_custom_panel(bpy.types.Panel):  # class naming convention ‘CATEGORY_PT_name’
    # where to add the panel in the UI
    bl_space_type = "VIEW_3D"  
    bl_region_type = "UI" 

    bl_category = "My Custom Panel category"  # found in the Sidebar
    bl_label = "My Custom Panel label"  # found at the top of the Panel

    def draw(self, context):
        layout = self.layout
        """define the layout of the panel"""
        row = layout.row()
        row.operator("mesh.primitive_cube_add", text="Add Cukkkkbe")
        row = layout.row()
        row.operator("object.simple_operator")
        # add a number input
        row = layout.row()
        row.label(text="Number of divisions:")
        row = layout.row()
        row.prop(context.scene, "div_num_prop")
        row = layout.row()
        row.prop(context.scene, "block_num_prop")
        row = layout.row()
        row.operator("object.print_div")

def register():
    bpy.utils.register_class(VIEW3D_PT_my_custom_panel)

    bpy.types.Scene.div_num_prop = bpy.props.IntProperty \
      (
        name = "Division num",
        description = "The number of divisions of the render region",
        default = 1,
        soft_min = 1
      )
    
    bpy.types.Scene.block_num_prop = bpy.props.IntProperty \
      (
        name = "Block num",
        description = "The number of the block to render",
        default = 1,
        soft_min = 1
      )
def unregister():
    bpy.utils.unregister_class(VIEW3D_PT_my_custom_panel)

    bpy.types.Scene.div_num_prop
    bpy.types.Scene.block_num_prop

