import bpy
import os
import random
import math
from modules.create import create
from modules.importasset import import_obj
from modules.physics import setup_rigidbody_world, add_rigidbody
from modules.material import assignColorMaterial
from modules.selection import select
from modules.act import act
from modules.sel import sel
from modules.light import create_point_light, create_directional_light

def final2():
    project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Add lights for better visibility
    create_point_light(location=(0, 0, 10), energy=1000, color=(1, 1, 1))
    create_directional_light(
        location=(0, 0, 10), 
        rotation=(math.radians(45), 0, 0),
        energy=1, 
        color=(1, 1, 1)
    )
    
    # Setup physics world
    setup_rigidbody_world(gravity=(0, 0, -2))
    
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
    
    # Import and setup snowflakes
    snowflake_path = os.path.join(project_dir, 'visuals', 'snowFlakeXobj.obj')
    snowflakes = []
    
    for i in range(200):
        snowflake = import_obj(snowflake_path, f'Snowflake_{i}')
        select(snowflake.name)
        
        # Random position
        sel.translate((
            random.uniform(-5, 5),
            random.uniform(-5, 5),
            random.uniform(8, 18)
        ))
        
        # Random rotation - using act instead of sel
        act.rotation((
            random.uniform(0, 3.14159),
            random.uniform(0, 3.14159),
            random.uniform(0, 3.14159)
        ))
        
        # Scale
        sel.scale((10, 10, 10))
        act.apply_scale()
        
        # Add rigid body physics
        add_rigidbody(snowflake, body_type='ACTIVE')
        
        # Add white material
        assignColorMaterial(
            snowflake, 
            f'SnowflakeMaterial_{i}', 
            color=(1, 1, 1, 1),
            metallic=0.3,
            roughness=0.2
        )
        
        snowflakes.append(snowflake)