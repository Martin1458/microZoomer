import bpy # type: ignore
import bpy_extras # type: ignore

class VIEW3D_PT_my_custom_panel(bpy.types.Panel):  # class naming convention ‘CATEGORY_PT_name’
    # where to add the panel in the UI
    bl_space_type = "VIEW_3D"  
    bl_region_type = "UI" 

    bl_category = "My Custom Panel category"  # found in the Sidebar
    bl_label = "My Custom Panel label"  # found at the top of the Panel

    def draw(self, context):
        """define the layout of the panel"""
        row = self.layout.row()
        row.operator("mesh.primitive_cube_add", text="Add Cukkbe")
        row = self.layout.row()
        row.operator("object.simple_operator")

def register():
    bpy.utils.register_class(VIEW3D_PT_my_custom_panel)


def unregister():
    bpy.utils.unregister_class(VIEW3D_PT_my_custom_panel)

