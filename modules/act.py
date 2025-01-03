import bpy

class act:
    """Function Class for operating on ACTIVE objects"""

    # Declarative
    def location(v):
        bpy.context.object.location = v

    # Declarative
    def scale(scale_value):
        """Scale the active object"""
        if isinstance(scale_value, (int, float)):
            bpy.context.active_object.scale = (scale_value, scale_value, scale_value)
        else:
            bpy.context.active_object.scale = scale_value

    def apply_scale():
        """Apply scale transformation"""
        bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)

    # Declarative
    def rotation(v):
        bpy.context.object.rotation_euler = v

    # Declarative
    def dimension(v):
        bpy.context.object.dimensions = v

    # Rename the active object
    def rename(objName):
        bpy.context.object.name = objName
