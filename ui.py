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
        #row = layout.row()
        #row.operator("mesh.primitive_cube_add", text="Add Cukkkkbe")
        #row = layout.row()
        #row.operator("object.simple_operator")
        # input fields
        row = layout.row()
        row.prop(context.scene, "div_num_prop")
        row = layout.row()
        row.prop(context.scene, "block_num_prop")
        # buttons (mostly testing)
        row = layout.row()
        row.operator("object.print_div")  
        row = layout.row()
        row.operator("object.select_rr")  
        # output dir path
        row = layout.row()
        row.label(text="Output dir path:")
        row = layout.row()
        row.prop(context.scene, "output_dir_prop")
        # Check if the dir path is a dir path not a file path
        if context.scene.output_dir_prop[-1] != "/" and context.scene.output_dir_prop[-1] != "\\":
            row = layout.row()
            row.label(text="The output dir is not a directory path", icon='ERROR')
            row = layout.row()
            row.label(text="Do not choose a name for the output", icon='ERROR')
        # render button :3
        row = layout.row()
        row.operator("object.render_rr")
        # render all button    yippie!
        row = layout.row()
        row.operator("object.render_all")
        if context.scene.frame_start != context.scene.frame_end:
            row = layout.row()
            row.label(text="The start and end frames are not equal", icon='ERROR')
            row = layout.row()
            row.label(text="Animations are currently not supported", icon='ERROR')
              

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
    
    default_output_dir = bpy.path.abspath("//output")
    bpy.types.Scene.output_dir_prop = bpy.props.StringProperty \
        (
            name = "Output dir",
            description = "The output directory path",
            default = default_output_dir,
            subtype = 'DIR_PATH'
        )
    
def unregister():
    bpy.utils.unregister_class(VIEW3D_PT_my_custom_panel)

    bpy.types.Scene.div_num_prop
    bpy.types.Scene.block_num_prop

