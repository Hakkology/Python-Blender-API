import bpy
import random
import math
from modules.create import create
from modules.act import act
from modules.selection import select
from modules.delete import delete_all
from modules.rigidbody import setup_rigidbody_world, add_rigidbody
from modules.material import makeStripedMaterial, setMaterial, assignMaterialsToSphere  
from modules.light import create_point_light, create_directional_light

def test7():
    # Delete all existing objects
    delete_all()
    
    # Set up the RigidBody world
    setup_rigidbody_world()

    # Add a point light at the center above the scene
    create_point_light(location=(0, 0, 10), energy=1000, color=(1, 1, 1))
    create_directional_light(location=(0, 0, 10), rotation=(math.radians(45), math.radians(45), math.radians(45)), energy=1, color=(1, 1, 1))
    
    # Create 80 spheres with random scale, rigidbody, and striped material
    for i in range(50):
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
        random_location = (random.uniform(-5, 5), random.uniform(-5, 5), random.uniform(1, 10))
        act.location(random_location)
        
        assignMaterialsToSphere(obj, stripe_count=10)

        # Testing node functionality, works well. Disabled and archived for future use.
        # # Create material with stripes
        # mat = makeStripedMaterial(f"StripedMaterial_{i}", stripe_count=6)
        
        # # Assign the material to the object
        # setMaterial(obj, mat)

