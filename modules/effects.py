import bpy
from modules.selection import select

def add_wind(location=(0, 0, 0), strength=1.0, noise=0.0, seed=1):
    """
    Adds a wind force field to the scene
    
    Args:
        location: Tuple of (x, y, z) coordinates
        strength: Wind force strength
        noise: Amount of noise/turbulence in the wind
        seed: Random seed for noise
    """
    bpy.ops.object.effector_add(type='WIND', location=location)
    wind = bpy.context.active_object
    
    # Configure wind settings
    field = wind.field
    field.strength = strength
    field.noise = noise
    field.seed = seed
    field.use_absorption = False
    
    # Set falloff
    field.falloff_type = 'SPHERE'
    field.use_max_distance = True
    field.distance_max = 20
    
    return wind

def add_turbulence(location=(0, 0, 0), strength=5.0, size=1.0, noise=0.0):
    """
    Adds a turbulence force field to the scene
    
    Args:
        location: Tuple of (x, y, z) coordinates
        strength: Turbulence force strength
        size: Size of turbulence effect
        noise: Amount of noise in the turbulence
    """
    bpy.ops.object.effector_add(type='TURBULENCE', location=location)
    turbulence = bpy.context.active_object
    
    # Configure turbulence settings
    field = turbulence.field
    field.strength = strength
    field.size = size
    field.noise = noise
    field.flow = 0.5  # How much turbulence follows flow direction
    
    # Set falloff
    field.falloff_type = 'SPHERE'
    field.use_max_distance = True
    field.distance_max = 15
    
    return turbulence

def animate_force_field(field, frames=250):
    """
    Animates a force field's strength over time
    
    Args:
        field: Force field object to animate
        frames: Number of frames for animation
    """
    # Ensure we're at frame 1
    bpy.context.scene.frame_set(1)
    
    # Set initial keyframe
    field.field.strength = 0
    field.field.keyframe_insert(data_path="strength", frame=1)
    
    # Set peak strength
    mid_frame = frames // 2
    field.field.strength = field.field.strength * 2
    field.field.keyframe_insert(data_path="strength", frame=mid_frame)
    
    # Return to initial strength
    field.field.strength = 0
    field.field.keyframe_insert(data_path="strength", frame=frames)
    
    # Add smooth interpolation
    if field.animation_data and field.animation_data.action:
        for fcurve in field.animation_data.action.fcurves:
            for keyframe in fcurve.keyframe_points:
                keyframe.interpolation = 'BEZIER'
                keyframe.handle_left_type = 'AUTO_CLAMPED'
                keyframe.handle_right_type = 'AUTO_CLAMPED'