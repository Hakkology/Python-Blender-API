import bpy
import os
import random
import math
from modules.create import create
from modules.importasset import import_obj
from modules.physics import setup_rigidbody_world, add_rigidbody, add_rigidbody_with_effects
from modules.material import assignColorMaterial
from modules.selection import select, mode
from modules.keyframe import animate_falling_text
from modules.act import act
from modules.sel import sel
from modules.light import create_point_light, create_directional_light
from modules.effects import add_wind, add_turbulence, animate_force_field
from modules.text import create_3d_text
from modules.camera import create_camera

def final2():
    project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Setup physics world
    setup_rigidbody_world(gravity=(0, 0, -2))

    # Add lights for better visibility
    create_point_light(location=(0, 0, 10), energy=1000, color=(1, 1, 1))
    create_directional_light(
        location=(0, 0, 10), 
        rotation=(math.radians(45), 0, 0),
        energy=1, 
        color=(1, 1, 1)
    )

    camera = create_camera(
        location=(0, -15, 10),  # Plane'in merkezinden biraz geride ve yukarıda
        rotation=(math.radians(45), 0, 0)  # 45 derece aşağı bakış
    )
    bpy.context.scene.camera = camera
    
    # Create background plane with snowy fog texture
    background = create.mesh_plane(
        'SnowyBackground',
        texture_path=os.path.join(project_dir, 'visuals', 'snowyFog.png')
    )
    
    # Scale and position the background plane
    select(background.name)
    sel.scale((48, 27, 1))
    sel.rotate_x(math.radians(90)) 
    sel.translate((0, 10, 10))
    act.apply_scale()

    # Add 3D text
    text = create_3d_text(
        "2025",
        location=(0, 8, 5),
        size=10.0,
        extrude=0.5
    )
    
    select(text.name)
    sel.rotate_x(math.radians(90))
    animate_falling_text(text, start_frame=1, end_frame=250, start_z=15, end_z=5)

    wind = add_wind(
        location=(0, 1, 13),
        strength= 0.005,  # Arttırıldı
        noise= 0.2      # Arttırıldı
    )
    animate_force_field(wind, frames=250)
    
    turbulence = add_turbulence(
        location= (0, 1, 8),
        strength= 0.005,   # Arttırıldı
        size= 2.0,      # Arttırıldı
        noise= 0.2       # Arttırıldı
    )
    animate_force_field(turbulence, frames=250)
    
    # Import and setup snowflakes
    snowflake_path = os.path.join(project_dir, 'visuals', 'snowFlakeXobj.obj')
    snowflakes = []
    
    for i in range(200):
        snowflake = import_obj(snowflake_path, f'Snowflake_{i}')
        select(snowflake.name)
        
        # Random position
        sel.translate((
            random.uniform(-5, 5),
            random.uniform(0, 2),
            random.uniform(8, 18)
        ))
        
        # Random rotation - using act instead of sel
        act.rotation((
            random.uniform(0, 3.14159),
            random.uniform(0, 3.14159),
            random.uniform(0, 3.14159)
        ))
        
        # Scale
        sel.scale((5, 5, 5))
        act.apply_scale()
        
        # Add rigid body physics
        add_rigidbody_with_effects(snowflake, body_type='ACTIVE', mass=1)
        
        # Add white material
        assignColorMaterial(
            snowflake, 
            f'SnowflakeMaterial_{i}', 
            color=(1, 1, 1, 1),
            metallic=0.3,
            roughness=0.2
        )
        
        snowflakes.append(snowflake)