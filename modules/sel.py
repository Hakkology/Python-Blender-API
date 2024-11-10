# Under sel namespace
import bpy;
import math;

class sel:
    """Function Class for operating on SELECTED objects"""

    @staticmethod
    def ensure_object_mode():
        obj = bpy.context.active_object
        if obj and obj.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')

    @staticmethod
    def select_object():
        bpy.ops.object.select_all(action='DESELECT')
        obj = bpy.context.active_object
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj

    @staticmethod
    def translate(v):
        obj = bpy.context.active_object
        obj.location = (obj.location.x + v[0], obj.location.y + v[1], obj.location.z + v[2])

    @staticmethod
    def scale(v):
        obj = bpy.context.active_object
        obj.scale = (obj.scale.x * v[0], obj.scale.y * v[1], obj.scale.z * v[2])

    @staticmethod
    def rotate_x(v):
        obj = bpy.context.active_object
        obj.rotation_euler.x += v

    @staticmethod
    def rotate_y(v):
        obj = bpy.context.active_object
        obj.rotation_euler.y += v

    @staticmethod
    def rotate_z(v):
        obj = bpy.context.active_object
        obj.rotation_euler.z += v

