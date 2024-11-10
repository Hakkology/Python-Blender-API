import bpy
import math

def add_camera(location=(0, 5, 10), rotation=(math.radians(40), 0, math.radians(180))):
    bpy.ops.object.camera_add(location=location, rotation=rotation)
    bpy.context.scene.camera = bpy.context.object 