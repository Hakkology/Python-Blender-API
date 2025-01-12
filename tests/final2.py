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
    setup_rigidbody_world(gravity=(0, 0, -3))

    # Add lights for better visibility
    create_point_light(location=(0, 0, 10), energy=1, color=(1, 1, 1))
    create_directional_light(
        location=(0, 0, 10), 
        rotation=(math.radians(45), 0, 0),
        energy=1, 
        color=(1, 1, 1)
    )
    
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

   # Basit kamera ayarı
    camera = create_camera(
        location=(0, -50, 10),  # Mesh'in önünde ve ortasında
        rotation=(math.radians(90), 0, 0)  # Düz bakış
    )

    # Kamera ayarları
    camera.data.type = 'ORTHO'  # Perspektif yerine orthographic kullan
    camera.data.ortho_scale = 48  # Mesh'in genişliği kadar görüş alanı

    bpy.context.scene.camera = camera
    # Add 3D text
    text = create_3d_text(
        "2025",
        location=(0, 8, 5),
        size=10.0,
        extrude=0.5
    )
    
    select(text.name)
    sel.rotate_x(math.radians(90))
    animate_falling_text(text, start_frame=1, end_frame=250, start_z=15, end_z=0)


    wind = add_wind(
        location=(0, 0, 10),      # Merkezi konuma al
        strength=.4,             # Daha güçlü
        noise=0.8                 # Daha fazla rastgelelik
    )
    animate_force_field(wind, frames=250)
    
    turbulence = add_turbulence(
        location=(0, 0, 8),       # Merkezi konuma al
        strength=0.4,             # Daha güçlü
        size=5.0,                 # Daha geniş etki alanı
        noise=0.8                 # Daha fazla rastgelelik
    )
    animate_force_field(turbulence, frames=250)
    
    # Import and setup snowflakes
    snowflake_path = os.path.join(project_dir, 'visuals', 'snowFlakeXobj.obj')
    snowflakes = []
    
    for i in range(120):
        snowflake = import_obj(snowflake_path, f'Snowflake_{i}')
        select(snowflake.name)
        
        # Random position
        sel.translate((
            random.uniform(-2, 2),    # Daha dar x aralığı
            random.uniform(-1, 1),    # Daha dar y aralığı
            random.uniform(4, 9)      # Daha alçak z aralığı
        ))
        
        # Random rotation - using act instead of sel
        act.rotation((
            random.uniform(0, math.pi),
            random.uniform(0, math.pi),
            random.uniform(0, math.pi)
        ))
        
        # Scale
        sel.scale((5, 5, 5))
        act.apply_scale()
        
        # Add rigid body physics
        add_rigidbody_with_effects(snowflake, body_type='ACTIVE', mass= .1)
        
        # Add white material
        assignColorMaterial(
            snowflake, 
            f'SnowflakeMaterial_{i}', 
            color=(1, 1, 1, 1),
            metallic=0.3,
            roughness=0.2
        )
        
        snowflakes.append(snowflake)