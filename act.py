import bpy

class act:
    """Function Class for operating on ACTIVE objects"""

    # Declarative
    def location(v):
        bpy.context.object.location = v

    # Declarative
    def scale(v):
        bpy.context.object.scale = v

    # Declarative
    def rotation(v):
        bpy.context.object.rotation_euler = v

    # Declarative
    def dimension(v):
        bpy.context.object.dimensions = v

    # Rename the active object
    def rename(objName):
        bpy.context.object.name = objName
