import bpy

def add_bevel(obj, width=0.02, segments=3):
    """Add bevel modifier to object with given parameters"""
    bevel = obj.modifiers.new(name="Bevel", type='BEVEL')
    bevel.width = width
    bevel.segments = segments
    bevel.limit_method = 'ANGLE'
    bevel.angle_limit = 0.785398  # 45 degrees in radians