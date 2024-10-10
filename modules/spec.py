import bpy

class spec:
    """Function Class for operating on SPECIFIED objects"""

    # Declarative
    def scale(objName, v):
        bpy.data.objects[objName].scale = v

    # Declarative
    def location(objName, v):
        bpy.data.objects[objName].location = v

    # Declarative
    def rotation(objName, v):
        bpy.data.objects[objName].rotation_euler = v
