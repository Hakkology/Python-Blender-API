import bpy
import random
import math
from modules.create import create
from modules.act import act
from modules.selection import select, mode
from modules.physics import setup_rigidbody_world, add_rigidbody, create_partial_spherical_ground
from modules.material import assignMaterialsToSphere  
from modules.camera import add_camera  
from modules.light import create_point_light, create_directional_light

def homework1():
    # Set up the RigidBody world
    setup_rigidbody_world()
    # Create partial spherical ground plane
    create_partial_spherical_ground()
    # Add a camera if none exists
    if not bpy.context.scene.camera:
        add_camera()

    # Add a point light at the center above the scene
    create_point_light(location=(0, 0, 10), energy=1000, color=(1, 1, 1))
    create_directional_light(location=(0, 0, 10), rotation=(math.radians(45), math.radians(45), math.radians(45)), energy=1, color=(1, 1, 1))
    
    # Create 80 spheres with random scale, rigidbody, and striped material
    for i in range(500):
        sphere_name = f"Sphere_{i}"
        
        # Create sphere
        create.sphere(sphere_name)
        
        # Activate the sphere object
        obj = select(sphere_name)
        
        # Add RigidBody
        add_rigidbody(obj, body_type='ACTIVE')
        
        # Set random scale
        random_scale = random.uniform(0.2, 1.2)
        act.scale((random_scale, random_scale, random_scale))
        
        # Set random position
        random_location = (random.uniform(-8, 8), random.uniform(-5, 5), random.uniform(1, 10))
        act.location(random_location)
        
        assignMaterialsToSphere(obj, stripe_count=10)
