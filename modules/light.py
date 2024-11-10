import bpy

def create_point_light(location=(0, 0, 0), energy=1000, color=(1, 1, 1)):
    """
    Creates a point light at the specified location.
    :param location: The location of the point light.
    :param energy: The brightness of the light.
    :param color: The color of the light.
    """
    bpy.ops.object.light_add(type='POINT', location=location)
    light = bpy.context.object
    light.data.energy = energy
    light.data.color = color
    return light

def create_directional_light(location=(0, 0, 10), rotation=(0, 0, 0), energy=1000, color=(1, 1, 1)):
    """
    Creates a directional (sun) light at the specified location and rotation.
    :param location: The location of the sun light.
    :param rotation: The rotation of the light, affecting the direction it shines.
    :param energy: The brightness of the light.
    :param color: The color of the light.
    """
    bpy.ops.object.light_add(type='SUN', location=location)
    light = bpy.context.object
    light.rotation_euler = rotation
    light.data.energy = energy
    light.data.color = color
    return light

def create_spot_light(location=(0, 0, 5), rotation=(0, 0, 0), energy=1000, color=(1, 1, 1), spot_size=0.785):
    """
    Creates a spot light at the specified location and rotation.
    :param location: The location of the spot light.
    :param rotation: The rotation of the light, affecting the direction it shines.
    :param energy: The brightness of the light.
    :param color: The color of the light.
    :param spot_size: The size of the spotlight cone in radians (default is 45 degrees).
    """
    bpy.ops.object.light_add(type='SPOT', location=location)
    light = bpy.context.object
    light.rotation_euler = rotation
    light.data.energy = energy
    light.data.color = color
    light.data.spot_size = spot_size
    return light